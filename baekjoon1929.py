#시간 초과가 나는 것을 막기 위해 제곱근을 이용해 소수를 걸러내는 방법을 사용

import math

def p(n):
    if n==1:
        return False
    num=int(math.sqrt(n))
    for i in range(2,num+1):
        if n%i==0:
            return False
    return True

m,n=map(int,input().split(" "))
for i in range(m,n+1):
    if p(i):
        print(i)

    