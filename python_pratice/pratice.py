# a =4

# print("나는"+str(a)+"살 이에요") #str 문자형 변경
# print("나는",a,"살 이에요")

# print(abs(-5)) #절댓값
# print(pow(4,3)) #4의 3승
# print(max(5,12)) #최댓값
# print(min(5, 12)) #최솟값
# print(round(3.14)) #반올림


# math 라이브러 사용

# from math import *
# print(floor(4.99)) #내림
# print(ceil(4.99)) #올림
# print(sqrt(16)) #제곱근

# 랜덤함수

# from random import *

# print(random()) #0.0~1.0 미만의 임의 값 생성
# print(random()*10)
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10)) #0~10 미만
# print(int(random()*10)+1) #1~10이하
# print(int(random()*45)+1) #1~45이하

# print(randrange(1,46)) #1~46미만
# print(randrange(1,46)) #1~46미만
# print(randrange(1,46)) #1~46미만
# print(randrange(1,46)) #1~46미만
# print(randrange(1,46)) #1~46미만

# print(randint(1, 45)) #1~45이하

# a=randint(4, 28)
# print("매월 스터디날짜는 %d 일로 선정 되었습니다"%a)

#  슬라이싱
# jumin= "000708-1234567"
# print("성별: %s" %jumin[7])
# print("연: %s" %jumin[0:2]) #0부터 2번째 직전까지(0,1)
# print("월: %s" %jumin[2:4])
# print("일: %s" %jumin[4:6])
# print("생년월일: %s" %jumin[:6]) #처음부터 6 직전까지
# print("뒤 7자리: %s" %jumin[7:]) #뒤 7가지, 7부터 끝까지
# print("뒤 7자리(뒤에서부터): %s" %jumin[-7:]) #뒤에서 7번째부터 끝까지

# 4-2문자열처리함수
# python = "Python is Amazing"
# print(python.lower()) #소문자
# print(python.upper()) #대문자
# print(python[0].isupper()) #해당위치 대문자인가?
# print(len(python)) #길이
# print(python.replace("Python","Java")) #바꾸고싶은 문자, 바꿀문자

# index = python.index("n") #n이 몇번째 위치에 있는지, 없으면 오류
# print(index)
# index = python.index("n",index+1) #두번째 위치에 있는 n
# print(index)

# print(python.find("n")) #n을 찾고 없으면 -1;
# print(python.count("n")) #n이 몇번 있는지

# 4-4 문자열 포맷
# 방법 1
# print("나는 %d살입니다." %20) # 정수형 %d
# print("나는 %s을 좋아해요." %"파이썬") # 문자열 %s
# print("Apple은 %c로 시작해요" % "A") # Char형 %c

# print("나는 %s살입니다." %20) # %s는 모든 형태 가능
# print("나는 %s색과 %s색을 좋아해요."%("파란","빨간"))

# #방법 2
# print("나는 {}살 입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# #방법3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age =20, color="빨간"))

# #방법4
# age=20;
# color="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요") #실제 변수에서 사용된값 사용

# 4-5탈출문자
# print("백문이 불여일견 \n백견이 불여일타") #\n 줄바꿈

# #"저는 "박진현"입니다.
# print("저는 \"박진현\"입니다.") #표출문자
# print("저는 \'박진현\'입니다.") #표출문자

# #\\: 문장 내에서 \
# print("aa\\ss\\dd")

# # \r: 커서를 맨 앞으로 이동
# print("Red Apple\rPine") #PineApple

# #\b  : 백스페이스
# print("Redd\bApple")

# # \t: 탭
# print("Red\tApple")


# pas = "http://naver.com"
# pas=pas.strip("http://")
# pas= pas[:pas.index(".")]
# print(pas[0:3]+str(len(pas))+str(pas.count("e"))+"!")

# url="http://naver.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# print("{0}의 비밀번호는 {1}입니다.".format(url,password))

# 리스트 []

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석","조세호","박명수"]
# print(subway.index("조세호")) #찾기

# #배열의 맨뒤에 추가
# subway.append("하하")
# print(subway)

# #배열의 사이에 추가
# subway.insert(1,"정형돈")
# print(subway)

# #배열의 제일 뒤에서 삭제
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# #같은 이름이 몇명있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))


# num_list = [5, 2, 4, 3, 1]
# #뒤집기
# num_list.reverse()
# print(num_list)

# #정렬 오름차순
# num_list.sort()
# print(num_list)

# #정렬 내림차순
# num_list.sort(reverse=True)
# print(num_list)


# #전체 삭제
# num_list.clear()
# print(num_list)

# #다양한 자료형 함께 사용

# num_list = [5, 2, 4, 3, 1]
# mix_list = ["조세호", 20, True,[10, "안녕", 30]]
# print(mix_list)

# #리스트확장
# num_list.extend(mix_list)
# print(num_list)

#사전 (key, value)
# cabinet = {3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
# # print(cabinet[5]) #없는 값 가져오면 오류
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능")) #값이 없으면 뒤의 문자 출력
# print(cabinet.get(3,"사용 가능"))

# print(3 in cabinet) #true
# print(5 in cabinet) #false

# cabinet = {"A-3":"유재석","B-3":"김태호"}
# print(cabinet["A-3"])

# #추가
# print(cabinet)
# cabinet["C-20"] = "조세호"
# cabinet["A-3"] = "김종국" #덮어쓰기
# print(cabinet)

# #제거
# del cabinet["A-3"]
# print(cabinet)

# #key 만 출력
# print(cabinet.keys())

# #value 들만 출력
# print(cabinet.values())

# #key, value 쌍으로 출력
# print(cabinet.items())

# #전체 삭제
# cabinet.clear()
# print(cabinet)

# 튜플(변경되지 않는 목록/list보다 빠름)
# menu = ("돈까스", "치즈까스")

# print(menu[0]) # 돈까스

# print(menu[1]) # 치즈까스


# name = "김종국"

# age = 20

# hobby = "코딩"

# print(name, age, hobby) # 김종국 20 코딩

# (name, age, hobby) = ("김종국", 20, "코딩")

# print(name, age, hobby) # 김종국 20 코딩


# #집합(set)

# my_set = {1, 2, 3, 3, 3} # 중복을 허용하지 않으므로 3은 1번만 들어감

# print(my_set) # {1, 2, 3}


# java = {"유재석", "김태호", "양세형"} # 자바 개발자 집합

# python = set(["유재석", "박명수"]) # 파이썬 개발자 집합


# # 교집합 (java 와 python 을 모두 할 수 있는 개발자)

# print(java & python) # {'유재석'}

# print(java.intersection(python)) # {'유재석'}


# # 합집합 (java 또는 python 을 할 수 있는 개발자)

# print(java | python) # {'박명수', '유재석', '김태호', '양세형'}

# print(java.union(python)) # {'박명수', '유재석', '김태호', '양세형'}


# # 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)

# print(java - python) # {'양세형', '김태호'}

# print(java.difference(python)) # {'양세형', '김태호'}


# # python 개발자 추가 (기존 개발자 : 박명수, 유재석)

# python.add("김태호")

# print(python) # {'박명수', '유재석', '김태호'}


# # java 개발자 삭제 (기존 개발자 : 유재석, 김태호, 양세형)

# java.remove("김태호")

# print(java) # {'유재석', '양세형'}


# 자료구조의 변형

# menu ={"커피","우유","쥬스"}

# print(menu)

# print(menu, type(menu)) #set 구조


# menu = list(menu)

# print(menu, type(menu))


# menu = tuple(menu)

# print(menu, type(menu))


# menu = set(menu)

# print(menu, type(menu))

# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) #랜덤
# print(lst)
# print(sample(lst, 1)) #랜덤 하나

# from random import *
# # lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# lst = range(1,21) #1부터 20까지 숫자를 생성
# lst = list(lst)
# chicken=sample(lst, 1)
# lst.remove(*chicken)
# coffee=sample(lst, 3)
# print(*chicken)
# print(coffee)

# if(분기)


# if 조건:
#     실행 명령문

# weather = "비"
# weather = "맑음"
# weather="미세먼지"

# weather=input("오늘날씨는 어때요? \n") #사용자의 입력을 받음
# if weather == "비" or weather=="눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요없어요")


# temp = int(input("기온은 어때요? \n")) #input 기본은 문자열

# if 30<= temp:
#     print("너무 더워요 나가지마세요")
# elif 10<= temp and temp<30:
#     print("괜찮은 날씨에요")
# elif 0<= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지마세요")

# 반복문
# for문
#   for Warning_no in [0, 1, 2, 3, 4]:
#     print("대기번호: {0}".format(Warning_no))
#     print("대기번호: %d" %Warning_no)

# #순차적으로 커질때 range
# for Warning_no in range(1,6): #1, 2, 3, 4, 5
#     print("대기번호: %d" %Warning_no)

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]

# for customer in starbucks:
#     print("%s, 커피가 준비되었습니다"%customer)

# while문
# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")


# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# continue와 break

# absent = [2, 5]
# no_book = [7] #책이없음
# for student in range(1, 11):
#     if student in absent:
#         continue #다음 반복으로 넘어감
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break #반복문 종료
#     print("{0}, 책을 읽어봐".format(student))


# 한줄 for

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# #학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students =[len(i) for i in students]
# print(students)

# #학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students =[i.upper() for i in students]
# print(students)

# 함수

# def open_account():
#     print("안녕")

# open_account()

# def deposit(balance, money): #입금
#     print("입급완료. 잔액은 {0}".format(balance+money))
#     return balance+money

# def withdraw(balance, money): #출금
#     if balance >= money:
#         print("출금완료. 잔액은 {0}".format(balance-money))
#         return balance-money

#     else:
#         print("출금실패. 잔액은 {0}".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금
#     commisson = 100 # 수수료 100원
#     return commisson, balance - money - commisson #여러개 값 가능

# balance = 0
# balance =deposit(balance, 1000)
# balance = withdraw(balance, 1500)

# commisson, balance =withdraw_night(balance, 500)
# print("수수료 {0}원이며 잔액은 {1}원 입니다.".format(commisson,balance))

# 기본 값
# \ 줄바꿈
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "자바")
# profile("김태호", 25, "파이썬")

# 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 키워드 값
# def profile(name, age, main_lang):
#         print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile( main_lang="자바", age=21, name="김태호")

# 가변 인자
# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end = " ") #end = " " 줄바꿈X
#     print(lang1, lang2, lang3, lang4, lang5)

# 가변 인자 사용 (서로 다른 개수의 값을 넣어줄때)
# def profile(name, age, *language):
#    print("이름: {0}\t나이: {1}\t".format(name, age), end = " ") #end = " " 줄바꿈X
#    for lang in language:
#     print(lang, end=" ")
#    print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 20, "Kotlin", "Swift")

# 지역 변수와 전역 변수
# gun = 10 #전역 변수

# def checkfoint(soldiers): #경계근무
#     # gun = 20 #지역변수
#     global gun #전역공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("함수 내 남은총: {0}".format(gun))

# def checkfoint_ret(gun, soldiers):
#     gun = gun - soldiers #지역 변수
#     print("함수 내 남은총: {0}".format(gun))
#     return gun

# print("전체 총: {}".format(gun))
# # checkfoint(2)
# gun = checkfoint_ret(gun,2) #리턴 값 받아 전역변수 변경
# print("남은 총: {}".format(gun))

# 표준 입출력
# print("Python", "Java", sep=" vs ", end ="?") #sep 중간에 뭐를 넣을지 정함
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python","Java", file = sys.stdout) #표준 출력으로
# print("Python","Java", file = sys.stderr) #표준 에러로

# 출력포맷
# scores = {"수학":0, "영어":50,"코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #왼족으로 정렬(8칸), #오른족정령 (4칸)


# 001, 002, 003 ...
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3)) #공간 3개확보 빈공간 0으로 채움

# 표준 입력

# answer = input("아무 값이나 입력하세요: ") #항상 문자열 형태로 입력
# print("입력하신값은 "+answer+" 입니다.")

# 다양한 출력 포멧
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# #양수일대 +로 표시, 음수일대는 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# #왼쪽 정렬하고, 빈칸으로 _채움
# print("{0:_<+10}".format(500))

# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# # 3자리 마다 콤마를 찍어주기, +,- 부호도 붙이기
# print("{0:+,}".format(10000000000))
# print("{0:-,}".format(10000000000))

# # 3자리 마다 콤마를 찍어주기, +,- 부호도 붙이기, 자릿수 확보 빈자리 ^로 채우기
# print("{0:^<+30,}".format(1000000000000))

# #소수점 출력
# print("{0:f}".format(5/3))
# #소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# 파일 입출력

# 파일에 쓰기
# score_file = open("score.txt","w", encoding="utf8") #w 쓰기위한 파일
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close() #파일을 열어주었으면 닫아주어야 함

# score_file = open("score.txt","a", encoding="utf8") #이미 있는 파일에 이어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 읽어오기
# score_file = open("score.txt", "r", encoding="utf8") #읽기
# print(score_file.read()) #전체 파일 읽어오기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline())
# score_file.close()

# 몇줄인지 모를때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# list에 값 다넣어서 처리
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end ="")
# score_file.close()


# pickle(프로그램 상에서 사용하는 데이터를 파일 형태로 저장)

# import pickle
# # profile_file = open("profile.pickle", "wb") #pickle쓰기 위해 b(바이너리타입 정의)
# # profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) #profile 에 있는 정보를 file에 저장
# # profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #파일에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with
# import pickle

# # with 사용시 close 필요없이 자동으로 종료
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


# pickle 없이 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# #읽어 오기
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# for i in range(1,11):
#     with open("%s주차.txt"%i , "w", encoding="utf8") as report_file:
#         report_file.write("- {0}주차 주간보고 -".format(i))
#         report_file.write("\n부서: ")
#         report_file.write("\n이름: ")
#         report_file.write("\n업무 요약: ")

# 9-1 클래스
# 마린 : 공격 유닛, 군인. 총을 솔 수 있음
# name = "마린" #유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 #유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp, damage))

# #탱크: 공격 유닛, 탱크. 포를 슬 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력{1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력{1}\n".format(tank2_hp, tank2_damage))

# def attack(name, loacation, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#         name, loacation, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# class Unit:
#     def __init__(self, name, hp, damage): #__init__ 생성자
#         self.name = name #멤버변수
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format( self.name))
#         print("체력 {0}, 공격력 {1}\n".format(self.hp,  self.damage))

# # marine1 = Unit("마린",40,5) #instance
# # marine2 = Unit("마린",40,5)
# # tank= Unit("탱크",150,35)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# #마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True #추가로 변수 할당가능

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))


# 메소드

from random import *

# 일반 유닛


class Unit:
    def __init__(self, name, hp, speed):  # __init__ 생성자
        self.name = name  # 멤버변수
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 공격유닛
class AttackUnit(Unit):  # (상속받을 클래스)
    def __init__(self, name, hp, speed, damage):  # __init__ 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, loacation):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
              .format(self.name, loacation, self.damage))


# 날 수 있는 기능을 가진 클래스
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스


class FlyableAttackUnit(AttackUnit, flyable):  # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        flyable.__init__(self, flying_speed)

    # 오버라이딩 파생 클래스에서 기반 클래스의 메서드를 새로 정의
    def move(self, location):  # move 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0}: 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동불가
    seize_development = False  # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_development == False:
            return

        # 현재 시즈모드가 아닐때 -> 시즈모드
        if self.seize_mode == False:
            print("{0}: 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드 일때 -> 시즈모드 해제
        else:
            print("{0}: 시즈모드로 전환합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 레이스


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloked = False  # 클로킹모드 (해제상태)

    def clocking(self):
        if self.cloked == True:
            print("{0} :클로킹 모드 해제합니다.".format(self.name))
            self.cloked = False
        else:
            print("{0} :클로킹 모드 설정합니다.".format(self.name))
            self.cloked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행


# 게임 시작
game_start()


# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_development = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다")


# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))  # 공격 랜덤으로 받음 (5~20)

# 게임종료
game_over()


# #건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # pass #아무것도 안하고 일단 넘어감
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, speed)#(). self 없이
#         self.location = location


# 서플라이 디폿: 건물, 1개 건물 = 8 유닛

# supply_depot = BuildingUnit("서폴라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")
# #발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")
# # #메딕 : 의무병


# 파이어뱃: 공격유닛, 화영방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)
