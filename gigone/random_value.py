# 유사 난수

import random

# 랜덤값을 열 번 출력
for i in range(1, 10):
    # seed 값을 현재 시간(타임스탬프)로 설정한다.
    random.seed()
    print(random.randrange(1, 10))

