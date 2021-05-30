# 다음 코드를 실행하기 위해서는 pyyaml 모듈이 필요하다.

import yaml


def open_yaml_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return yaml.load(file, Loader=yaml.SafeLoader)
        except yaml.parser.ParserError as e:
            print('YAML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


# message1.yaml 파일은 같은 디렉터리에 있어야 한다.
yaml_data = open_yaml_file('message1.yaml')
if not yaml_data:
    # 더 이상 로직을 진행할 수 없으므로 종료합니다.
    exit(0)

# 정수
num_value = yaml_data['number']

# 실수
float_value = yaml_data['pi']

# 문자열
str_value = yaml_data['str']

# 빈 키(None)
empty_value = yaml_data['null_key']

print('num_value={0}'.format(num_value))  # num_value=12345
print('float_value={0}'.format(float_value))  # float_value=3.14
print('str_value={0}'.format(str_value))  # str_value=문자열 값
print('empty_value={0}'.format(empty_value))  # empty_value=None

# 객체 안 객체 접근
yaml_data2 = yaml_data['object']
print('yaml_data[\'object\'][\'str2\']={0}'.format(yaml_data2['str2']))

# 배열 접근
yaml_array = yaml_data['num_array']
for n in yaml_array:
    print('n={0}'.format(n))
