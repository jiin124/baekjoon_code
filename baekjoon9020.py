import math

count=0
def p(n):
    prime=[True]*n
    for i in range(2,int(math.sqrt(n))+1):
        if prime[i]==True:
            for j in range(i+i,n,i):
                prime[j]=False
    return [i for i in range(2,n) if prime[i]==True]



n=int(input())
for i in range(n):
    num=int(input())
    prime=p(num)
    l=p(num//2+1)
    for j in range(len(l)-1,-1,-1):
        if (num-l[j]) in prime:
            print("%d %d"%(l[j],num-l[j]))
            break


