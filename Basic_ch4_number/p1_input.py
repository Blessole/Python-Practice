# 한 줄에 하나씩 숫자 입력받기
# 예시1
a = int(input('a 입력 : '))
b = int(input('b 입력 : '))
c = int(input('c 입력 : '))

print(a, b, c, a+b+c)    # 3  6  9  18 로 출력 됨

# 예시2
a = input('a 입력 : ')
b = input('b 입력 : ')
c = input('c 입력 : ')

print(a, b, c, a+b+c)    # 3  6  9  369 로 출력 됨


# 한 줄에 여러 개의 숫자 입력받기
a, b, c = map(int, input('a b c 값 입력').split())

print(a, b, c, a+b+c)
