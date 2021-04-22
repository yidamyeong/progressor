a = 'abc-def g-h-ij-klm no p'

print(a.split())  # 괄호 안 아무것도 입력하지 않으면 공백 기준으로 스플릿
print(a.split('-'))  # 괄호 안 입력하면 그 문자열 기준으로 스플릿
print(a.split('m n'))
