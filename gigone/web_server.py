# 다음 코드를 실행하기 위해선 Flask 모듈이 필요하다. (설치 완료)

import uuid
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    request_id = uuid.uuid4()
    print('API 요청 ID={0}'.format(request_id))
    return 'Hello World'


if __name__ == '__main__':
    app.run()

# 실행 후 127.0.0.1:5000 으로 접속하면 실행 결과를 볼 수 있다.
# 새로운 요청이 올 때마다 ID 가 바뀌며, 이렇게 생성한 UUID 는 요청이 끝나기 전이나 논리적인 작업이 끝나기 전까지 가지고 있거나
# 요청으로 만든 작업과 함께 데이터베이스에 넣어 관리할 수 있다.
