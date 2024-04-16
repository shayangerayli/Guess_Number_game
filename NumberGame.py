import random
while True:
    Question=input("You Want Continue?(Yes/No)")
    number = random.randrange(0,100)
    if(Question=="yes" or Question=="yes"):
        while True:
            try:
                ClientNumber=int(input("Please Enter Your Number : "))
                if ClientNumber==number:
                    print('Yes! Your number is ',number)
                    break
                elif ClientNumber<number:
                    print("computer Number Biggest Than")
                else :
                    print("computer Number Smaller Than")
            except:print("Please Input Number")
    else:
        break