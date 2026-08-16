n,x=input().split()
n=int(n)
x=int(x)
count=0
for i in range(1,n+1):
    while i>0:
        num=i
        if num%10==x:
            count+=1
        num//=10
print(count)