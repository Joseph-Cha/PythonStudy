# quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에서 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건 2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3: random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# list = [1, 2, 3, 4, 5]
# suffle(list)
# print(sample(list, 1))

from random import *
attendants = list(range(1, 21))
print(attendants)
shuffle(attendants)
chicken = sample(attendants, 1)
chicken_num = attendants.index(chicken[0])
attendants = set(attendants)
attendants.remove(chicken_num)
attendants = list(attendants)
shuffle(attendants)
coffees = sample(attendants, 3)

print("--당첨자 발표--")
print("치킨 당첨자: " + str(chicken[0]))
print("커피 당첨자:", coffees)
print("--축하합니다--")

# 모범 답안
from random import *

users = list(range(1, 21))
shuffle(users)
winners = sample(users, 4)

print("--당첨자 발표--")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("--축하합니다--")