import pandas as pd
from userManagement.controller.UserController import UserController

class UserView:

    @staticmethod
    def register():
        from userManagement.entity.User import User
        print("[사용자 등록 화면]")
        username = input("사용자 이름 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")

        response = UserController.registerUser(User(
            username=username,
            password=password,
            name=name,
            email=email
        ))

        if not response.__dict__.get("body"):
            print("데이터를 추가하는 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")

    @staticmethod
    def showAllUser():
        response = UserController.getUsersAll()
        print("[ 전체 사용자 조회 ]")
        if bool(response.body):
            print(pd.DataFrame(response.body))
        else:
            print("조회 할 데이터가 없습니다.")

    @staticmethod
    def showFindUser():
        print("[ username으로 사용자 정보 검색 ]")
        username = input("검색하실 사용자이름을 입력하세요 >>> ")
        response = UserController.getUser(username)
        if bool(response.body):
            print(pd.Series(response.body))
        else:
            print("조회 할 데이터가 없습니다.")



