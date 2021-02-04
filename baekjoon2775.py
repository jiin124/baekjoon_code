num=int(input())
ar=[]

for i in range(num):
    k=int(input())
    n=int(input())
    ar=[j for j in range(1,n+1)]
    for x in range(k):
        for y in range(1,n):
            ar[y]+=ar[y-1]
    print(ar[n-1])


        


    
