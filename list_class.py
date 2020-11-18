# lst=[1,2,3,4,5]
# list=["jane","kemi","obi","mose"]
# print(len(lst))
# print(lst [0 : 3])
# print(list)
# num=lst[0]*lst[1]#using list for mathematical operation
# print(num)
# print(list[1:])
# print(list[1::2])
# print(lst[-1])
# print(lst[:-1])
# list3=["david","john",2,"ben",7,9,"germany"]
# print(list3[1])
# #changing values
# list3[1]= "wed"
# print(list3)
# #changing values of a specific index
# list3.insert(0,10)
# print(list3)
# #removing element
# list3.remove("wed")
# print(list3)
# list3.pop()
# print(list3) #deletes the last element the list
# del list3[2] #deletes the specified index
# print (list3)
# list3.clear()
# print(list3)#clears all the list content
# del list3
# print(list3)#deletes the list
# number=["jenny","bunny","55"]
# list2=[9,8,6,1,2,3,4,5]
# lst3=["m","y","z","b"]
# print(lst3)
# number.append("56")#adds to the list
# print (number)
# print(type(number))
# list2.extend(number)
# print(list2)#adds number to list2
# lst3=number.copy()
# print (lst3)#copys numbeer into lst3 and replaces it completly
# lst3.sort()
# print(lst3)#arranges the list
# lst10=["ben","jen","9","3"]#put numbers in double quote for integer and string combination
# lst10.sort()
# print(lst10)
# list5=["jamie",3,"davie",8,0]
# list5.pop(0)#used to remove a specific index
# list5.pop()
# print(list5)
# list6=[0,9,8,7,6,5]
# list6.sort()
# print(list6[-1])#to show the largest number in the list
# lst7=[3,6,9]
# newlist=[]
# mul=lst7[0]*lst7[1]*lst7[2]
# newlist.append(mul)
# print(newlist)#multiiplys the list
# list9=[1,4,0,7]
# list9.sort()
# print (list9[0])#returns the smallest number in the list
# list11=[1,3,5,7,9]
# print ("The list is : " + str(list11))
# counter = 0
# for i in list11:
#     counter=counter+1
# if counter == ind:
#     print ("Length of list without using len is : " + str(counter))

#CORRECTION
#1 a function to delete the first and last element in the list
# lst=["chucks","ada","henry","benita"]
# def remv(param):
#     param.pop(0)
#     param.pop()
#     return param

# remv(lst)
# print(lst)

 #2 a function to print the largest value in the list
list6=[0,9,8,7,6,5]
def large(param: list):
    largest=0
    for x in list6:
        if x > largest:
            largest = x
    return largest   


a = large(list6)
print(a)     

#3 a function to print smallest value in the list
list6=[0,9,8,7,6,5]
def small(param: list):
    smallest=sum(list6)
    for x in list6:
        if x < smallest:
            smallest = x       
    return smallest  


b= small(list6)
print(b) 





