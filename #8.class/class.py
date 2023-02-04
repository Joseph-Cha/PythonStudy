from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # 생성자
        # self.멤버 변수
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닉 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}"\
            .format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, damage, speed): # 생성자
        # self.멤버 변수
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다."\
            # self.name -> 객체의 멤버 변수의 값을 출력
            # location -> 함수 인자 값을 출력
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스탬팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

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
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player: gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine): # isinstance: 지금 만들어진 객체가 어떤 클래스의 객체인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 21)) # 5 ~ 20

game_over()

# -------------------------------- 실습 ----------------------------
class BuildingUnit(Unit):
    def __init__(self, name, hp, locatation):
        super().__init__(name, hp, 0) # 부모 클래스 초기화
        self.location = locatation

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

# 벌처
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

# 서플라이 디폿
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass # 아무것도 안하고 넘어갈 때
