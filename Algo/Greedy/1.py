#거스름돈 문제
n = 1260
count = 0

#큰 단위의 환폐 부터 확인
array = [500, 100, 50, 10]

for coin in array:
    count+= n//coin #n을 거스름돈으로 나눈 몫
    n%= coin #나머지

print(count)
