import sys

print("Python", "Java", "JavaScript", sep=",", end="? ") # sep == seperate , end == 문장의 끝을 ?로 변경(줄바꿈 x)
print("무엇이 더 재밌을까요?") # Python,Java,JavaScript? 무엇이 더 재밌을까요?

print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # key: subject, value: score -> tuple 형식으로 반환
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust: 왼쪽으로 정렬 후 8칸의 공간을 확보

# 은행 대기 순번표
# 001, 002, 003, ...

for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3)) # zfill: 빈공간을 0으로 채움(여기선 3개 글자까지 해당)

answer = input("아무 값이나 입력하세요: ")
print(type(answer)) # 사용자 input 값은 항상 str 타입이다.
print("입력하신 값은 {0}입니다.".format(answer))