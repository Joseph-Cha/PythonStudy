# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3
print(5%3)  # 나머지
print(5//3) # 몫

print(10 > 3)
print(10 >= 3)
print(10 < 3)
print(10 <= 3)

print(3 == 3)
print(3 + 4 == True)

print(1 != 3)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 > 5))

print (5 > 4 > 3)
print (5 > 4 > 7)

# 숫자 처리 함수
print(abs(-5))      # 절대값
print(pow(4, 2))    # 제곱
print(max(5, 12))   # 최대값
print(min(5, 12))   # 최소값

print(round(3.14))  # 반올림

from math import *
print(floor(4.99))  # 내림
print(ceil(3.14))   # 올림
print(sqrt(16))     # 제곱근

# 랜덤 함수
from random import *
print(random())                 # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)            # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))       # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)   # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1, 11))         # 1 ~ 10 이하의 임의의 값 생성

print(randint(1, 10))           # 1 ~ 10 이하의 임의의 값 생성, 처음과 끝 포함