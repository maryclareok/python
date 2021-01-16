import random
users={}
new_user_registration = {}
user_info = "name","username","password","confirm new password","customers credit","customers debit"
def question():
    print("1.buy goods")
    print("2.online chat")
def onlinechat():
    print("1. late delivery\n2. bad delivery\n3.inquires\n4.special compliant")
def onlinechat1(asking):
    if asking == 1:
        print( "your request has been recived,\nplease wait three working days for a response\nif no response is sent please visit us any of our nearest shopping malls\n or contact us at 08060349460")
    elif asking == 2:
        print("sorry for the bad delivery,\nyour goods will be replaced within three working days,\nplease be patient")
    elif asking ==3:
        print("you can contact us at maryclareokekek@gmail.com")
    elif asking ==4:
        complaint = input("enter your compliants \n >>> ")
        print(complaint)
        print("your special compliant has been sent ,\n please wait 3 to 4 working days for it to be resolved")       
def intros():
    print("type stop to stop buying")
    print (goods.keys())

    
goods={
"bread":400,
"chalk":100,
"meat":500,
"fanta":100,
"coke":100,
"malt":100,
"sprite":100,
"ice cream":500,
"cookie":200,
"snickers":100,
"skitiles":150
}

i = 0
while i < len(user_info):
    #accepts user_info details
    if user_info[i] == "customers credit":
        customerscredit = random.randint(0,500000)
        new_user_registration.update({"customers credit":customerscredit})
    elif user_info[i] == "customers debit":
        customersdebit = 0
        new_user_registration.update({ "customers debit":customersdebit})
    elif user_info[i] == "password":
        password = input(f"enter {user_info[i]} : ")
    elif user_info[i] == "confirm new password":
        password2 = input(f"enter {user_info[i]} : ")
    else:
        info=input(f"enter{user_info[i]} : ")
        new_user_registration.update({user_info[i]:info})
    i+=1
    t=0
    #will continue running till the password is correct
else:
    if password == password2:
        new_user_registration.update({"password":password}) 
    else:
        while t < 10:
            password =input("enter password: ")
            password2 = input("enter confirm new password: ")
            if  password == password2:
                new_user_registration.update({"password":password})
                break
        t += 1
print(new_user_registration)

f = 0
while f < 10 :
    prompt = input("enter username>>> ")
    password = input("enter your password>>> ")
    if new_user_registration["username"] == prompt and new_user_registration ["password"] == password:
        print("welcome to checkit online store \nplace your order.....")
        break
    else:
        continue
f += 1
question()
que=int(input("<<<"))
if que==1:
    p = 0
    while p < len(goods):
        intros()
        food = input("What do you want: ")       
        for good in goods:
            if good == food :
                print(f"It costs {goods.get(food)}NGN")
                ask = input("Buying?,yes/no ")
                if ask.lower() == "yes":
                    customersdebit = customersdebit + goods.get(food)
                    customerscredit =customerscredit-goods.get(food)
                    print(f"ping ping!! you have {customerscredit} left in your account.")
                    new_user_registration.update({food:goods.get(food)})           
                elif ask.lower() =="no":
                    continue
            elif food.lower() == "stop":
                print("YOU ARE DONE SHOPING!\nThank you for using checkit")
                print(new_user_registration)
                break
    p += 1

elif que==2:
    print("leah:what issues are you having")
    onlinechat()
    asking=int(input("<<<"))
    onlinechat1(asking)
else:
    print("error start again")

# print(new_user_registration)    
#storing in a general dictionary
dicti = len(users)
dicti +=1
users.update({dicti:new_user_registration})
print (users)
i+=1