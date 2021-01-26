
n = int(input('Enter how many Fibonacci numbers you want: ')) # allows user to determine how many numbers in the sequence they want to be calculated

x = 0 # counter variable

fibonacci = [0, 1] # list to store numbers in sequence

num1 = 0 # first number to be added
num2 = 1 # second number to be added

while n <= 0:
    n = int(input('Enter a positive, real integer: '))

while len(fibonacci) < n:
    fibonacci.append(fibonacci[num1] + fibonacci[num2])
    num1 = num1 + 1
    num2 = num2 + 1
    x = x + 1

print(fibonacci)
    
    

