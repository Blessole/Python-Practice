# split 함수
# 문자1.split(문자2) : 문자 2를 기준으로 문자 1을 자른다

text = input('날짜 입력 yyyy.mm.dd')
y, m, d = text.split('.')

print(text, y, m, d)
# 입력 : 2022.12.25
# 출력 : 2022.12.25 2022 12 25

# -------------------------------------------------------- #
# map(함수, 집합형태 -iterable 객체)
# 집합에서 하나씩 꺼내 함수를 거쳐 변수에 입력
a, b, c = map(int, ['1', '2', '3'])
print(a, b, c, a+b+c)

# 출력 : 1 2 3 6


# -------------------------------------------------------- #
# map과 split을 한 줄로 적으면 ▼
a, b, c = map(int, input('a b c 값 입력').split())


# map 과 split을 풀어서 써보면 ▼
text = input('a b c 값 입력')
text = text.split()
a, b, c = map(int, text)

print(a, b, c, a+b+c)
