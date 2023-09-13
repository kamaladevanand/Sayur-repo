# square patteren
row=5
col=7
for i in range(row):
    print()
    for j in range(col):
        if i==0 or i==row-1:
            print("*",end=' ')
        else:
            if j==0 or j==col-1:
                print("*",end=' ')
            else:
                print(" ",end=' ')


