# n = 17
# k = 4
# count = 0

# while(n!=1):
#     if n%k == 0:
#         n//=k
#         count+=1
#     else:
#         n-=1
#         count+=1
# print(count)

#출력조건: 첫째줄에서 n이 1이될때까지 1벊ㅎㄱ운 2번의 과정을 수행하는 횟수의 최솟값
#입력 예시 25 5 출력예시 2

# N, K공백 기준으로 구분하여 입력
n, k = map(int, input().split())

result = 0

while True:
    #N이 K로 나누어 떨어지는 수가 될때까지 빼기
    traget=(n//k)*k
    result +=(n-traget)
    n = traget
    #n이 k보다 작을 떼 (더 이상 나눌 수 없을때) 반복문 탈툴
    if n < k:
        break;
    #k로 나누기
    result += 1
    n//=k
result += (n-1)
print(result)