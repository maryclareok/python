users={}
new_user_registration = {}
user_info = "name","username","password","confirm new password"

i=0
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
else:
    #this loop is will run ten times if the password is incorect, till the password is correct
    while t < 10:
        if password == password2:
            new_user_registration.update({"password":password}) 
        else:
            password =input("enter password: ")
            password2 = input("enter confirm new password: ")
            if  password == password2:
                new_user_registration.update({"password":password})
        t += 1
        if t >8 :
            print("you have one last chance")
            continue
print(new_user_registration)
#storing in a general dictionary
dicti = len(users)
dicti +=1
users.update({dicti:new_user_registration})
print (users)
# for i in users:
#     question = input("do you want to add more data \n yes or no")
#     if question == "yes":