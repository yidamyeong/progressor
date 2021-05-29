import random

# 랜덤값 10번 출력
for i in range(10):
    # seed 값을 0으로 설정
    random.seed(0)
    print(random.randrange(1, 10))
    # 랜덤값이 전부 똑같이 7이 나옴 -> 충분한 수(624개)의 난수만 확보할 수 있으면 다음 난수를 예측할 수 있어서
    # 시드값을 역으로 예측하는 것도 가능하다.
    # 타임스탬프처럼 단순하게 증가하며 예측이 쉬운 값을 사용하면 시드 값을 예측하는 것도 쉽기 때문에 난수 또한 쉽게 예측할 수 있다.