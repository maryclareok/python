# while i != len(user_info):
#     if user_info[i] == user_info[-2]:
#         password = input(f"enter {user_info[i]} : ")
#     elif user_info[i] == user_info[-1]:
#         password2 = input(f"enter {user_info[i]} : ")
#     else:
#         info=input(f"enter{user_info[i]} : ")
#         new_user_registration.update({user_info[i]:info})
#     i+=1
def breakloop (a):
    a = input("enter done")
    f.write(a)
    f.write("\n")
    if a == "done":
        break
       

 while True:
            content = input("Enter data for the file and done when your done typing: ")
            f.write(content)
            f.write("\n")
            # count+=1
            if content == "done":
                break