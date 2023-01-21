cabinet = {3:"유재석", 100:"김태호"} # key: 3, value: 유재석
print(cabinet[3])       # 유재석
print(cabinet[100])     # 김태호

print(cabinet.get(3))   # 유재석
# print(cabinet[5])     # 키 값이 없어서 오류 후 종료
print(cabinet.get(5, "사용 가능"))   # 사용 가능 출력 후 종료 x

print(3 in cabinet) # True 
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
cabinet["A-3"] = "김종국" # 업데이트
cabinet["C-20"] = "조세호" # 추가

# 삭제
del cabinet["A-3"] 

# key 들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목용탕 폐점
cabinet.clear()
