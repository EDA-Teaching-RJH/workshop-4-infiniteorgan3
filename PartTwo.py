# Coffee machine:

def validatingdrink():
    drinks = ["water", "soft drink", "coffee", "tea", "hot chocolate", "juice", "lemonade"]
    drinkchoice = ""
    while drinkchoice not in drinks:
        drinkchoice = input("What drink are you having?").lower().strip()
    return drinkchoice
    

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
            choiceofshot = input("Would you like an additional shot of coffee? y/n ").lower().strip()
       if choiceofshot == "y":
            price = 95
       else:
            price = 75
    case "tea":
        price = 75
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