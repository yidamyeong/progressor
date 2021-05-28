import uuid
import time

# 고정된 값을 포함한 UUID

now = str(int(time.time()))
print('현재시간(Unix epoch time): {0}'.format(now))

uuid_str = str(uuid.uuid4())
print('생성된 UUID={0}'.format(uuid_str))

new_uuid_str = now[0:8] + '-' + now[8:10] + '00-' + uuid_str[14:]
print('새로 만든 UUID={0}'.format(new_uuid_str))
