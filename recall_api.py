import requests
from pprint import pprint
#인증키파일 추가 key="인증번호"
from api_key import key

# 쿼리파라미터 제작 함수
# 쿼리값 검증도 추가하

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