#Dictionaries help you to connect pieces of related information and modify that information
#dictionaries can store almost limitless amount of information

#A simple dictionary
#using dictionaries takes practise
#dictionary in Python is a collection of key-value pairs. Each key is connected to #to a value, and you can use a key to access the value associated with that key.

#A dictionary is wrapped in braces {} with a series of key value pairs inside the braces
#color is a key value and green is the value
alien_0={'color':'Green', 'points':5}
#To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets
print(alien_0['color'])
print(alien_0['points'])

#accessing values in  a dictionary
new_points= alien_0['points']
message=("You've just earned " + str(new_points) + " points")
print(message)

#Adding new key value pairs
#Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time
#adding new key value pairs
alien_0['x-position']=0
alien_0['y-position']=25
print(alien_0)

#Starting with an empty dictionary
#typically youll use empty dictionaries when storing user-supplied data in a dictionary or when you write code that generates a larg number of key-value pairs automatically
Persona={}
Persona['Name']='James'
Persona['Location']='Nairobi'
Persona['Age']=23
Persona['Email']='james@yahoo.com'
print(Persona)

#modyfing values in a dictionary
Persona['Age']=22
print("2020 Isn't being recorded, so the age is "+ str(Persona['Age']))

#an alien that can move at different speeds
alien_1={}
alien_1['x-position']=0
alien_1['y-position']=25
alien_1['speed']='medium'
print('original x-position '+ str(alien_1['x-position']))

#determine how far the alien moved based on its current speed
if alien_1['speed']== 'slow':
    x_increment=1
elif alien_1['speed']=='medium':
    x_increment=3
else:
    alien_1['speed']=='high'
    x_increment=10

#the new position is the old position plus the x_increment
alien_1['x-position']=alien_1['x-position'] + x_increment
print('New position ' + str(alien_1['x-position']))

#removing key value pairs
del alien_1['y-position']
print(alien_1)
#note deleting key values removes it permanently

#
favourite_fruits={
'Jen':'Oranges',
'Ken':'Banana',
'Lee':'Apples',
'James':'Watermelon'
}
print(favourite_fruits['Ken'])
