import requests
import warnings
from pprint import pprint
# 인증키파일 추가 key="인증번호"
from api_key import key

# API 매개변수 생성 함수
def make_parm(name,list):
    """
    API매개변수 명과 각 매개변수 필드 리스트를 받아 none을 제외한 필드로 매개변수를 생성한다
    :param name: 매개변수명
    :param list: 각 매개변수 필드
    :return:
    """
    parm = []
    for f in list:
        if f != None:
            parm.append(f)
    return '''\"{0}\" : \'{{ {1} }}\' '''.format(name,",".join(parm))

class recallAPI:
    """
    리콜API에 연결하고 자료를 요청하는 객체입니다

    """
    def __init__(self):
        pass

    def request(self):
        api_key = key()
        url = "http://www.ibtk.kr/recallDetail_api/{key}".format(key=api_key)

        #매겨변수 취합

        #자료 요청
        r = requests.get(url,)
        data = r.json()
        return data

    def search(self,C_search):
        """
        검색 매개변수 처리 메소드
        :param C_search: 검색 인스턴스를 인수르 받는다.
        :return:
        """
        pass

    def page(self,C_page):
        """
        페이징 매개변수 처리 메소드
        :param C_page: 페이징 인스턴스를 인수로 받는다.
        :return:
        """
        pass

    def view(self,C_view):
        """
        출력여부 매개변수 처리 메소드
        :param C_view:
        :return:
        """
        pass

class Search:
    """
    필드 검색 인수를 받아 취합, 이후 리콜api의 매개변수로 활용
    """
    pass


class Page:
    """
    페이징 처리 인수를 받아 취합, 리콜api의 매개변수로 활용
    """
    def __init__(self):
        """
        매개변수 인수값 초기화
        """
        self.fenable = None
        self.fnum = None
        self.fsize = None
        self.fsort = None

    def Enable(self,bool= False):
        """
        페이지 처리여부
        :param bool: 기본 False / True시 페이징 처리함
        :return:
        """
        self.fenable = '\"enable\" : {0}'.format(bool)

    def Num(self,num=0):
        """
        페이지 번호
        :param num:
        :return:
        """
        self.fnum = '\"pageNumber\" : {0}'.format(num)

    def Size(self,num=10):
        """
        페이지당 행 갯수
        :param num: 기본값 10
        :return:
        """
        self.fsize = '\"pageSize\" : {0}'.format(num)

    def Sort(self):
        """
        각 필드별 정렬 조건
        :return:
        """
        pass


    def __repr__(self):
        fild = [self.fenable,self.fnum,self.fsize,self.fsort]
        parm = []
        for f in fild:
            if f != None:
                parm.append(f)
        self.parms = '''\"model_query_pageable\" : \'{{ {0} }}\' '''.format(",".join(parm))
        return self.parms





class View:
    """
    출력 필드 인수를 받아 취합, 리콜api의 매개변수로 활용
    """
    pass

