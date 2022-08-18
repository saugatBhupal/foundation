def sendName(firstName, lastName):
    return (firstName + " " + lastName)
firstName = input("Enter First Name:")
secondName = input("Enter Second Name:")
print("Your full name is: " + sendName(firstName,secondName))