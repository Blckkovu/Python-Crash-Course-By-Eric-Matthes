#Exercise 2.3 & 2.4
# peronal Message; Store a persons name in a variable and print a message to that person
#print the persons name in lowercase, uppercase and title case
Name = ("Neo")
print("Hello " + Name.upper() + " are you are the one!")
print("Hello " + Name.lower() + " are you are the one!")
print("Hello " + Name.title() + " are you are the one!")

#exerecise 2.6
#Find a quote from the famous perosn you admire, print the quote and name of its author
#The store the persons name
#then compose your message then store it in an ew variable called message, print your message
Quote = "\nWhat you know you can't explain, but you feel it. You've felt it your entire life, that there's something wrong with the world. You don't know what it is, but it's there, like a splinter in your mind, driving you mad."
famous_person = ("\nMorpheus")
print (famous_person +"-"+ Quote)

#exercise 2.7 Stripping names
#
fName="  Alexander"
sName= "    \tAsefa"
fName=fName.strip()
sName=sName.strip()
full_name= fName +' '+ sName
Message="\nHello " + full_name
print(Message)

#I didnt cover much about strip and whitespacing inthis section because the key notes to learn them was quite simple
#When using whitespacing you can declare them in the value assigned to the variable or when printing an output that does not need to be changed
#when stripping names or any other value yoou need to first store the values in a vaariable then use the method .strip on each variable as shown above
