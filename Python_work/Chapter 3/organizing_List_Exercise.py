#exercise 3.8
#store a list and print out the list
Visit =['Chile', 'Tibet', 'Bali', 'Egypt', 'Canada']
print(Visit)
#output ['Chile', 'Tibet', 'Bali', 'Egypt', 'Canada']

#soting in alphabetical order withouth changing the order
print (sorted(Visit))
#output ['Bali', 'Canada', 'Chile', 'Egypt', 'Tibet']

#showing original order
print(Visit)
#output ['Chile', 'Tibet', 'Bali', 'Egypt', 'Canada']

#print in reverse alphbatical order
print(sorted(Visit,reverse=True))
#output ['Tibet', 'Egypt', 'Chile', 'Canada', 'Bali']

#show its in its original order
print(Visit)
#output ['Chile', 'Tibet', 'Bali', 'Egypt', 'Canada']

#use reverse to change order of list
Visit.reverse()
print(Visit)
#ouput ['Canada', 'Egypt', 'Bali', 'Tibet', 'Chile']

#use reverse to change order of list again
Visit.reverse()
print(Visit)
#output ['Chile', 'Tibet', 'Bali', 'Egypt', 'Canada']

#exercise 3.9
print(len(Visit))
places=(len(Visit))
message= "I'm travelling to " + str(places) + " places in the future."
print(message)


#When working with list unknown errors might occur but check the actual list or number of items on a list this is because it might have been managed dynamiccaly by the program
