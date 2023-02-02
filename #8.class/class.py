# 일반 유닛
class Unit:
    def __init__(self, name, hp): # 생성자
        # self.멤버 변수
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, damage): # 생성자
        # self.멤버 변수
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다."\
            # self.name -> 객체의 멤버 변수의 값을 출력
            # location -> 함수 인자 값을 출력
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed) -> None:
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


marine1 = AttackUnit("마린", 40, 5)
marine2 = AttackUnit("탱크", 150, 35)

# 레이스
wraith1 = AttackUnit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤
wraith2 = AttackUnit("레이스", 80, 5)
wraith2.clocking = True # 실제 클래스에는 없는 변수지만 이렇게 외부에서 변수 값을 생성 후 사용 가능

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


firebat1 = AttackUnit("파이어뱃", 50, 16)

firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

# 드랍쉽
