num = int(input("Enter number"))

def filter(num):
    even=[]
    odd=[]
    for i in range(num):
        if(i%2 ==0) and (i != 0):
            even.append(i)
        else:
            odd.append(i)

    print(f"Odd list is:{odd} and Even list is :{even}")
    

filter(num)