from random import randint

min_number = int(input('Enter the minimum number: '))
max_number = int(input('Enter the maximum number: '))

if (min_number > max_number):
    print("The minimum number must be less than the maximum number.")
else:
   rn_number = randint(min_number, max_number)
   print("The random number is", rn_number)