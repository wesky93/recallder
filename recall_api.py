import requests
from pprint import pprint
#인증키파일 추가 key="인증번호"
from api_key import key

# 쿼리파라미터 제작 함수
# 쿼리값 검증도
def search(dic, mode="one"):
    # 필드 목록
    # 할일 : 필드 검증용 리스트 생성
    li_fild = ["recallState","makingNation","recallName"]
    """
    model_query 파라미터 생성하는 함수
    :param dic: 검색필드를 담은 필드
    :param mode: and,or 검색시 표시
    :return: model_query터 요청 파라미터
    """
    params = {"model_query":""}
    if mode == "one":
        if
        params["model_query"] = "{query}".format(query=dic)
    elif mode == "and":
        pass    # 할일 : and 파라미터 생성하기
    elif mode == "or":
        pass    # 할일 : or 파라미터 생성하기
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