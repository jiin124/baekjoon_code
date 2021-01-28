from collections import Counter
cnt=0
n=input().upper()

count=list(Counter(n).values())

for i in count:
    if max(count)==i:
        cnt+=1

if cnt>1:
    print("?")
else:
    max_index=count.index(max(count))
    print(list(Counter(n).keys())[max_index])