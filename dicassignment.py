prompt = input("enter username>>> ")

userlogin = {
  "mery":"Tecno12345" ,
  "mericlre": "tecno",
  "em_klare": "tecno1233",
  "marygraphy": "tecno12345",
}
for i in userlogin:
    if i == prompt :
        password = input("enter your password>>> ")
        if userlogin.get(prompt) == password:
            print("welcome")
            break 
else:
    print("VALUE ERROR")    
