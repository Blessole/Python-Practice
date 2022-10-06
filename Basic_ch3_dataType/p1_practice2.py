# 파이썬에서 자료형 타입 확인하기 : type() 함수!

a = input('숫자 하나 입력')
print(type(a))
# <class 'str'> 로 출력

b = int(a)
print(type(b))
# <class 'int'> 로 출력

c = float(a)
print(type(c))
# <class 'float'> 로 출력


# 만약 a 에 문자를 여러 개 입력시 > b랑 c에서 오류남
