
room=1#방 개수
N=1 #2부터 7, 8부터 19까지의 수열 때문이다. 
sequence=6 # 수열이 6,12,24씩 늘어난다. 

n=int(input())# 수 입력

if(n==1): # 만약 1이라면 1출력하기 어느 방도 지나지 않았기 때문
    print("1")

else:
    while True:
        N+=sequence
        room+=1
        if(N>=n):
            print(room)
            break
        sequence+=6# 6,12,18,, 씩 늘어나는 수열 때문


    