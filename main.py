#WRITE YOUR CODE IN THIS FILE
def factorial(x):
    total = 1

    for i in range(1, x + 1):
        total = total * i
        
    return total


print(factorial(5))
    
