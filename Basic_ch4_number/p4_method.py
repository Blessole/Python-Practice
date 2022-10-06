# 반올림 : round(a), round(a,b)
print(round(3.33))              # 3
print(round(3.66))              # 4
print(round(3.66, 1))           # 3.7

# 절대값 : abs(a)
print(abs(3))                       # 3
print(abs(-3))                      # 3

# 제곱 : pow(a,b)
print(pow(3, 2))                     # 9
print(3**2)                           # 9

# 나눗셈 : divmod(a,b)  > 몫과 나머지를 다 표현할 때 사용함!
x, y = divmod(7, 2)
print(x)                                # 몫 3
print(y)                                # 나머지 1

# 최대값 : max(a,b,c,d...)
# 최소값 : min(a,b,c,d...)
print(max(7, 5, 1, 3))               # 7
print(min(7, 5, 1, 3))                # 1
print(max([7, 5, 1, 3]))             # 이렇게 집합 형태로 넣어줘도 가능!

# 합 : sum (집합 형태 : iterable)
print(sum(7, 5, 1, 3))               # 집합 형태가 아니라서 오류남
print(sum([7, 5, 1, 3]))             # 16
