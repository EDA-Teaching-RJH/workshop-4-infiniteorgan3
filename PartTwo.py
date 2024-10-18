# Coffee machine:

def validatingdrink():
    drinks = ["water", "soft drink", "coffee", "tea", "hot chocolate", "juice", "lemonade"]
    drinkchoice = ""
    while drinkchoice not in drinks:
        drinkchoice = input("What drink are you having?").lower().strip()
    return drinkchoice
    
def sugar():
    inp = ""
    inp = int(input("How many teaspoons of sugar would you like?"))
    return inp

def milk():
    validmilktypes = ["whole", "skimmed","lowfat","almond","coconut","soy", "oat","none"]
    milkteaspoons = 0
    milktype = ""
    while (milktype not in validmilktypes):
        milktype = input("What kind of milk would you like?").lower().strip()
    
    if milktype != "none":
        milkteaspoons = int(input("How many teaspoons of milk would you like?"))
    else:
        return 0
    
    match milktype:
        case "whole":
            return milkteaspoons * 5
        case "skimmed":
            return milkteaspoons * 5
        case "lowfat":
            return milkteaspoons * 10
        case "almond":
            return milkteaspoons * 15
        case "coconut":
            return milkteaspoons * 15
        case "soy":
            return milkteaspoons * 10
        case "oat":
            return milkteaspoons * 20
        

def validatingcoins():
    validcoins = [50,20,10,5]
    coin = 0
    while coin not in validcoins:
        coin = int(input("How much money are you putting into the coffee machine? This machine only accepts 50p, 20p, 10p and 5p coins."))
    
    return coin

totalcoins = 0

price = 0

match (validatingdrink()):
    case "water":
        price = 30
    case "soft drink":
        price = 55
    case "coffee":
       choiceofshot = ""
       while (choiceofshot != "y" and choiceofshot != "n"):
            choiceofshot = input("Would you like additional shots of coffee? y/n ").lower().strip()
       if choiceofshot == "y":
            numofshots = int(input("How many additional shots would you like?"))
            price = 75 + (numofshots * 20) + (sugar() * 5) + (milk())
       else:
            price = 75
    case "tea":
        price = 75 + (sugar() * 5) + (milk())
    case "hot chocolate":
        price = 90
    case "juice":
        price = 50
    case "lemonade":
        price = 65

print(f"The price is: {price}p.")
while totalcoins < price:
    totalcoins += validatingcoins()

print(f"The change you are owed is: {totalcoins - price} pence.")