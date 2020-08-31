#Looping through all key-value pairs
user={
'Username':'Meliodas',
'first_Name':'Sin',
'second_name':'wrath'
}
for key, value in user.items():
    print(key +' ' + value )

favourite_fruits={
'Jen':'Oranges',
'Ken':'Banana',
'Lee':'Apples',
'James':'Watermelon'
}
#the code below tells python to loop through each key-value pair in the dictionary]
for name, fruit in favourite_fruits.items():
    print(name.title()+"'s favourite_fruit is "+ fruit.title())

Peoples_Age={
'James':22,
'Lee':20,
'Purity':50
}
for name in Peoples_Age:
    print(name)
if 'Steve' not in Peoples_Age.keys():
    print("Steve please put your age")

#Looping in order of all values in a dictionary
for age in sorted(Peoples_Age.values()):
    print("Ages are "+ str(age))
