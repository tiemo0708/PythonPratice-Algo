# try:
#     print("나누기 전용 계산기입니다")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print(err)

#의도적으로 에러 발생시키기

class BignumberError(Exception): #사용자 정의 에러처리
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self): #리턴할때 str
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번쨰 숫자를 입력하세요 : "))
    num2 = int(input("두 번쨰 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BignumberError("입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BignumberError as err: #리턴값 받아오기
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
    print(err)
finally: #무조건 끝날떄 실행/ 강제종료 맏
    print("계산기를 이용해 주서 감사합니다")    