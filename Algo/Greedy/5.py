#상하좌우 문제

n= int(input())
data = list(map(str, input().split()))
#arr=[[ 0 for j in range(n)] for i in range(n)]

#오, 위, 왼, 아
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

#현재위치
x, y = 0,0

for i in range(len(data)):
    if(data[i] == "R" and y != n-1):
        x = x+dx[0]
        y = y+dy[0]
    elif(data[i] == "U" and x !=0):
        x = x+dx[1]
        y = y+dy[1]
    elif(data[i] == "L" and y !=0):
        x = x+dx[2]
        y = y+dy[2]
    elif(data[i] == "D" and x !=n-1):
        x = x+dx[3]
        y = y+dy[3]
    else: continue

print(x+1,y+1)
# print('{}   {}'.format(x+1, y+1))
# print('%d    %d'%(x+1,y+1))