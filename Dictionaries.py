# This program is for rosalind.info/problems/ini6/

# This program will read a string and return the number of occurences of each
# word in the string. 

# Amanda Zacharias; April 29th, 2021

"""
In a dictionary there are keys:values.
    keys can be strings, numbers, floats, or other immutable types
    values can be any type

accessing values from a dictionary:
    phones = {'Zoe':'232-43-58', 'Alice':165-88-56}
    print phones['Zoe']

adding new values or assigning a new value to an existing key:
    phones['Zoe'] = '658-99-55'
    phones['Bill'] = '342-18-25' #Bill appears at the beginning of the dictionary
    print phones

Ordering of dictionaries:
    case senstive ~ uppercase is before lowercase

Create an empty dictionary:
    d = {}
    # Can use to add values dynamically (ex. reading a file)

Check whether a key is in the dictionary:
    if 'Peter' in phones:
        print "We know Peter's phone"
    else:
        print "We don't know Peter's phone"

# Delete a key:value pair
    phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
    del phones['Zoe']
    print phones
"""

"""
Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated
    by spaces. Words are case-sensitive, and the lines in the output can be in
    any order.
"""

s = "When I find myself in times of trouble Mother Mary comes to me Speaking "\
    "words of wisdom let it be And in my hour of darkness she is standing right "\
    "in front of me Speaking words of wisdom let it be Let it be let it be let "\
    "it be let it be Whisper words of wisdom let it be And when the broken "\
    "hearted people living in the world agree There will be an answer let it "\
    "be For though they may be parted there is still a chance that they will "\
    "see There will be an answer let it be Let it be let it be let it be let it "\
    "be There will be an answer let it be Let it be let it be let it be let it "\
    "be Whisper words of wisdom let it be Let it be let it be let it be let it "\
    "be Whisper words of wisdom let it be And when the night is cloudy there is "\
    "still a light that shines on me Shine until tomorrow let it be I wake up "\
    "to the sound of music Mother Mary comes to me Speaking words of wisdom let "\
    "it be Let it be let it be let it be yeah let it be There will be an answer "\
    "let it be Let it be let it be let it be yeah let it be Whisper words of "\
    "wisdom let it be"
# Split the string into a list where each word is a list item.
# Whitespace is used to deliminate words.
s_list = s.split()
# In this dictionary, key = word, value = number of occurences in the string
word_dict = {}

for word in s_list:
    # If the word isn't in the dictionary, add it to the dict w/ a value of 1
    if word not in word_dict:
        word_dict[word] = 1
    # If the word is in the dictionary, add one to the existing count
    else:
        word_dict[word] = word_dict[word] + 1

# For every word in the dictionary print the word and its number of occurences. 
for word in word_dict:
    print (word, word_dict[word])




