#changig values for the first item of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

motorcycles[0]= 'ducati'
print (motorcycles)
#note the first element has been changed

#appending elements in a list
#the append command is used to add an element to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
#inserting elements in a list
motorcycles.insert(1, 'Tesla')
#the append command adds itat the last position while the insert position adds it in the beginning

print (motorcycles)

#the append method can be used to build list dynamically
#the elements below have been added to the list above
motorcycles.append('honda')
motorcycles.append('yamaha')
print (motorcycles)

#Removing elements using the del statement but you have to know the position of the item from the list
del motorcycles[1]
print (motorcycles)
#note the Tesla item has been removed which is the second one

#Sometimes youll want to remove the value of an item after removing it
#for example you may want to know the x an y position of an alien that was just shot down so that you may draw an explosion at that point
#in this instance use the pop() method
print (motorcycles)
popped_motorcycle = motorcycles.pop()
print (motorcycles)
print(popped_motorcycle)
#the end value yamaha was removed from the list and stored in popped_motorcycle

#generating a statement with the last item
print ('I hate a ' + popped_motorcycle.title() )

#generating a statement with the first item
#we selected the first item by using the index position
first_motorcycle = motorcycles.pop(0)
print ('I love '+ first_motorcycle.title() + 'because its really comfortable.')

#Removing an item by value
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
