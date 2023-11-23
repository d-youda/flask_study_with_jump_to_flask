from flask import Flask

#create_app 함수를 선언하는 ㄴ방식. =>애플리케이션 팩토리
def create_app():
    '''create_app은 플라스크 내부에 정의된 함수명이다.
        다른 이름으로 변경하면 정상작동 되지 않는다'''
    
    app = Flask(__name__) #플라스크 애플리케이션 생성하는 코드
    #__name__에 모듈명 담감. __name__ ->pybo 담기는 것!

    @app.route("/") #URL과 플라스크 코드를 매핑하는 플라스크 데코레이터
    def hello_pybo():
        return 'Hello, pybo!'
    return app