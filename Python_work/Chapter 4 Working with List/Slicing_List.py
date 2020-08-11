#print a part of ac slice of a alist
Bclover= ['Asta', 'Yami', 'Vanessa', 'Noelle']
print(Bclover[0:3])
#output ['Asta', 'Yami', 'Vanessa']
#the structure of the list is maintained by it prints out the first 3

#when you omit the first index and in a slice python automatically starts your slice at the beginning of the list
Bclover= ['Asta', 'Yami', 'Vanessa', 'Noelle']
print(Bclover[:2])
#output ['Asta', 'Yami']

#looping through a alist
print('Here are the members of the black clover:')
for member in Bclover[:4]:
    print(member.upper())
#when working with data you can you can slice to process your data in chunks


#copying a lsit
#to copy alist you can eit the first and second index
my_foods = ['Pizza', 'Cake', 'Fries']
friends_food= my_foods[:]
print("I love ")
print(my_foods)

print("my friend's favourite foods are:")
print(friends_food)
