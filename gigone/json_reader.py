import json


def open_json_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return json.load(file)
        except ValueError as e:
            print('JSON 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


# message1.json 파일은 같은 디렉터리에 있어야 한다.
json_data = open_json_file('message1.json')
if not json_data:
    # 더 이상 로직을 진행할 수 없으므로 종료
    exit(0)

# 정수
num_value = json_data['number']

# 실수
float_value = json_data['pi']

# 문자열
str_value = json_data['str']

# 빈 키(None)
empty_value = json_data['null_key']

print('num_value={0}'.format(num_value))  # num_value=12345
print('float_value={0}'.format(float_value))  # float_value=3.14
print('str_value={0}'.format(str_value))  # str_value=문자열 값
print('empty_value={0}'.format(empty_value))  # empty_value=None

# 객체 안 객체 접근
json_data2 = json_data['object']
print('json_data[\'object\'][\'str2\']={0}'.format(json_data2['str2']))  # json_data['object']['str2']=문자열 값2

# 배열 접근
json_array = json_data['num_array']
for n in json_array:
    print('n={0}'.format(n))
# n=1
# n=2
# n=3
# n=4
# n=5

# 'unknown_key'를 읽는 잘못된 방법 (error 남)
# unknown_value = json_data['unknown_key']
# print('unknown_value={0}'.format(unknown_value))

# 'unknown_key'를 읽는 올바른 방법 1
try:
    unknown_value = json_data['unknown_key']
    print('unknown_value={0}'.format(unknown_value))
except KeyError:
    print('\'unknown_key\'는 존재하지 않습니다')  # 'unknown_key'는 존재하지 않습니다

# 'unknown_key'를 읽는 올바른 방법 2
if 'unknown_key' in json_data:
    unknown_value = json_data['unknown_key']
    print('unknown_value={0}'.format(unknown_value))
else:
    print('\'unknown_key\'는 존재하지 않습니다')  # 'unknown_key'는 존재하지 않습니다

# float_value 가 3 이상 3.2 미만인지 검사하는 코드
# assert 는 디버깅 환경에서만 동작한다.
assert(3 <= float_value < 3.2)

# str_value 가 null 이 아니고 문자열 길이가 0 이상인지 검사하는 코드
assert(str_value and len(str_value) > 0)

# JSON 객체와 배열을 읽을 때는 객체 내부 또는 배열 요소가 알파벳 순서나 오름차순과 같은 순서로 정렬됐다는 가정을 하지 않는 게 좋다.
# 객체나 배열 요소는 데이터를 전달하는 소프트웨어 로직이나 라이브러리에 의해 바뀔 수 있기 때문이다.
