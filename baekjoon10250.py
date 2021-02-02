n=int(input())

for i in range(n):
    h,w,n=map(int,input().split(" "))
    floor=n%h
    if floor==0:
        floor=h
        room=int(n/h)
    else:
        room=int(n/h)+1
    if room<10:
        room='0'+str(room)
    else:
        room=str(room)
    print(str(floor)+room)

