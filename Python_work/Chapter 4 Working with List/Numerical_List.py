#the range function makes it easy to generate a list of numbers
for value in range(1,5):
    print (value)
#in this scenario you'll see a result of the off-by-one behaviour the otput never contains the end value in thi case 5

#if you want to list the numbers you can convert the result of range () directly into list()
numbers= list(range(0,9))
print (numbers)
#output [0, 1, 2, 3, 4, 5, 6, 7, 8]

#we can also use range function to print to skip numbers in a given arrange
even_numbers =list(range(2,11,2))
print(even_numbers)
#in this range function it starts with the value 2 and then adds 2 to the value , it adds 2 repeteadly until it reaches or passes the end value

##you can create alost any set of numbers you want to use the range value
squares=[]
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
#each value is immediately squared and appended to the list squares

#simple statistics with a list of numbers
digits=[1,2,3,4,5,6]
print (min(digits))
print (max(digits))
print (sum(digits))

#using  a list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
