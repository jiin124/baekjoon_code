n=int(input())
arstr=""

for i in range(n):
    arstr=""
    num,string=input().split()


    for j in string:
        arstr+=j*int(num)
    print(arstr)
