a,b,c=map(int,input().split())
i=1

while True:
    if(a+b*i<c*i):
        print(i)
        break
    i+=1