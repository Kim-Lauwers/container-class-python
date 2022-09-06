# Write a program which iterates the integers from 1 to 50.
# If divisible by three print "Fizz" instead of the number
# If divisible by five print "Buzz".
# If divisible by both three and five print "FizzBuzz".

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
