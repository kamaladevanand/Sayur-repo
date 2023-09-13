# accept two string. if of unequal length add a to the smaller one till both equal
str1="Schooling"
str2="learningsssss"
if len(str1)==len(str2):
    print("both strings of equal length.. Bye Exiting program")
elif( len(str1)> len (str2)):
    i= len(str1)-len(str2)
    for j in range(i):
        str2=str2+'a'
else:
    i= len(str2)-len(str1)
    for j in range(i):
        str1=str1+'a'
print( "string 1=",str1 , "string 2=",str2)
