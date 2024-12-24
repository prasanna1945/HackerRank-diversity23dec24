arr = [int(i) for i in input().split()]
m = arr[0]
n = arr[1]  
for i in range(n):
    for j in range(i+1):
        print(m,end = "")
    print("")
    m += 1
m -= 2
for i in range(n-1):
    for j in range(n,i+1,-1):
        print(m,end = "")
    print("")
    m -= 1