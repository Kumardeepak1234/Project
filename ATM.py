pin=123
chance=3
while chance>0:
    userpin=int(input("welcome to SBI ATM, please enter ur pin"))
    if pin==userpin:
        print("Welcome, what opertion u want to perform")
        break
    else:
        print("wrong pin, please try again")

    chance-=1
