import requests
import warnings
from pprint import pprint
#인증키파일 추가 key="인증번호"
from api_key import key




# 쿼리파라미터 제작 함수

def fild_check(dic):
    """
    요청받은 쿼리파라미터의 필드명을 검수. 잘못된 필드명 확인시 경고발생
    :param dic: 요청할 쿼리 파라미터 딕셔너리 객체
    :return: 문제없는 쿼리 파라미터
    """
    # 필드명 목록
    li_fild = ["makingNation", "recallName", "recallState", "actions", "productContents", "recallAmount",
               "harmContents", "accidentExam", "signDate", "rc_req_No", "userName", "userPhone", "recallNationType",
               "confirmUID", "recallType", "companyName", "harmLevel", "harmCause", "harmFlawInfo", "recallAction",
               "recallMeans", "publicDate", "makeTerm1", "makeTerm2", "sellTerm1", "sellTerm2", "actionTerm1",
               "actionTerm2", "makeAmount", "sellAmount", "recallActionVol", "saleCompany", "importCompany", "linkURL",
               "linkID", "closeCheck", "productCategory", "recallAppType", "productUID", "productName", "trademark",
               "model", "serialNumber"]
    # 잘못된 필드명 목록
    name_error = []

    # 필드 검수 시작
    for fild in dic.keys():
        if not fild in li_fild: # 잘못된 필드명만 추출
            name_error.append(fild)
    if len(name_error) == 0:
        return dic  # 문제 없을시 원래 dic객체 반환
    else:
        warnings.warn("다음 필드명이 일치 하지 않습니다. : {0}".format(name_error),SyntaxWarning)

def muti_fild(dic):    # 다중 필드 쿼리파라미터 생성
    fild_list=[]
    for fild in dic:
        fild_list.append('{{"{key}":"{val}"}}'.format(key=fild,val=dic[fild]))
    return ",".join(fild_list)

# 할일 : search 함수 코드 테스트
def search(dic, mode="one"):
    """
    model_query 파라미터 생성하는 함수
    :param dic: 검색필드를 담은 필드
    :param mode: and,or 검색시 표시
    :return: model_query터 요청 파라미터
    """
    params = {}
    if mode == "one":
        # 필드 수량 검사
        if len(dic) != 1:   # 질의할 필드가 한개가 아닌경우 오류발생
            warnings.warn("한개의 필드에 대해서만 질의해야 합니다.",SyntaxWarning)
        # 파라미터 생성
        params["model_query"] = "{query}".format(query=dic)
        return params
    elif mode == "and":
        # 필드 수량 검사
        if not len(dic) >= 2:  # 질의할 필드가 2개이상이 아닌역우 오류 발생
            warnings.warn("and 질의시 2개 이상의 필드에 대해 질의해야 합니다.", SyntaxWarning)

        dic = muti_fild(dic)
        params["model_query"] = "{"+"$and: [{query}]".format(query=dic)+"}"
        return params
    elif mode == "or":
        # 필드 수량 검사
        if not len(dic) >= 2:  # 질의할 필드가 2개이상이 아닌역우 오류 발생
            warnings.warn("or 질의시 2개 이상의 필드에 대해 질의해야 합니다.", SyntaxWarning)

        dic = muti_fild(dic)
        params["model_query"] = "{" + "$or: [{query}]".format(query=dic) + "}"
        return params

def make_params(search,d_mode="page"):
    # 3가지 파라미터의 딕셔너리값을 받은후 최종에서 취합

    return params

# api 요청 함수
def request_api(params,mode="page"):
    url = "http://www.ibtk.kr/recallDetail_api/{key}".format(key=key())
    r = requests.get(url,params=params)
    data = r.json()
    if mode == "page":
        # page형태로 받은 자료를 정리하는 함수
        pass
    elif mode == "list":
        # list형태로 받은 자료를 정리하는 함
        pass
    return data

# dat정리 함수


# test 파라미터
params = {"model_query_pageable":'{"enable":"true","pageSize":2}',"model_query_fields":'{"productName":1}'}
pprint(request_api(params))