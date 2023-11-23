from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/') 
#main = blueprint의 별칭
#url_prefix : 라우팅 함수 에너테이션 URL앞에 붙일 기본 접두어 URL


@bp.route('/hello')
def hello_pybo():
    return "Hello, pybo!"

@bp.route('/')
def index():
    return 'Pybo index'