
snakecase = ""

camelcase = input("What is the name of your variable in camel case?")

for char in camelcase:
    if char.isupper():
        snakecase += ("_" + char.lower())
    else:
        snakecase += char

print(f"The snakecase version of {camelcase} is: {snakecase}.")