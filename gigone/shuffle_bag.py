# 공정한 난수, 셔플 백
# 난수가 사용자 경험에 직접적인 영향을 끼칠 때는 난수를 엄격히 제어해야 함.
# 셔플 백은 난수를 제어하는 기법으로 발생할 수 있는 모든 가능성을 한 가방에 넣고 섞는 방법.
# 공정한 게임을 만들 수 있지만 전체 요소가 너무 많거나 확률이 희박할 경우, 모든 경우의 수를 담기 위해 필요한 컨테이너 크기가 커지는 단점.

import random

# 당첨 확률: 30%
WIN_RATE = 0.3
# 뽑기 횟수: 10번
NUMBER_OF_DRAWS = 10

# 뽑기 컨테이너와 승/패 개수
draws = []
win_draws = int(NUMBER_OF_DRAWS * WIN_RATE)
loss_draws = NUMBER_OF_DRAWS - win_draws
print('win={0} / loss={1}'.format(win_draws, loss_draws))

# 당첨 제비를 넣습니다.
for i in range(0, win_draws):
    draws.append(1)

# 그 다음 꽝 제비를 넣습니다.
for i in range(0, loss_draws):
    draws.append(0)

# 제비를 섞습니다.
random.seed()
random.shuffle(draws)

# 제비 출력
print(draws)
# win=3 / loss=7 .. 동일
# [0, 0, 0, 0, 1, 1, 0, 0, 0, 1] .. 랜덤
