num=int(input("enter a no"))
onum=num
i=0
q=num

while (q>3):
    q=num//3
    i+=1
    num=q
print("original num=",onum)
print("final number=",num)
print("no.of times div took place=",i)