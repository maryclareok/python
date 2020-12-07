def breakloop (a):
    f.write(a)
    f.write("\n")
    if a == "done":
        break
try:
    newfile = input("enter filename.txt ")
    f = open(newfile,"r")
    question1 = input("do you want to write into this file, enter yes or no>> \n")
    f.close()
    if question1 == "yes":
        f=open(newfile,"a")
        while True:
            breakloop(a)
            a = input("enter done")
        print("sucessful")                       
    elif question1 == "no":
        print("okay \n done")
except:
    print("file does not exist")
    question2=input("do you want to create a new file, yes/no>>\n")
    if question2=="yes":
        f = open(newfile, "a")
        question=input("do you want to write into the file yes/no>>\n")
        if question=="yes":
            while True:
                new=input("enter data for the file and Done when your done typing : ")
                f.write(new)
                f.write("\n")
                # count1 +=1
                if new=="done":
                    break
            print("sucessful")
                # f.close()
        elif question =="no":
            print("okay \n done")
    elif question2=="no":
        print("bye")
f.close()