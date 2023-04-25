#곱하기 혹은 더하기

data= list(map(int,list(input())))
result = data[0];
for i in range(1, len(data)):
    num = data[i]
    if num <= 1 or result <= 1:
        result += num
    else:
        result*= num

print(result)

    