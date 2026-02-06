import random

def random_with_N_digits(n):
    start_range=10**(n-1)
    end_range=(10**n)-1
    return random.randint(start_range,end_range)

def checkValid(cardNo:int):
    nDigits=len(cardNo)
    nSum=0
    isSecond=False

    for i in range(nDigits-1,-1,-1):
        d=ord(cardNo[i])-ord('0')

        if isSecond==True:
            d=d*2
        nSum+=d//10
        nSum+=d%10
        isSecond=not isSecond
    
    if(nSum%10==0):
        return True
    else:
        return False
    
if __name__=="__main__":

    found = 0
    while found < 1:
        cardNo = str(random_with_N_digits(16)) 
        
        if checkValid(cardNo):
            print(f"Found Valid Card: {cardNo}")
            found += 1
    if checkValid("5632016887467943"):
        print("Valid")
    else:
        print("Not Valid")

