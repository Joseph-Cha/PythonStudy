# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

subway = [10, 20, 30]
subway = ["유재석", "조세호", "박명수"]

# 조세호 몇번째?
print(subway.index("조세호"))

# 하하 추가
subway.append("하하")
print(subway)

# 정현돈 -> 유재석, 조세호 사이
subway.insert(1, "정현동")
print(subway)

# 지하철에 있는 사람 한명씩 뺌
print(subway.pop()) # 하하

# 같은 사람이 몇명?
subway.count("유재석")

# 정렬
num_list = [5, 2, 3, 3, 1]
num_list.sort() # 오름차순

num_list.reverse() # 내림차순

# 모두 지우기
num_list.clear()

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]

# 리스트 합체
num_list.extend(mix_list) 

