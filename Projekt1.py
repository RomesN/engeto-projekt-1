TEXTS = ["""
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. """,

         """At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.""",

         """The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present."""
         ]

# dict of registered users {user: pass}
reg_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# helping variable
separator = "-" * 40

# singing in and eventual welcome
usern = input("username: ")
passw = input("password: ")

print(separator)

if reg_users.get(usern) == passw:
    print(f"Welcome to the app, {usern}.")
    print(f"We have 3 texts to be analyzed.")
    print(separator)
else:
    print("The user not registered! This program ends for you.")
    print(separator)
    quit()

# choosing text to analyze
text_choice = input("Enter a number between 1 and 3 to select: ")

print(separator)

# quiting if wrong input
if not text_choice.isnumeric():
    print("The program ends. Please select number between 1 and 3.")
    print(separator)
    quit()
elif int(text_choice) not in range(1, 4):
    print("Oh no! Such text does not exist. Please select number between 1 and 3.")
    print(separator)
    quit()

# defining variables
text_analyzed = TEXTS[int(text_choice) - 1]
word_list = []
word_counter = 0
title_counter = 0
upper_counter = 0
lower_counter = 0
numeric_counter = 0
numbers_counter = 0
word_len = 0
word_len_c = 0
words_len_dic = dict()

# text cleaning
for word in text_analyzed.split():
    word_list.append(
        word.strip(",.:;!#%&?")
    )

# calculating statistics
for word in word_list:
    word_counter += 1
    if word.istitle():
        title_counter += 1
    if word.isupper() and word.isalpha():
        upper_counter += 1
    if word.islower():
        lower_counter += 1
    if word.isdigit():
        numeric_counter += 1
        numbers_counter += int(word)
    word_len = 0
    for char in word:
        word_len += 1
    else:
        words_len_dic[word_len] = words_len_dic.setdefault(word_len, 0) + 1

# putting values from dict {Len: Frq} into list of tuples (Len, Frq) ascending according to word length
words_len_dic_cop = words_len_dic.copy()
words_len_sorted = [words_len_dic_cop.popitem()]
for key in words_len_dic_cop:
    for index, pair in enumerate(words_len_sorted):
        if key < pair[0]:
            words_len_sorted.insert(index, (key, words_len_dic_cop[key]))
            break
    else:
        words_len_sorted.append((key, words_len_dic_cop[key]))

# printing
print(f"There are {word_counter} word/s in the selected text.")
print(f"There are {title_counter} titlecase word/s.")
print(f"There are {upper_counter} uppercase word/s.")
print(f"There are {lower_counter} lowercase word/s.")
print(f"There are {numeric_counter} numeric string/s.")
print(f"The sum of all the numbers is {numbers_counter}.")
print(separator)
print(f"LEN|  OCCURENCES  |NR.")
print(separator)
for LenFrq in words_len_sorted:
    ast_line = "*" * LenFrq[1]
    print(f"{LenFrq[0]:<2}|{ast_line:<20}|{LenFrq[1]:<2}")
