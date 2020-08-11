#Exercise 4.3 count to 20 to print the numbers 1 to 20 inclusive
for numbers in range(1,21):
    print(numbers)

#exercise 4.4 make a list of numbers from one to one million
Digits=[]
for value in range(1, 100):
    digit= value
    Digits.append(digit)
print(Digits)

#exercise 4.5 Make a list of odd_numbers
odd_numbers=list(range(1,20,2))
print(odd_numbers)

#exercise 4.7 make a list of multiples of 3 from 3 to 30 and use a for loop to print he numbers on the alist
Multiples=[]
for value in range(3,30):
    value=(value%3==0)
    Multiple=value
    Multiples.append(Multiple)
print(Multiples)

#Exercise 4.8 cubes
Cubes=[]
for value in range(1,11):
    cube=value**3
    Cubes.append(cube)
print(Cubes)

#exercise 4.9 cube comprehension
Cubes=[value**3 for value in range(1,11)]
print(Cubes)
