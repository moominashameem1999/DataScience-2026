"""Write a Python program to:
1. Define a function that accepts an integer n.
2. For every positive integer i ≤ n, apply the following rules:
o Print "FizzBuzz" if i is divisible by both 3 and 5.
o Print "Fizz" if i is divisible by 3 (but not 5).
o Print "Buzz" if i is divisible by 5 (but not 3).
o Print the number itself (as a string) if none of the above conditions are true.
3. Call the function with user input as the argument."""

n = input("Enter a positive integer: ")
for i in range(0, int(n)+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))


