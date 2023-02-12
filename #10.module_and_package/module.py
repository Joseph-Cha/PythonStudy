import theater_module

theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
theater_module.price_soldier(5) # 5명 군인이 영화보러 갔을 때

import theater_module as mv # 모듈의 별명
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # theater_module의 모든 기능 사용
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 필요한 함수만 정의
price(4)
price_morning(5)
price_soldier(3) # 에러

from theater_module import price_soldier as price
price(3) # call price_soldier
