#
winningNumber = 10
userProvidedNumber = int(input('Please provide your number:'))

if(userProvidedNumber > winningNumber):
    print('guess was high')
elif(userProvidedNumber < winningNumber):
    print('NUmber was low')
else:
    print('correct guess')
