
n=int(input())
seq=1
count=0

while True:
    count+=seq
    if count>=n:
        break
    seq+=1

if seq%2==0:
    up=seq-(count-n)
    down=1+(count-n)
else:
    up=1+(count-n)
    down=seq-(count-n)


print("{}/{}".format(up,down))
