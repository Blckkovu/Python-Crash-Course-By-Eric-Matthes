#Exercise 6.4
Programming_words={
'Python':'A programming language',
'Hashtags':'Used to write sentences',
'Looping':'shifting between different elements in a list',
'dictionary':'A collection of key value pairs '

}
for name, meaning in Programming_words.items():
    print(name.title() + ": " + meaning.lower())

#exercise 6.5
Major_Rivers={
'Nile':'Egypt',
'Tana':'Kenya',
'Shibeli':'Somali',
'Nairobi':'Nairobi'
}
for river, country in Major_Rivers.items():
    print("The "+ river.title() + " runs through "+ country.title())

for river in Major_Rivers.keys():
    print(river.title())

for country in Major_Rivers.values():
    print(country.title())


#Exercise 6.6
students=['Ken', 'Jim','Lee', 'elda', 'Luz']
favourite_languages={
'Ken':'C+',
'Jim':'Python',
'Lee':'HTML',
'Luz':'JavaScript'
}
for student in students:
    if student not in favourite_languages.keys():
        print (student.title()+ ' please take your poll')
else:
    for student, language in favourite_languages.items():
        print(student.title() + "'s favourite language is " + language.title() )
