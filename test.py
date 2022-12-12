from collections import Counter
N,M = input().split()
max = -1
arr=[]
for a in range(int(M)):
    arr += list(map(int, input().split()))
  
counter = Counter(arr).most_common()

for x, y in counter:    
    if int(y)> max:
        max = y
       

for x, y in counter:    
    if max == int(y):
        print(x,end=" ")

