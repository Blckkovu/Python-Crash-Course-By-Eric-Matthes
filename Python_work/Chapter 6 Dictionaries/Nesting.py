#A list of Dictionaries
alien_0={
'color':'green',
'points': 5
}
alien_1={
'color':'yellow',
'points':10
}
alien_2={
'color':'red',
'points': 15
}
Aliens=[alien_0, alien_1, alien_2]
for alien in Aliens:
    print(alien)


#automatically generate
#making an empty list
Aliens=[]
#generating new aliens
for alien_number in range(20):
#Creating a dictionary for new aliens
    new_alien={
    'color':'green',
    'points':5,
    'speed':'slow'}
#placing every alien generated in a list
    Aliens.append(new_alien)
#showing the first 5 aliens
for alien in Aliens[:5]:
    print(alien)
#showing the total number of aliens created
print("Total number of aliens  generated " + str(len(Aliens)))

#change in dictionary
Ships=[]
for Ships_numbers in range(30):
    new_ships={
    'color':'white',
    'points':50
    }
    Ships.append(new_ships)
for ship in Ships[10:20]:
    if ship['color']=='white':
        ship['color']='black'
        ship['points']=-100

for ship in Ships[10:20]:
    print(ship)
for ship in Ships[:30]:
    print(ship)


#A list in a dictionary
Pizza={
'Type':'Something Meaty',
'Size':'Large',
'Crust':'Thick',
'Toppings':['Mushrooms', 'Extra cheese']
}
print("You've ordered a "+ Pizza['Size'] +' '+ Pizza['Crust']+' ' + Pizza['Type'] + " pizza with the following toppings: " )
for topping in Pizza['Toppings']:
    print("\t"+topping)

#a dictionary within a dictionaary
users={
'Einstein':{
'first':'Albert',
'second':'Einstein',
'location':'Germany',
},
'Maurice':{
'first':'Nikola',
'second':'Tesla',
'location':'USA',
},
}
for Username, user_info in users.items():
    print("\nusername: "+ Username.title())
    full_name= user_info['first'] + " "+ user_info['second']
    location=user_info['location']
    print("\tFull Name: "+ full_name.title())
    print("\tLocation: "+ location.title())
