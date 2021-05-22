import re


def find_pattern(pattern, string):
    match = re.findall(pattern, string)
    if not match:
        print('일치하는 데이터가 없습니다.')
        return

    print('일치하는 데이터를 찾았습니다: {0}'.format(match))


find_pattern('o', 'Hello World')
find_pattern('[a-z]', 'Hello World, 1, 2, 3, 4, 5')
find_pattern('[A-Z]', 'Hello World, 1, 2, 3, 4, 5')
find_pattern('[a-zA-Z]', 'Hello World, 1, 2, 3, 4, 5')
find_pattern('[0-9]', 'Hello World, 1, 2, 3, 4, 5')
find_pattern('[a-zA-Z0-9]', 'Hello World, 1, 2, 3, 4, 5')

# 파이썬 언어는 문자열 앞에 r을 붙여 다음과 같이 \ 파싱을 피할 수 있다.
# find_pattern(r'[\\\[\]]', r'!@#$%^&*()?><\[]')과 같다.
find_pattern(r'[\\\[\]]', r'!@#$%^&*()?><\[]')  # r 없으면 invalid

# 하나 이상의 문자 찾기
find_pattern('[a-z]+', r'Hello World, 1, 2, 3, 4, 5, !@#$%^&*()?></\[]')

# 지정한 길이의 문자열 찾기 (3글자)
find_pattern('[a-z0-9,]{3}', r'Hello World, 1,2,3,4,5, !@#$%^&*()?></\[]')

# 최소 3글자, 최대 5글자의 문자열 찾기
find_pattern('[a-z0-9,]{3,5}', r'Hello World, 1,2,3,4,5, !@#$%^&*()?></\[]')

# 주어진 문자열의 첫 3글자가 소문자 또는 대문자인지 검사
find_pattern('^[a-zA-Z]{3}', r'Hello World, 1,2,3,4,5, !@#$%^&*()?></\[]')

# 마지막 세 글자가 소문자, 대문자, 숫자가 아닌 특수문자인지 검사
find_pattern('[^a-z^A-Z^0-9]{3}$', r'Hello World, 1,2,3,4,5, !@#$%^&*()?></\[]')
