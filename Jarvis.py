import time
import os 
from plyer import notification
from AppOpener import run 
from bs4 import BeautifulSoup
import requests

os.system("color 0c")
print('''
                            ___      __        _______  ___      ___  __      ________      
                           |"  |    /""\      /"      \|"  \    /"  ||" \    /"       ) 
                           ||  |   /    \    |:        |\   \  //  / ||  |  (:   \___/  
                           |:  |  /' /\  \   |_____/   ) \\  \/. ./  |:  |   \___  \    
                        ___|  /  //  __'  \   //      /   \.    //   |.  |    __/  \\   
                       /  :|_/ )/   /  \\  \ |:  __   \    \\   /    /\  |\  /" \   :)  
                      (_______/(___/    \___)|__|  \___)    \__/    (__\_|_)(_______/   
                                                                                          
''')
 
name = input("Enter name: ")
print("Hello", name, "I am JARVIS, your personal asssistant")
IconPath = r"C:\Users\vipul\OneDrive\Desktop\Courses\Course\JARVIS 2.0\Python-JARVIS\Jarvis_logo_ico.ico"
notification_title = 'JARVIS ACTIVATED!'  
notification_message = (f'Hello {name} JARVIS is ready to be your assistant 🤖:) ')
  
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = IconPath,  
    timeout = 1,  
    toast = False  
    )

print("Do you prefer Sir or Miss")
C = input()
print("Understood", C)
IconPath = r"C:\Users\vipul\OneDrive\Desktop\Courses\Course\Python-JARVIS\Jarvis_logo_ico.ico"
notification_title = 'HELLO'  
notification_message = (f'Hello {C}')
  
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = IconPath,  
    timeout = 1,  
    toast = False  
    )

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
        Y = input("yes/no\n>>").lower()
        if Y == ("yes"):
            os.system('shutdown /p')

        else:
            print("Canceling shutdown", C)
            
    elif A ==("restart"):
        print("Are you sure",C)
        Y = input("yes/no\n>>").lower()
        if Y ==("yes"):
            os.system('shutdown /r')
        else:
            print("Cancelling Restart",C)
            
    elif "add" or "subtract" or "multiply" or "divide" or "modulus" or "exponentiation" or "floor division" in A:
        print("Do you want me to perform  arthimatic operations ?")
        Y = input("yes/no\n>>").lower()
        if Y == ("yes"):
            print("Select the Operation to perform : \n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Modulus\n6) Exponential\n7) Floor Division\n>>")
            Y = input().lower()
            if Y ==("1"):
                A = int(input("Enter first number : "))
                B = int(input("Enter second number : "))
                print("The sum of two numbers are : ",A+B)
            elif Y ==("2"):
                A = int(input("Enter first number : "))
                B = int(input("Enter second number : "))
                print("The subtraction of two numbers are : ",A-B)
            elif Y ==("3"):
                A = int(input("Enter first number : "))
                B = int(input("Enter second number : "))
                print("The multiplication of two numbers are : ",A*B)
            elif Y ==("4"):
                A = int(input("Enter first number : "))
                B = int(input("Enter second number : "))
                print("The division of two numbers are : ",A/B)
            elif Y ==("5"):
                A = int(input("Enter first number : "))
                B = int(input("Enter second number : "))
                print("The modulus of two numbers are : ",A%B)
            elif Y ==("6"):
                A = int(input("Enter first number : "))
                B = int(input("Enter second number : "))
                print("The exponential of two numbers are : ",A**B)
            elif Y ==("7"):
                A = int(input("Enter first number : "))
                B = int(input("Enter second number : "))
                print("The floor division of two numbers are : ",A//B)
            else:
                print("Invalid number")
                      
        elif "open" or "application" in A:
            print("Do you want me to open application ?")
            Y = input("yes/no\n>>").lower()
            if Y == ("yes"):
                Y = input("ENTER APPLICATION TO OPEN: ").strip()
            if input:
                run(Y)
            else:
                print("Please check the application name you have typed")
                
                
        elif "weather" in A:
            headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


            def weather(city):
             city = city.replace(" ", "+")
             res = requests.get(
              f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
             print("Searching...\n")
             soup = BeautifulSoup(res.text, 'html.parser')
             location = soup.select('#wob_loc')[0].getText().strip()
             time = soup.select('#wob_dts')[0].getText().strip()
             info = soup.select('#wob_dc')[0].getText().strip()
             weather = soup.select('#wob_tm')[0].getText().strip()
             print(location)
             print(time)
             print(info)
             print(weather+"°C")


            city = input("Enter the Name of City -> ")
            city = city+" weather"
            weather(city)
            print("Have a Nice Day:)")
            
    else:
        print("I'm not sure I understand", C)
