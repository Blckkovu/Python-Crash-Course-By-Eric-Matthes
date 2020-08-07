#sorting a list permanently with sort()method
cars = ['Bmw', 'Audi','Toyota', 'Subaru']
cars.sort()
print(cars)
#The cars have been arranged in alphabetical order

#reverse in alphabetical order
#dont forget the method of an given set of value is set after the dot sign
cars.sort(reverse=True)
print (cars)

#sorting a list temporary
#note they've been sorted but the original order hasnt been changed
Movers = ['Bmw', 'Audi','Toyota', 'Subaru']
print(sorted(Movers))
print(Movers)

#revesing the order of items in alist
Music =['Jazz', 'HipHop', 'Retro', 'Instrumental']
print(Music)
Music.reverse()
print (Music)

#finding the length of a a list
Music =['Jazz', 'HipHop', 'Retro', 'Instrumental']
len(Music)
print (len(Music))
