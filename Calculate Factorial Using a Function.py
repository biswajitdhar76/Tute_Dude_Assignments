
def factorial(n):
    result= 1
    for i in range(1, n + 1):
        result *= i    # result = result * i
    print(f"The factorial of {n} is: {result}")

factorial(n=int(input("Enter a number to calculate its factorial: "))) 
 