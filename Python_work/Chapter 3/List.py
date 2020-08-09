#A list is  a collection of item in a particualr order
#You can out anything you want into a list and the items in your list dont have to be related in any way because a list usually contains more than one element
#In python square brackets indicate a list, ([])

Languages = ['Python', 'Java', 'C+', 'Dart', 'JavaScript']
print (Languages)

#when we asked for a specific item in python always index as below
Languages = ['Python', 'Java', 'C+', 'Dart', 'JavaScript']
print (Languages[0])

#or
#in this example the output is capitalized
print (Languages[0].upper())
print (Languages[2] + ' is a boring language')
#index position always starts at 0 the second 1....

#When asking for the last index you ask with the index -1
print(Languages[-1]+ ' is fun for hacking.')

#using individual values from a list and create a message by concatenation
Person = ['Elon', 'Eric', 'Tesla', 'Einstein', 'Peter']
message = Person[4].title() + ' was forced to code the program.'
print(message)

#exercise
Names= ['James', 'Peter', 'Eric', 'Solomon']
print (Names[0])
print(Names[1])
print(Names[2])
print(Names[3])
message1= 'Hey ' + Names[0] + ' !'
message2= 'Hey ' + Names[1] + ' !'
message3= 'Hey ' + Names[2] + ' !'
message4= 'Hey ' + Names[3] + ' !'
print(message1)
print(message2)
print(message3)
print(message4)
