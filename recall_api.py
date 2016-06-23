import requests
import warnings
from pprint import pprint
# 인증키파일 추가 key="인증번호"
from api_key import key


class recallAPI:
    """
    리콜API에 연결하고 자료를 요청하는 객체입니다

    """
    def __init__(self):


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

class search:
    """
    필드 검색 인수를 받아 취합, 이후 리콜api의 매개변수로 활용
    """
    pass


class page:
    """
    페이징 처리 인수를 받아 취합, 리콜api의 매개변수로 활용
    """
    pass


class view:
    """
    출력 필드 인수를 받아 취합, 리콜api의 매개변수로 활용
    """
    pass

