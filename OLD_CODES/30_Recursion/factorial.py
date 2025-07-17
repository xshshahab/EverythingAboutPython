# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1

# factorial(0) = 1

def factorial(n):
    if(n==1 or n==0):
        return 1
    else :
        return n * factorial(n-1)
    

print("Hardcoded Value :",factorial(3))

num = int(input("Enter number to calculate factorial :"))
print("Calculated Value of factorial is :",factorial(num))