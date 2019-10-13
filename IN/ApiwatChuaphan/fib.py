# Function for nth Fibonacci number


def Fibonacci(n):
    # a = 0
    # b = 1
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


# Driver Program
Fib_num = int(input("Enter a Fibonacci number: "))
for i in range(1, Fib_num+1):
    print(Fibonacci(i))

# This code is contributed by Saket Modi
