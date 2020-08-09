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
Visit.sort(reverse=)
#output ['Tibet', 'Egypt', 'Chile', 'Canada', 'Bali']

#show its in its original order
print(Visit)
#output ['Bali', 'Canada', 'Chile', 'Egypt', 'Tibet']

#use reverse to change order of list
Visit.reverse()
print(Visit)

#use reverse to change order of list again
Visit.reverse()
print(Visit)

#okay my head hurts i cant seem to know whats happening from line 18
#so im just gonna finish the last 2 exercise
#exercise 3.9
print(len(Visit))
places=(len(Visit))
message= "I'm travelling to " + str(places) + " places in the future."
print(message)


#When working with list unknown errors might occur but check the actual list or number of items on a list this is because it might have been managed dynamiccaly by the program
