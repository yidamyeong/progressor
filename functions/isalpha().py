a = 'abc'
b = 'ab3'
c = '123'
d = 123
e = True

print(a.isalpha())  # True : 문자열의 모든 게 온전히 문자일 때
print(b.isalpha())  # False
print(c.isalpha())  # False
# print(d.isalpha())  # Error : 문자열 아닌 것(int)은 에러남
# print(e.isalpha())  # Error : 문자열 아닌 것(bool)은 에러남
