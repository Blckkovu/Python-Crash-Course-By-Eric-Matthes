#tuples is used to create a list of items that cant change
#tuples look like a list but use paranthesis instead of square brackets
dimesnsions= (200,50)
print(dimesnsions)
print(dimesnsions[0])
print(dimesnsions[1])

#looping through all values in a tuple
for dimesnsion in dimesnsions:
    print(dimesnsion)

#we cant change the value in a tuple but we can write over a tuple
dimesnsions= (30,500)
print ('Original dimesnsions:')
print(dimesnsions)

dimesnsions= (450,900)
print ('Changed dimesnsions:')
print(dimesnsions)

#Exercise 4.13
Buffet_Menu=('Fries', 'Rice+stew', 'Ugali+kale', 'Chicken')
print( Buffet_Menu)
for food in Buffet_Menu:
    print(food)

#Nwe list
Buffet_Menu=('Fries', 'Rice & pea stew', 'Ugali & kale', 'Injera & Beef stew')
print("New_List")
for food in Buffet_Menu:
    print(food)

#creating an error
Buffet_Menu.insert(2, Injera)
Buffet_Menu.insert(-1, chicken_stew)
print(food)
#values in a tuple cannot be changed
