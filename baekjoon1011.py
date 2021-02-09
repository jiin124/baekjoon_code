n=int(input())
count=0
hap=1

for i in range(n):
    x,y=map(int,input().split(" "))
    distance=y-x
    count=0
    hap=1
    while distance>0:
        distance-=hap
        count+=1
        if count%2==0:
            hap+=1
    print(count)

    
