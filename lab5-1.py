'''
###########
Lab 5.01
###########

Instructions
------------
Write a program that uses a dictionary to offer users the meanings of common internet abbreviations.
The program, dictionary_lab.py, prompts the user to enter an internet abbreviation they would like explained. 
If the requested abbreviation is in the program's dictionary (use the in keyword with an if statement 
to test this), then it prints out the definition. If the abbreviation is not in the dictionary, the program 
prints an apologetic message saying that it could not find a definition.

Example Output:
---------------
>>> python3 dictionary_lab.py

What word would you like to look up? nbd
nbd: a phrase meaning no big deal

What word would you like to look up? kittens
Sorry, kittens is not defined

What would would you like to look up?

Bonus
------
Extend the program with any of these features:
The user can
update the definitions (values) for existing abbreviations in the dictionary
add new abbreviations (keys) and provide their definitions (values).
delete entries (key, value pairs) from the dictionary.
get the entire dictionary printed to the screen.
Lesson 6.01 did not cover all the techniques for manipulating dictionaries that you will need to program these features. Search for the necessary information in the [Python tutorial about dictionaries][1] and the [advanced Python documentation about dictionaries][2].
'''

user_input = input("Enter a common internet abbreviations and we'll let you know what they mean! ")

my_dictionary = {
'lol': 'laughing out loud',
'omg': 'Oh my God',
'btw': 'By the way',
'asap': 'As soon as possible',
'gtg': 'got to go',
'imo': 'In my opinion',
'fr': 'For real',
'ttyl': 'Talk to you later',
'ong': 'On God'}


if user_input in my_dictionary:
    print(my_dictionary[user_input])
else:
    print("Sorry, we dont know this one! Try another")

print(my_dictionary)