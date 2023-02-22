import os
import platform
def shutdown():
    if platform.system()=="Windows":
        os.system("shutdown -s")
    else:
        print("os is not supported")

command=input("enter s for shutdown")
if command=="s":
    shutdown()
else:
    print("wrong input")
        