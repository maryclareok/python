
users={}
new_user_registration = {}
user_info = "name","username","password","confirm new password"

i = 0
while i < len(user_info):
    #accepts user_info details
    if user_info[i] == "password":
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
#storing in a general dictionary
dicti = len(users)
dicti +=1
users.update({dicti:new_user_registration})
print (users)
f = 0
while f < 10 :
    prompt = input("enter username>>> ")
    password = input("enter your password>>> ")
    if new_user_registration["username"] == prompt and new_user_registration ["password"] == password:
        print("welcome")
        break
    else:
        continue
f += 1
#the code above allows user to sign in after registering