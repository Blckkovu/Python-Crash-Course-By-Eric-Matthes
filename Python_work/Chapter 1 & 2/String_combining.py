#This is used to store different names or variables seperately then want to combine  and display them fully e.g names
first_name = "Elon"
Second_name = "Musk"
full_name = first_name +" "+ Second_name
print(full_name)
#the plus symbol is used to combine strings
#The method of combining strings is called concatenation
print(full_name.title() + " is a beast in the Tech World")
#Note weve used a method in the name and concatenated it with

#In the section below we will whitespace with tabs or newlines with (\t,(used for tabs) \n,(tells python to move to a new line) )
#You can only whitespace when declaring a value in a variable

#You can use concatenation to compose a message to someone
email= "\n\t\tElonMusk@org"
message = "\tSubscribe " + email.title()
print(message)
