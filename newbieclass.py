# length=10
# breadth=13
# print("the area of a rectangle is : ",length*breadth)
# print("the perimeter of the rectangle is: ",2*(length+breadth))
#CONDITIONAL STATEMENTS:
#sequential
#iteration
#reuse
#condition
#examples: if, ifelse, chained-conditions,nested if
# word = "example"
# for letter in word:
#     print (letter,end= "\n\n")
# names = ["jane","parker","harry","peter","paul"]
# for name in names:
#     if name == "harry":
#         print("found harry")
# names = ["jane","parker","harry","peter","paul"]
# for name in names:
#     if name.startswith("p"):
#         continue
#     else:
#         print(name)
balls = ["baseball","basketball","volleyball"]
colors = ["red","orange","white"]

for ball in balls:
    for color in colors:
        if(ball,color) ==("baseball","orange") or (ball,color) ==("baseball","red"):
            continue
        elif (ball,color) == ("basketball","red"):
            continue 
        else:
            print(color,"==>",ball)
