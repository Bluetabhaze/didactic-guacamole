import random

option=input("""Enter option for password (WRITE "help" for list):""")
if option == "help" :
    print("""
this program is used to save data 
a is equal to add a new password.
r is equal to read all the password
d is equal to delete all the PASSWOrds 
""") 

elif option == "a" :
    Question = input ("What is the Account Password for :")

    qoutput = (Question + " password is ")

    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length = 10
    pw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        pw = pw + alphabet[next_index]

    pw_file = open("/tmp/password.txt", "w")

    pw_file.write (qoutput + pw)

    pw_file.close()

    pw_file = open("/tmp/password.txt", "r")

    for line in pw_file:
        print(line, end="")
    pw_file.close

elif option == "r" :
    pw_file = open("/tmp/password.txt", "r")    
    for p in pw_file :
        print(p,end="")
    pw_file.close

elif option == "d" :
    print ("""this is not an option yet""")

else :
    print(""" invaild write a password input""")

