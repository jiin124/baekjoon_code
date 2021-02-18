import math

def p(num):
    if num==1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

prime=list(range(2,246912))
listp=[i for i in prime if p(i)]

while True:
    n=int(input())
    count=0
    if n==0:
        break
    for i in listp:
        if n<i<=n*2:
            count+=1
    print(count)