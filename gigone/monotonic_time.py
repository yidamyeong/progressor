import time

# t1 시간 기록 (현재)
t1 = time.monotonic()

while True:
    # t2 시간 기록
    t2 = time.monotonic()
    # 이 루프가 3초 이상 실행된 경우 종료
    if t2 >= t1 + 3:
        break

    time.sleep(0.1)

# 실제 시간 차이 출력
print('t1 = {0}'.format(t1))
print('t2 = {0}'.format(t2))
print('diff = {0}'.format(t2 - t1))

# 이 코드를 더 활용하면, 범용 타이머 기능을 만들 수 있다. 이 타이머는 작업 큐에서 작업을 가져와 작업시간을 100ms 주기마다 확인하고,
# 시간이 됐을 때 다른 스레드로 작업을 넘긴 후 다음 작업을 가져와 다시 시간을 확인하는 형태로 동작한다.
# 단, 작업 큐는 반드시 실행할 시간이 가까운 순서대로 정렬되어 있어야만 한다.
