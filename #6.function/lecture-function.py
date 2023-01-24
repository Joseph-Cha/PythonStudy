def opeon_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: 
        print("출금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commision = 100
    return commision, balance - money - commision

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commision, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commision, balance))

def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")

# 키워드를 통해 파라미터 값의 순서를 바꿀 수 있다.
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="파이썬", name="유재석", age=20)

# end=" " -> print문이 끝날 때 줄바꿈을 하지 않고 한칸 띄워서 출력
def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")
    