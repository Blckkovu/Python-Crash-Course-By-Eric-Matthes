#exercise 3.4 guest list
#crate a list of people inviting them for dinner and invite them individually
invites= ['Nikola', 'Albert', 'Galileo', 'Socrates']
print (invites)
message1= invites[0].title() + ' you are invited to the Gala.'
message2= invites[1].title() + ' you are invited to the Gala.'
message3= invites[2].title() + ' you are invited to the Gala.'
message4= invites[3].title() + ' you are invited to the Gala.'
print(message1)
print(message2)
print(message3)
print(message4)

#exercise 3.5 changing guest list
#Someone cant make it so you have to inviite someone else
message5= invites[1].title() + " can't make it to the Gala"
print(message5)

#modifying the list with the name of the person who cant make it with the name of the person you are inviting

invites.remove('Albert')
print (invites)

#replacing the name of the person who can't make it with one who can
invites.insert(1,'zackerberg')
print(invites)

#second invitation
message1= invites[0].title() + ' you are invited to the Gala.'
message2= invites[1].title() + ' you are invited to the Gala.'
message3= invites[2].title() + ' you are invited to the Gala.'
message4= invites[3].title() + ' you are invited to the Gala.'

#printing new invites
print ('new invites')
print(invites)
print(message1)
print(message2)
print(message3)
print(message4)

#exercise 3.6 more guests
#informing people there is more space
print('Space for three more people is available')
invites.insert(4, 'Ken')
invites.insert(5, 'Lee')
invites.append('Klare')
print(invites)
message1= invites[0].title() + ' you are invited to the Gala.'
message2= invites[1].title() + ' you are invited to the Gala.'
message3= invites[2].title() + ' you are invited to the Gala.'
message4= invites[3].title() + ' you are invited to the Gala.'
message5= invites[4].title() + ' you are invited to the Gala.'
message6= invites[5].title() + ' you are invited to the Gala.'
message7= invites[6].title() + ' you are invited to the Gala.'

#print a new set of invites
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)

#the point of this task is to see whether you've understood how to modify a list
#shrink guest list so that only 2 people are invited
print (invites)
#remove invite so as your left with only 2

popped_1Uninvited = invites.pop(0)
popped_2Uninvited = invites.pop(1)
popped_3Uninvited = invites.pop(2)
popped_4Uninvited = invites.pop(3)
popped_4Uninvited = invites.pop(-1)

#not certain how each item was stored in so i used -1


#inviting the last 2
print (invites)
print(message2)
print (message4)

#removing the last 2 invites
print (invites)
del invites[1]
del invites[0]

print(invites)
