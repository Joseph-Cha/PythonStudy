# input: 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))

# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir()) # [ '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'language']
import random # 외장 함수
print(dir()) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'language', 'random']

print(dir(random)) # random에서 사용 가능한 변수와 함수 리스트

lst = [1, 2, 3]
print(lst)

name = "jim"
print(dir("name")) # string에서 사용 가능한 변수와 함수 리스트

# list of python builins 검색 -> 파이썬에서 사용 가능한 내장 함수 리스트