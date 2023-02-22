from secrets import choice
import webbrowser
import time
choice=input("Do u want me to open Intagram")
if choice=="yes":
    age=int(input("let us know ur age"))
    if age>=18:
        webbrowser.open("www.instagram.com")
        time.sleep(2)
    else:
        print("thode bade ho jaao")
        
else:
    print("Thank u")