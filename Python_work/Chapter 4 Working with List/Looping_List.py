#Looping through an entire list this is done to perorm the same task on each items
#for example you may want to perform the same task on every item in a alist
magicians =['Alice', 'Quentin', 'Juliet', 'Eliot', 'Margo']
for magician in magicians:
    print(magician)
    #The concept of looping is important when a computer wants to do repetive task
    #python initially reads the first line of loop and stores the first value from the list of magicians and stores it in the variable magician
    # python repeats the loop till the last value
    #don't forget to use a proper naming convention for the variable, plural abd singular method is the best notice magician in magicians

#printing messages in list
for magician in magicians:
    print(magician.title() + ' is an awesome actor in the show "The Magicians"')
    print("I can't wait for the next episode " + magician.title())

#to print a message to after a loop do not forget not to indent the last line
print("The Magicians is freaking amazing!")

#Don't forget to indent because you might receive an error
#Don't indent  unnecesarilly
#Don't forget to use a colon because you'll get a syntax error

#exercise 4.1
Pizzas =['Hawaian', 'BBQ', 'Chicken', 'Teriaki',]
for Pizza in Pizzas:
    print("I love " + Pizza.title())
print("The best is " + Pizzas[0].upper() + " though")

#exercise 4.2
Animals= ['cats', 'dogs', 'dolphins', 'snakes']
for animal in Animals:
    print (animal)

#if you can store a mwssage i a list an print it accordingly with the animal list please do so


print('All of them are pets')
