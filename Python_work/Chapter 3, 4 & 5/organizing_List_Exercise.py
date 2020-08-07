#exercise 3.8
Visit =['Chile', 'Tibet', 'Bali', 'Egypt', 'Canada']
print(Visit)

#soting in alphabetical order
print (sorted(Visit))

#showing original order
print(Visit)

#print in reverse alphbatical order
Visit.sort(reverse=True)

#show its in its original order
print(Visit)

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
