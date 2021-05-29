# 암호학적으로 안전한 난수
# 생성 속도가 상대적으로 느리지만, 시드 값을 사용하지 않아서 예측이 불가능하다는 장점이 있다.

import os
import struct

# 랜덤값을 열 번 출력
for i in range(1, 10):
    # 운영체제에서 제공하는 기능을 사용해 랜덤하게 생성된 4바이트 값을 읽는다.
    random_four_byte = os.urandom(4)
    # 4바이트 값을 정수로 변환한 후, 출력한다.
    random_integer = struct.unpack("<L", random_four_byte)[0]
    print('hex=' + random_four_byte.hex() + ', integer=' + str(random_integer))

