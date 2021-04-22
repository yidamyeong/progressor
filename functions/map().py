a = input('공백으로 구분하여 입력 : ').split()
print(a)

b = map(int, a)  # 이때 리스트 a 에 숫자가 아닌 문자가 포함되어 있으면 에러남 (int 가 아니기 때문)
print(b)  # map object 주소값 출력
print(list(b))  # int 원소로 구성된 리스트 출력

x, y = b, b  # map 객체는 변수 여러 개에 저장할 수 있음
print(x)
print(y)
print(list(y))  # [] 공백으로 나옴.
