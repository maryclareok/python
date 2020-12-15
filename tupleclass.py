# tup1  = ('physics','chemsitry',1999,2000)
# tup2 = (1,2,3,4,5)
# print(tup1[0])
# print(tup2[1:5])
# tup3=()

# thistup=list(tup3)


# while True:
#     newlist=input("enter the strings for this tuple or yes to end>>> ")
#     if newlist.lower() == "yes":
#        break
#     else:
#         thistup.append(newlist) 
     
# tup3 = tuple(thistup)
# print(tup3)
# print(max(tup3),"\n",min(tup3))
# print(tup3[2:4])
tup4 = ()
thistup1=list(tup4)
while True:
    newlist1=int(input("enter the integers for this tuple or 0 to end>>> "))
    if newlist1 == 0:
        break
    else:
        thistup1.append(newlist1)
tup4 = tuple (thistup1)
print(tup4)
largest_value = max(tup4)
smallest_value = min(tup4)
print(largest_value,"\n",smallest_value)