# package: 여러 모듈을 보관
# /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11 경로에 travel 폴더를 복사하면 사용 가능

import travel.thailand # 패키지명 또는 모듈 명만 import 할 수 있다. 클래스 이름은 안됨.

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from import 구문에서는 class를 사용 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()

from travel import * # *은 package에서 모든 것을 사용(단 공개된 것들만 사용가능)
trip_to = vietnam.VietnamPackage()

print(__name__)

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))