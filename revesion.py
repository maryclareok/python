user_info = [
    {
        "name" : "ken",
        "surname" :"benny",
        "marital status" :"married",
        "age" : 37,
        "business" : True,
        "pets" : {
            "dogs":["caucasian" , "pitbull" , "pitbull" , "german sheperd"]
        },
       "kids" : ["annie" , "mary" , "jerry" , "tony"],
       "cars" : {
       "bmw" : {"model" : 2020 , "speed" : "10mpg"},
       "bently" : {"model" : 2020 , "speed" : "100mpg"},
       },
       "houses_location" : ["abuja" , "lagos" , "calabar"]
    },
]
name= user_info[0]["name"]
dog2=len(user_info[0]["pets"]["dogs"])
print(name,"has",dog2,"dogs",end= " ")
for listofdogs in user_info[0]["pets"].get("dogs"):
    print(listofdogs,end= " ")
    


name2 = user_info[0]["name"]
car2 = len(user_info[0]["cars"])
print("\n",name2,"has",car2,end= " ")
for listofcars in user_info[0]["cars"].keys():
    print(listofcars,end= " ")   