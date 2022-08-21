#1 ask a two integer number with user and function should return their addition

def add(num1,num2):
    sum = num1 + num2
    return(sum)

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
sum = add(num_1, num_2)
print(f"sum is {sum}")

# ask an information about your laptop and a function should return like this:
"""
Ex. Dell Vostro @ rs. 80000
"""

def retInformation(brand,model, price):
    print(f"{brand} {model} @ Rs. {price}")

BName = input("Enter brand name: ")
MName = input("Enter model name: ")
Price = int(input("Enter price: "))
retInformation(BName,MName,Price)


