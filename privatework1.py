# count=1
# count1=1
# while count&count1==1:
#     print("im stuck in a loop")

# max=-9999999999
# number=int(input("enter number or -1 to stop "))
# while number !=-1:
#     if number>max:
#         max=number
#     number=int(input("enter number or -1 to stop "))#why did they put another "numbetr"down  there
#     print("the largest number is: ",max)


# evens=0
# odd=0
# number=int(input("enter number or 0 to stop:  "))
# while number !=0:
#  if number %2 ==0:
#    odd+=1
#  else:
#    evens+=1
#  number=int(input("enter number or 0 to stop:  "))
#  print("even numbers: ",evens)
#  print("odd number: ",odd) 
# for i in range(10):
#     print("value of i is currently",i)
# for i in range(2,8):#why did it bring out onlu 2 and not 8 is it not a range
#     print("the value of i is currently",i)
# for i in range(2,8,3):#why did this bring out only 2,5
#    print("the value of i is currently",i)
# for i in range(1,1):
#     print("the value of i is currently",i)
# for i in range(2,1):
#     print("the value of i is currently",i)
# pow=1
# for exp in range (16):
#     print("2 to the power of",exp,"is",pow)
#     pow *= 2 #how exactly does this work

# max=-9999999999
# counter=0

# while True:
#     number=int(input("enter number or -1 to stop "))
#     if number==-1:
#         break
#     counter+=1
#     if number>max:
#         max=number
#     if counter:    
#         print("the largest number is: ",max)
#     else:
#         print("are you kidding? you havent entered any value")

# max=-9999999999
# counter=0
# number=int(input("enter number or -1 to stop "))
# while number !=-1:
#     if number ==-1:
#         continue
#     counter+=1 #whats the point of the counter here
#     if number>max:
#         max=number
#         number=int(input("enter number or -1 to stop "))
#     if counter:    
#         print("the largest number is: ",max)
#     else:
#         print("are you kidding? you havent entered any value")

# i=1
# while i<5:
#     print(i)
#     i+=1
# else:
#     print("else: ",i)

# i=5
# while i<5:
#     print(i)
#     i+=1
# else:
#     print("else: ",i)

# for i in range(5):
#     print(i)
# else:
#     print("else: ",i)

# i=111
# for i in range(2,1):
#     print(i)
# else:
#     print ("else: ",i)    


# # you may remember De Morgan’s laws from school. They say that:

# # The negation of a conjunction is the disjunction of the negations.

# # The negation of a disjunction is the conjunction of the negations.
# not(p and  q) = (not p) or (not q)
# not(p or q) = (not p) and  (not q)
# i=15
# j=22
# bit = i & j
# print(bit)

# i=22
# bitneg= ~i
# logneg= not i
# print(bitneg)
# print(logneg)
# x=15
# y=22
# x=x & y # its the same as  x&=y
# x=x | y# x|=y
# x= x ^ y# x^=y
# print(x)
# flagregister=0x1234
# print(flagregister)#used to convert decimal to hexadecimal (0x)
# x=flagregister & 1#used to show the value of flagregister in bits
# print(x)
# themask = 8
# if  flagregister & themask:
#     #the bit is set
# else:
#     #the bit is reset
# flagregister &= ~themask#flagregister- flagregister & ~themask
# print(flagregister) 
# flagregister = flagregister ^ themask#flagregister^=themask
# flagregister ^1=~flagregister
# var=17
# varright=var>>1#dividing by one bit that (17/2)
# varleft=var<<2#multiplying by two bit (17*4)
# print(var,varright,varleft)
#result=function(arg)#a function invocation
#result=data.method(arg)#a moethod invocation
# list=[2,3,4,8]
# list.insert(-1,5)
# print(list)
# list1=[]
# for i in range(5):
#     list1.append(i+1)
# print (list1)    

# list1=[]
# for i in range(5):
#     list1.insert(0,i+1)
# print (list1)   

# list10=[]
# for i in range(5):
#     list10.insert(-1,i+1)
# print (list10)   
# sum=0
# list10=[]
# for i in range(5):
#     list10.insert(-1,i+1)
# for i in range(len(list10)):
#     sum+=list10[i]
# print(sum)    

# list=[1,10,11,23,45,56]
# list[0],list[4]=list[4],list[0]
# list[1],list[3]=list[3],list[1]
# print(list)

# list=[1,10,11,23,45,56]
# l=len(list)
# for i in range(l//2):
#     list[1],list[1-i-1]=list[1-i-1],list[1]
# print(list)

# list1=[1]
# list2=list1
# list1[0]=2
# print(list2)
# list1=[1]
# list2=list1[:]
# list1[0]=2
# print(list2)
# list=[1,10,11,23,45,56]
# new_list=list[-1:1]
# print(new_list)
# list=[1,10,11,23,45,56]#it deletes only the content in the list
# del list[:]
# print(list)
# list=[1,10,11,23,45,56]#it deltes the entire list hence why the error
# del list
# print(list)
# list=[1,10,11,23,45,56]
# print(1 in list)
# print(100 not in list)
# print(2000 in list)
# list=[1,10,11,23,45,56]
# max=list[0]
# for i in range (1,len(list)):
#     if list[i]>max:
#         max=list[i]
# print (max)        
# list=[1,10,11,23,45,56]
# max=list[0]
# for i in list:
#     if i>max:
#         max=i
# print (max)    
# list=[1,10,11,23,45,56]
# max=list[0]
# for i in list[1:]:
#     if i>max:
#         max=i
# print (max)      

# list2 = [1,2,3,4,5,6,7,8,9]
# tofind = 1
# found = False
# for i in range(len(list2)):
#     found = list2[i] == tofind
#     if found:
#         break
#     if found:
#         print ("element found at index",i)
#     else:
#         print("absent")

# bets = [5,7,8,11,12]
# draws = [3,4,6,11,13]
# hits = 0
# for number in bets:
#     if number in draws:
#         hits += 1
# print(hits)        



# # User registration
# users = {}
# new_user = {}
# requested_data = ["first_name", "last_name", "nick_name","password", "comfirm_password"]

# for data in requested_data:
#     if data == "password":
#         passwd = input(f"Enter {data}: ")
#     elif data == "comfirm_password":
#         passwd2 = input(f"Enter {data}: ")
#     else:
#         info = input(f"Enter {data}: ") 
#         new_user.update({data:info})
# else:
#     if passwd == passwd2:
#         new_user.update({"password":passwd})

# print(new_user)

# # Storing value in bigger Dictionary

# key = len(users)
# key += 1
# users.update({key:new_user})
# print(users)

# chioma_money = 1_500#done it works
# listitems = {"beans":300, 
# "rice":500,
# "beef":750,
# "egg":200}
# print (listitems.keys())
# food = input("What do you want: ")
# for i in listitems:
#     if i == food :
#         print(f"It costs {listitems.get(food)}NGN")
#         ask = input("Buying? ")
#         if ask.lower() == "yes":
#             chioma_money = chioma_money - listitems.get(food)
#             print(f"ping ping!! you have {chioma_money} left in your account.")# code to enable user to select menu 
#             #option and see the price as well as amou#nt left in thier account
# def  message():
#     print("enter value")

# print("we start here")
# message()
# print("we end here")
# def message (no):
#     print("enter value",no)
# no = 1234
# message(no)
# print(no)

# def message (what,no):
#     print(f"enter {what} number  {no}")
# message("price" ,5)
# gem = int(input())
# message ("tax",gem)
def sum(a,b,c):
    print(f"{a},+{b},+{c} = {a+b+c}")
