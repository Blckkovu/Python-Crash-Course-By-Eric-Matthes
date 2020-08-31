#exercise 5.8
Users=['Admin', 'James', 'Ida', 'Emity', 'Luz']
for user in Users:
    if user =="Admin":
        print('Hello ' + user.upper() + ' would you like to see your status report? ')
    else:
        print('Hey '+ user.title() + ' welcome back')

#exercise 5.9
Users=[]
if Users:
    for user in Users:
        print('Hello '+ user.title())
else:
    print('We need to find some Users')

#exercise 5.10
Current_Users=['Admin', 'James', 'Ida', 'Emity', 'Luz', 'JOHN']
for Current_User in Current_Users:
    Current_User=Current_User.title()
    print(Current_User)

new_users=['Quintin', 'Margo', 'Asefa', 'Luz', 'John']
for new_user in new_users:
    new_user=new_user.title()
    print(new_user)

if new_user in Current_Users:
    print('\nName '+ new_user.title() + ' in use')
    print("use another name")
else:
    print('The name '+ new_user.title() +' is available ')

#Exercise 5.11
Ordinal_Numbers=[1,2,3,4,5,6,7,8,9]
for Ordinal_Number in Ordinal_Numbers:
    if Ordinal_Number == 1:
        print(str(Ordinal_Number) + 'st')
    elif Ordinal_Number == 2:
        print(str(Ordinal_Number) + 'nd')
    elif Ordinal_Number == 3:
        print(str(Ordinal_Number) + 'rd')
    else:
        print(str(Ordinal_Number) + 'th')
