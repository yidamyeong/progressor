# 다음 코드를 실행하기 위해선 pyyaml 모듈 필요
import yaml

# 유니코드 문자열을 명시하기 위해 u를 붙이기
message2 = {
    u'number': 12345,
    u'pi': 3.14,
    u'str': u'문자열 값',
    u'null_key': None,
    u'object': {
        u'str2': u'문자열 값 2',
        u'object2': {
            u'number2': 12345
        }
    },
    u'num_array': [1, 2, 3, 4, 5],
    u'str_array': [u'one', u'two', u'three', u'four', u'five']
}

# ensure_ascii=True 인 경우에는 아스키 코드가 아닌 모든 문자열을 \uXXXX 로 표기
with open('message2.yaml', 'w', encoding='UTF8') as file:
    yaml.dump(message2, file, allow_unicode=True)

# 실행 시 message2.yaml 파일 생성

