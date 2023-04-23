class SoldOutError(Exception):
    pass
    # def __init__(self, msg):
    #     self.msg = msg
    # def __str__(self):
    #     return self.msg

chicken = 10
waiting = 1
while(True): 
    try:
        print("[남은 치킨: {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문?"))
       

        if order > chicken:
            print("재고가 부족합니다.")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료 되었습니다."\
                .format(waiting, order))
            waiting +=1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
        # print(err)