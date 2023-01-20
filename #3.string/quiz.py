# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) 생성된 비밀번호 nav51!

email = "http://naver.com"
rule1 = email[7:]
dot_index = rule1.index(".")
rule2 = rule1[:dot_index]
length = len(rule2)
count = rule2.count("e") 
rule3 = rule2[:3] + str(length) + str(count) + "!"
 
print(rule3)