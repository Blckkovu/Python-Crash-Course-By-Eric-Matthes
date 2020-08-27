#exercise 5.1
#Writing a series of conditional test
Deity= "Thoth"
if Deity== 'Thoth':
    print('Wisdom')
else:
    print('Wrong deity')


polarity="North"
if polarity == "South":
    print('Face South')
else:
    print("Face North")

#or
vibration1= 176
vibration2= 160
if vibration1 > 174 or vibration2 > 174 :
    print("Your good")
else:
    print("Please Meditate")
    #or ust checks if one condition is true

#and
vibration1= 174
vibration2= 160
if vibration1 > 174 and vibration2 > 174 :
    print("Your good")
else:
    print("Please Meditate")
    #and checks if both conditions are both true or false


#exercise 5.2
#test for equality
Car = "Tesla"
if Car == "Tesla":
    print (True)
else:
    print(False)

#test for inequality
Car = "Tesla"
if Car != "Tesla":
    print (True)
else:
    print(False)

#Numerical test
Number=10
if Number == 10:
    print ('exact')

Number=10
if Number < 10:
    print ('less')

Number=11
if Number > 10:
    print ('Great')

Number=12
if Number >= 10:
    print ('perfect')

#Tests using the and keyword and the or keyword
Number=100
if Number > 50 or Number < 90:
    print ('passed')

Number=100
Number1=90
if Number > 70 and Number1 < 92:
    print ('passed')
else:
    print('failed')

#test whether an item is in a list
arr = [1,2,3,4,5]
if 1 in arr:
    print(True)

if 7 in arr:
    print(True)
else:
    print(False)
