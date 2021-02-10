a=int(input())
b=int(input())
ar=[]

for i in range(a,b+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
            if(count>2):
                break
    if count==2:
        ar.append(i)


if len(ar)!=0:
    print(sum(ar))
    print(ar[0])
else:
    print(-1)



