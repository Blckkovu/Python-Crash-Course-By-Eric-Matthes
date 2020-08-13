#sorting a list permanently with sort()method
cars = ['Bmw', 'Audi','Toyota', 'Subaru']
cars.sort()
print(cars)
#The cars have permanently been arranged in alphabetical order
#output ['Audi', 'Bmw', 'Subaru', 'Toyota']

#reverse in alphabetical order, this is done by passing the argument reverse=True
#dont forget the method of an given set of value is set after the dot sign
cars.sort(reverse=True)
print (cars)
#output ['Toyota', 'Subaru', 'Bmw', 'Audi'] this is reversed in alpahbeteical order

#sorting a list temporary
#note they've been sorted but the original order hasnt been changed
Movers = ['Bmw', 'Audi','Toyota', 'Subaru']
print(sorted(Movers)) #output ['Audi', 'Bmw', 'Subaru', 'Toyota']
print(Movers) #output ['Bmw', 'Audi', 'Toyota', 'Subaru']

#reversing the order of items in a list
Music =['Jazz', 'HipHop', 'Retro', 'Instrumental']
print(Music)#output ['Jazz', 'HipHop', 'Retro', 'Instrumental']
Music.reverse()
print (Music)#ouput ['Instrumental', 'Retro', 'HipHop', 'Jazz']

#finding the length of a a list
Music =['Jazz', 'HipHop', 'Retro', 'Instrumental']
print (len(Music))
