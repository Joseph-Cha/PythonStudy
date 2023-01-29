score_file = open("score.txt", "w", encoding="utf8") # w: write
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # a: append 기능으로 작성
score_file.write("과학 : 80")
score_file.write("\n코딩 : 80")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r: read
print(score_file.read()) # 모든 내용 출력
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r: read
# 한 줄 읽고, 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 수학 : 0
print(score_file.readline(), end="") # 영어 : 50
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r: read
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r: read
lines = score_file.readlines # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()