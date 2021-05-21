import datetime
import time

# t1 시간 기록 (특정 날짜)
t1 = datetime.datetime(
    year=2021, month=5, day=21, hour=22, minute=4, second=00
)

while True:
    now = datetime.datetime.now()
    print('현재 시간: {0}'.format(now))
    print('루프 만료 시간: {0}'.format(t1))
    if t1 <= now:
        break

    time.sleep(1)

# 단조 시간으로도 한 달을 잴 수는 있지만, 한 달은 30일과 31일이 있고 윤년도 염두에 두고 계산해야 한다.
# 따라서 한 달 이상 주기를 두고 실행하는 작업은 실제 시간을 기준으로 하는 게 좋다.
