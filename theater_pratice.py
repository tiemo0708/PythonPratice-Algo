#같은 경로내에 있어야 모듈 사용 가능

# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_solder(5)

# import theater_module as mv #모듈의 이름 지정
# mv.price(3)
# mv.price_morning(4)
# mv.price_solder(5)


# from theater_module import * #모듈의 모든것을 스겠다
# price(3)
# price_morning(4)
# price_solder(5)

from theater_module import price, price_morning #쓸 함수만 가져오기
price(3)
price_morning(4)
# price_solder(5)

from theater_module import price_solder as price
price(5)
