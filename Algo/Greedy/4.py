#모험가 길드문제
n= int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도 낮은것 부터 하나씩 확인
    count +=1 #현재 그룹에 해당 모험가 포함
    if count >=i: #현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이면 그룹핑
        result +=1
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화
print(result) #총 그룹의 수