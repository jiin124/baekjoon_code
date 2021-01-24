a,b=input().split(" ")#문자열 받자마자 분리해서 a,b에 각각 저장하기
lista=list(a)#a에 저장한 문자 리스트로 바꾸기
listb=list(b)#b에 저장한 문자 리스트로 바꾸기
lista.reverse()
listb.reverse()#리스트 뒤집는 함수

newa="".join(lista)# 리스트 다시 합치기
newb="".join(listb)

if(newa>newb):
    print(newa)
elif(newa<newb):
    print(newb)