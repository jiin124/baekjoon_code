string=input().lower()
ar=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

time=0
for i in range(len(string)):
    for j in ar:
        if(string[i] in j):
            time+=ar.index(j)+3

print(time)

