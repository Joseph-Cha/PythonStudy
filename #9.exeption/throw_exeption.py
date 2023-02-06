try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫번째 자리 숫자: "))
    num2 = int(input("두번째 자리 숫자: "))
    if num1 >= 10 or num2 > 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
