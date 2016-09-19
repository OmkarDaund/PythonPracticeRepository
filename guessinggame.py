import random



minValue=1
maxValue=100

randomNumber=random.randint(minValue,maxValue)

found= False

while not found:
    #print("Guess anumber between 1 to 100")
    userNumber=int(input("Guess anumber between 1 to 100:  "))
    if randomNumber==userNumber :
        print ("It's right")
        found=True
    if randomNumber>userNumber :
        print ("Go a bit high")       
    if randomNumber<userNumber :
        print ("Go a bit low")
                       
               
    
    



