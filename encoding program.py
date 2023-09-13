# encoding program
msg="I love India"
pat="*** ***** *******"
newstr=""
i=0
for j in pat:    
    if (j=="*"):
       if (i<len(msg)):
            if msg[i] !=" ":
                newstr=newstr+msg[i]
            else :
                newstr=newstr+msg[i+1]
                i=i+1

            i=i+1
       else:

            i=0
            newstr=newstr+msg[i]
            i=i+1
    else:
        newstr=newstr+" "
print("new encoded string=",newstr)