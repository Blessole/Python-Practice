# 6009 입출력 - 문자 1개 입력받아 그대로 출력하기
c = input("문자를 입력하세요.")
print(c)

# 6010 입출력 - 정수 1개 입력받아 int로 변환하여 출력하기
c = input("정수를 입력하세요")
print(int(c))

# 6011 입출력 - 실수 1개 입력받아 변환하여 출력하기
c = input("실수를 입력하세요")
print(float(c))

# 6012 입출력 - 정수 2개 입력받아 그대로 출력하기1
a = input("첫번째 정수를 입력하세요")
b = input("두번째 정수를 입력하세요")
print(int(a))
print(int(b))

# 6013 입출력 - 문자 2개 입력받아 순서 바꿔 출력하기1
a = input("첫번째 문자를 입력하세요")
b = input("두번째 문자를 입력하세요")
print(str(b))
print(str(a))

# 6014 입출력 - 실수 1개 입력받아 3번 출력하기
a = input()
a = float(a)
print(a)
print(a)
print(a)

# 6015 입출력 - 정수 2개 입력받아 그대로 출력하기2
a, b = input().split()
print(int(a))
print(int(b))

# 6016 입출력 - 문자 2개 입력받아 순서 바꿔 출력하기2
# print 안에 ','를 찍으면 공백 하나 두고 나란히 출력됨
a, b = input().split()
print(str(b), str(a))

# 6017 입출력 - 문자 1개 입력받아 3번 출력하기
a = input()
print(a, a, a)

# 6018 입출력 - 시간 입력받아 그대로 출력하기
a, b = input().split(':')
print(a+':'+b)

# 6019 입출력 - 연월일 입력받아 순서 바꿔 출력하기
year, month, day = input().split('.')
print(day + '-' + month + '-' + year)

# 6020 입출력 - 주민번호 입력받아 형태 바꿔 출력하기
# 공문자 : ''
a, b = input().split('-')
print(a + '' + b)

# 6021 입출력 - 단어 1개 입력받아 나누어 출력하기
# s[i] = i번째 문자
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 6022 입출력 - 연월일 입력받아 나누어 출력하기
# 단순한 방법 1
s = input()
print(s[0:2], s[2:4], s[4:6])
# for문을 활용한 방법 2
s = input()
arr=[s[0:2], s[2:4], s[4:6]]
for s in arr:
    print(s, end=' ')

# 6023 입출력 - 시분초 입력받아 분만 출력하기
hour, minute, second = input().split(':')
print(minute)

# 6024 입출력 - 단어 2개 입력받아 이어 붙이기
# 키보드로 입력되는 것들은 기본적으로 문자열로 인식
a, b = input().split()
print(a+b)