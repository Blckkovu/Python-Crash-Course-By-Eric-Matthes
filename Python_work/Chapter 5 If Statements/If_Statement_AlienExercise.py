#Alien color 5.3
Alien_color=['Green', 'yellow', 'red']
if 'Green' in Alien_color:
    print('5 points earned')

#iftest
if "yellow" in Alien_color:
    print("30 points earned")
#this version has no output
if 'blue' in Alien_color:
    print('100 points earned')

#exercise 5.4
Alien_color= "Green"
if Alien_color == 'Green':
    print('5 points earned')
else:
    Alien_color != 'Green'
    print('10 points earned')

Alien_color= "Red"
if Alien_color == 'Green':
    print('5 points earned')
else:
    Alien_color != 'Green'
    print('10 points earned')

#exercise 5.5
Alien_color=['Green', 'yellow', 'red']
if 'Green' in Alien_color:
    print('5 points earned')
elif 'yellow' in Alien_color:
    print('10 points earned')
elif  'red'in Alien_color:
    print('15 points earned')

#exercise 5.6
age=30
if age <2:
    print("You are a baby")
elif age <4:
    print('You are a Toddler')
elif age <13:
    print('You are a Kid')
elif age <20:
    print('You are a Teenager')
elif age <65:
    print('You are an Elder')

#exercise 5.7
favourite_fruits=['Apples', 'Watermelon', 'Orange', 'Banana']
if 'Orange' in favourite_fruits:
    print('You really like Oranges')


#Usin if statements with lsit
#you can watch for special values that needs to be treated differently
#ensures you code works in all possible situations

#checing for special items in a list
Pizzas = ['Something Meaty']
Extra_Toppings=['Cheese', 'mushroom', 'meat', 'Bbq.Sauce']
for Pizza in Pizzas:
    print(Pizza.title() + ' Ordered')
for Extra_Topping in Extra_Toppings:
    if Extra_Topping=="Bbq.Sauce":
        print("We are out of Bbq Sauce")
    else:
        print('Adding extra ' + Extra_Topping.title())

print("\n Pizza in progress wait 2o mins")

#checking that a lsit is not empty
Toppings=[]
if Toppings:
    for topping in Toppings:
        print("Adding" + topping)
    print("\nfinished making you pizza")
else:
    print("are you sure you want a plain Pizza")
#if Toppings line checks if the list is empty before jumping into a for loop

#using multiple list
Available_toppings=['blue cheese', 'Mushrooms', 'Meat']
requested_toppings=['Mushrooms', 'blue cheese', 'pepper']
for requested_topping in requested_toppings:
    if requested_topping in Available_toppings:
        print("Adding "+ requested_topping)
    else:
        print(requested_topping+ ' not available')
