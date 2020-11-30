f = open("newfile3.txt", "x")
f = open("newfile3.txt", "w")
count=1
while count !=0:
    new=input("enter text ")
    f.write(new)
    f.write("\n")
    count +=1
f.close()
