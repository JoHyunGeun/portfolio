# Flask_Blog 에는 __init__파일이 없어서 패키지로 취급하지 못하기 때문에 .으로 사용을 못하는 것 같다.
from Finger.finger import app

# flaskblog 파일을 직접 실행했을 때(import한 경우가 아닌) debug mode로 실행하여 수정된 결과를 바로 확인할 수 있도록 한다.
if __name__ == '__main__':
    app.run(debug=True)