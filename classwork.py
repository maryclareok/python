# f = open("newfile.txt", "x")
# f = open("newfile.txt", "w")
# count=0
# while count !=10:
#     new=input("enter text ")
#     f.write(new)
#     f.write("\n")
#     count +=1
# f.close()
# try:
#     open("classdoc.txt")
# except:
#     print("the file does not exist")
# try:
#     total = 0
#     for _ in range(10):
#         total += int(input("Enter a number: "))
#     print(total)
# except ValueError:
#     print("enter a number")

total = 0
for _ in range(10):
    total += int(input("Enter a number: "))
print(total)