#exercise4.10
Movies=['Chuck','Avengers', 'Avatatar','Wizards','HarryPotter']
print('The first three items are:')
print(Movies[:3])
#output['Chuck', 'Avengers', 'Avatatar']

print('The items from the middle to the last are: ')
print(Movies[2:])
#output ['Avatatar', 'Wizards', 'HarryPotter'

print('The last three items are: ')
print(Movies[:3])
#output['Chuck', 'Avengers', 'Avatatar']

#exercise 4.11
Pizzas =['Hawaian', 'BBQ', 'Chicken', 'Teriaki',]
Friend_Pizzas=Pizzas[:]
Pizzas.append('Vegan')
Friend_Pizzas.append('Double delax')
print(Pizzas) #output ['Hawaian', 'BBQ', 'Chicken', 'Teriaki', 'Vegan']
print(Friend_Pizzas) #output['Hawaian', 'BBQ', 'Chicken', 'Teriaki']

print('My best pizzas are: ')
for pizza in Pizzas[:]:
    print(pizza)

print('My friends best pizzas are: ')
for f_pizza in Friend_Pizzas[:]:
    print(f_pizza)
