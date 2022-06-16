import time
import os 

os.system('color 71')
print("                                                  -------------")
print("                                                  -J.A.R.V.I.S-")
print("                                                  -------------")
 
name = input("Enter name: ")
print("Hello", name, "I am JARVIS, your personal asssistant")

print("Do you prefer Sir or Miss")
C = input()
print("Understood", C)

while 1:
    print("How can I help you", C)
    A = input().lower()
    if A == ("hello") or A == ("hi") or A == ("hey") or A == ("jarvis"):
        print("Hello", C)

    elif A == ("open google") or A == ("open google"):
        os.system('start chrome www.google.com')
        print("Opening chrome to google.com")

    elif A == ("exit"):
        print("Exiting in")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        os.system('TASKKILL /F /IM py.exe')
        break

    elif A == ("shutdown"):
        print("Are you sure", C)
        Y = input("yes/no").lower()
        if Y == ("yes"):
            os.system('shutdown /p')

        else:
            print("Canceling shutdown", C)

    else:
        print("I'm not sure I understand", C)
