# ind=0
# word="python programming"
# length =len(word)
# while ind < length:
#     print(word[ind])
#     ind+=1 
   
#  "x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
# x = "awesome"
# print("Python is " + x)  
#  
# word="happy"
# num=10
# print(word)
# print(num) 
#  name="don"
# print(f"hello {name}")#diffrent type of print
# print("hello",name) 

#  length=12
# breadth=24
# print(f"the area of a rectangle {length*breadth}")
# print(f"the perimeter of a rectangle {2*(length+breadth)}") 

#  num1=10
# num2=20

# value=num1>num2#comparing values
# print(value)
# num1=10
# num2=20

# value=num1<=num2#comparing values
# print(value) 
#  "num1=10
# num2=20

# value=num1>num2 or num1<num2#comparing values
# print(value) 
#  num1=10
# num2=20

# value=num1>num2 and num1<num2#comparing values
# print(value)
# num1=30
# num2=40
# if num1<num2:
#  print("yes")#conditional statement
#  print("hello")
# print("weldone") 
#  
# x = "awe"



# def demo(a, b):
#   print(a + b)

# demo(2, 3)
# print()

 
# x = "tired"
# print(type(x))  
#  
# x = list(("apple", "banana", "cherry"))

# #display x
# print(x)

# #display the data type of x
# print(type(x))  
#  
# x = ("apple", "banana", "cherry")

# #display x:
# print(x)

# #display the data type of x:
# print(type(x))  
#  
# x = range(36)

# #display x:
# print(x) 
#  
# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z)) 

#  x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c)) 
#  import random

# print(random.randrange(1, 10)) 
#  
# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0'
# print(x)
# print(y)
# print(z)
# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2") # w will be 4.2
# print(x)
# print(y)
# print(z)
# print(w)
# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3
# print(x)
# print(y)
# print(z) 
#  
# a = "Hello, World!"
# print(a[0]) 
 
# b = "Hello, World!"
# print(b[2:5])
# b = "Hello, World!"
# print(b[-5:-2]) 
# a = " Hello, World! "
# print(a)
# print(a.strip()) # returns "Hello, World!" without space

# a = "HELLO, World!"
# print(a.lower())#returns text in lower case 
#  a = "Hello, World!"
# print(a.upper())
# a = "Hhello, World!"
# print(a.replace("Hh", "J"))#used to replace letters in a sentence 
# #you put the first letter"H",*the second letter which will replace the first letter"J"" which gives Jello World
# print(a.replace("W", "J")) 
#  
# a = "Hello, World!"
# b ="beeeeee,who,you want to be"
# print(a.split(",")) # returns ['Hello', ' World!']
# print(b.split(","))
# print("pussy cat pussy cat\nwhere have you been")#"\n"is used to move a sentence to another line like an enter key

# print("my name is","python",end=",")
# print("monty python")
# print("my name is",end="")
# print("monty python")
# print("my name ","python",end="\n ")
# print("monty python")
# print("my name is","python",end=" ")
# print("monty python")
# print("my","name","is","monty","python",sep=".",end="\n")#sep to seperate with with any character
# print("my","name","is","monty","python",sep="-",end="\n")#sep to seperate with with any character
# print("my","name","is","monty","python",sep="+",end="\n")#sep to seperate with with any character
# print("my","name","is",sep="_",end="*")
# print("monty","python",sep="*",end="\n")
# print(0o1234)#"0o"is used to represent octal to decimal number conversion
# print(0x123)#for hexadecimal to decimal conversion
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)