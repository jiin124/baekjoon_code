a,b,c=map(int,input().split())#숫자로 연속해서 
i=1

while True:
    if(a+b*i<c*i):
        print(i)
        break
    i+=1
