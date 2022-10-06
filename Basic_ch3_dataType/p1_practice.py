# input()으로 숫자 입력 받기

# 예시 1
# 숫자 7을 입력하더라도 python은 자동으로 str 방식으로 저장함
a = input('숫자를 입력하세요.')

# int 로 변환해주기 ▼
a = int(input('숫자를 입력하세요.'))

print(a+a)


# 예시 2
# range() 함수의 변수로는 int형만 들어가야 함
num = 5.0
range(num)          # float형이라 오류나!
range(int(num))    # int형으로 변경해서 들어감
