# quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오
#
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500 / 50 2000년

class House:
    def __init__(self, location, form, paid, year_of_complection) -> None:
        self.location = location
        self.form = form
        self.paid = paid
        self.year_of_complection = year_of_complection
    
    def print_info(self):
        print("{0} {1} {2} {3}".\
            format(self.location, self.form, self.paid, self.year_of_complection))

h1 = House("강남", "아파트", "매매 10억", "2010년")
h2 = House("마포", "오피스텔", "전세 5억", "2007년")
h3 = House("송파", "빌라", "월세 500 / 50", "2000년")

houses = [ h1, h2, h3 ]

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.print_info()
        