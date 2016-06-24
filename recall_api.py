import requests
import warnings
import collections
from pprint import pprint
# 인증키파일 추가 key="인증번호"
from api_key import key

# API 매개변수 생성 함수
def make_parm(name,parm_list):
    """
    API매개변수 명과 각 매개변수 필드 리스트를 받아 none을 제외한 필드로 매개변수를 생성한다
    :param name: 매개변수명
    :param list: 각 매개변수 필드
    :return:
    """
    parm = []
    for f in parm_list:
        if f != None:
            parm.append(f)
    return '''\'{{ {} }}\' '''.format(",".join(parm))


class Search:
    """
    필드 검색 인수를 받아 취합, 이후 리콜api의 매개변수로 활용
    """
    pass


class Page:
    """
    페이징 처리 인수를 받아 취합, 리콜api의 매개변수로 활용
    """
    def __init__(self, enable=True, page_num=0, page_size=10):
        """
        매개변수 인수값 초기화
        """
        self.enable = '\"enable\" : {}'.format(enable)
        self.num = '\"pageNumber\" : {}'.format(page_num)
        self.size = '\"pageSize\" : {}'.format(page_size)
        self.sort = []
        self.sortOder = None
        self.parms = None

    def Sortoder(self,fild,valv):
        if valv not in (-1,1):
            print("값은 -1 혹은 1 이어야 합니다.")
            return

        exi_fild = [x['property'] for x in self.sort]
        sort = list(self.sort)

        if fild not in exi_fild:
            sort.append({"property": fild, "direction" : valv})
        else:
            for d in sort:
                if d["property"] == fild:
                    d["direction"] = valv

        self.sort = sort
        self.sortOder = '\"sortOder\" : {}'.format(self.sort)

    def Delsort(self):
        self.sort = []
        self.sortOder = None


    def __repr__(self):
        # page 매개변수를 반환
        parmname = "model_query_pageable"
        fild = [ self.enable, self.num, self.size, self.sortOder ]
        parm = []
        for f in fild:
            if f != None:
                parm.append(f)
        return make_parm(parmname,parm)


class View:
    """
    출력 필드 인수를 받아 취합, 리콜api의 매개변수로 활용
    """
    def __init__(self,fild,valv):
        if valv not in (1,0):
            print("출력은 1, 출력안함은 0 입니다")
            return

        self.parm = ['"{}" : {}'.format(fild,valv)]

    def __repr__(self):
        parmaname = "model_query_fields"
        return make_parm(parmaname,self.parm)


class recall:
    """
    리콜API에 연결하고 자료를 요청하는 객체입니다

    """
    def __init__(self):
        self.search = None
        self.page = None
        self.view = None
        self.parms = {}

    def Request(self):
        api_key = key()
        url = "http://www.ibtk.kr/recallDetail_api/{key}".format(key=api_key)

        #매겨변수 취합
        parms = [self.search,self.page,self.view]
        for parm in parms:
            if parm != None:
                self.parms.update(parm)

        #자료 요청
        r = requests.get(url,params=self.parms)
        self.data = r.json()
        return self.data


    def Search(self,search):
        # 검색 매개변수 클래스를 받음
        self.search = {"model_query" : search }

    def Page(self,page):
        # 페이징 매개변수 클래스를 받음
        self.page = {"model_query_pageable" : page }

    def View(self,view):
        # 출력여부 매개변수 클래스를 받음
        self.view = {"model_query_fields" : view }
