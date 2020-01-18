import sys
from random import randrange

def check_arg(option):
    if('-v' in option):
        print("verions 1.0.0")
    elif(option in ['-?','-h']):
        print("How may I help you?")
    elif(option in ['-p']):
        print(randrange(1024,65000))
    elif(option in ['-i']):
        try:
            arg2 = sys.argv[2]
            if arg2[:3] == 'eth':
                if 0 <= int(arg2[3:]) <= 10:
                    print(arg2)
                else:
                    print("Invalid interface")
            else:
                print("Invalid interface name")
        except:
            print("Single argument missing")
    elif(option in ['-debug']):
        try:
            arg2 = sys.argv[2]
            if(arg2.lower() == "yes"):
                print("debug enabled")
            elif(arg2.lower() == "no"):
                print("debug disabled")
            else:
                print("Invalid argument")
        except:
            print("Single argument missing")
    else:
        print("Invalid option")
try:
    option = sys.argv[1]
    check_arg(option)
except:
    print("Provide option.")
