import numpy as np

a = np.matrix([[0, 0, 0]])
b = np.matrix([[1, 1, 1]])
FibArray = [a, b]

def fibonacci(n):

    # Check is n is less than 0
    if n < 0:
        print("Incorrect input")
        
    # Check is n is less than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:        
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        print(FibArray)
        return FibArray[n]

print(fibonacci(10))