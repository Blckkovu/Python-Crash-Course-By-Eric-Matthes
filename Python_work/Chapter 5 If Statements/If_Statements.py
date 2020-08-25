#If statements allow you to examine current states of a program and allows you to respond appropriaately to that state
#A simple example
Names= ['James', 'Ken', 'Rm', 'Stace']
for Name in Names:
    if Name=="rm":
        print(Name.upper())
    else:
        print(Name)
#the loop first checks if the current value of names is rm. if it is it is printed with an upper font
#the fifth line checks if the name is equal to the value this is done with a double equal sign(==)
#the double equal sign checks for equality(==)


#Checking for equality
Pizza='Debonairs'
if Pizza != 'Debonairs' :
    print("Don't deliver!")
else:
    print("Deliver")
# the not equal sign (!=) checks if the value assigned is false/do not much

#Personal example
Answer= 9*9
if Answer != 81:
    print(wrong)
else:
    print("Continue")

#Rather than eqaul or not equal u can also check for lesser or greater than between values
Number=9
if Number > 10:
    print("Nice")
else:
    print("Try again")
#this checks for a value greater than the expected value

#checks for value lesser than
Number=9
if Number < 10:
    print("Nice")
else:
    print("Try again")

#checks for greater or equal to
Number=10
if Number >= 10:
    print("Nice")
else:
    print("Try again")

#using and
#checking for multiple conditions are both true
age_1=20
age_2=23
if age_1 > 18 and age_2 > 26:
    print("Valied")
else:
    print("Too young")
#the overall expression comes out as false(too young) because one of the conditions is false

#using or to check multiple conditions
#it passes if either one of the conditions is true(valied)
age_1=20
age_2=23
if age_1 > 18 or age_2 > 26:
    print("Valied")
else:
    print("Too young")

#checking whether a value is in a list
Banned_users=['Victor', 'Kanake', 'Alan']
user = 'Ida'
if user in Banned_users: 
    print(user.title() + 'access denied')
else:
    print('access approved')
#you can also use (if user not in)
