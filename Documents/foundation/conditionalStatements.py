name = input("Enter name:")
age = int(input("Enter age:"))

if(age==10):
    print(f"Hey {name} your ticket price is 100")
elif(age > 10):
    print(f"Hey {name} your ticket price is 150")
elif(age < 0):
    print(f"Hey {name} Please enter a valid age")
else:
    print(f"Hey {name} your ticket price is 50")