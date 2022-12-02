'''
#############
Lab 5.02
#############
In this lab we will implement a word frequency algorithm. 
It will tell you how many of each word you had in an essay.

At the top of the document save a variable with a long paragraph (example below). 
In order to turn this paragraph into a list of lower case words we will use the split(" "), 
replace(), and lower() functions. There is code at the bottom of this page that will do this 
for you. Feel free to read more about split() in the Python documentation, but it's not critical 
to this lab.

For each word in the document, count the number of times it occurs. Consider the following phrase: 
'Cats are cool. Baby cats are called kittens. Cats make great pets.' The word 'cats' appears 3 times. 
The word 'are' appears 2 times.

The program will first create a dictionary with the words as keys and the number of times they occur 
as values. Then it will prompt the user which word they are curious about. If the word was in the 
paragraph it will print the number of times it occurred.

Example
------------
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? cats
'cats' occurs 3 times
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? dogs
'dogs' does not occur

split, replace, and lower
--------------------------
This is the code to lower case the letters in the paragraph, remove the periods, and split them into 
individual words.

example_paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk 
from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in 
New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided 
to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande 
decides to go to Times Square instead. What a beautiful day in New York."

#make all letters lowercase
example_paragraph_lower = example_paragraph.lower()

#remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")

#convert paragraph into a list of individual strings
example_word_list = example_paragraph_lower_no_punctuation.split(" ")
'''
how_many = 0 
example_paragraph = "cats it was a beautiful day in new york city. Our hero ariana grande was on a walk from the standard to duane reade. ariane grande was walking rather quickly because she had lived in new york for a few months. all of a sudden a slimy donut appeared out of nowhere. ariana grande decided to prance foolishly instead of dealing with the situation. Thrown off of from duane reade ariana grande decides to go to times square instead. what a beautiful day in new york."
example_paragraph_lower = example_paragraph.lower()
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")
example_word_list = example_paragraph_lower_no_punctuation.split(" ")
print(example_paragraph)
user_input = input("What word are you curious about? ")
for word in example_paragraph:
    how_many+=1 
my_dictionary = {"cats": (f'cats appears {how_many} times'),

}

if user_input in my_dictionary and example_paragraph:
    print(my_dictionary[user_input])
else:
    print(f"{user_input} does not occur")



