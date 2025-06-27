import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
    
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#format_words = {new_key:new_value for (index, row) in df.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
format_words = {row['letter']:row['code'] for (index, row) in data.iterrows()}

word = input("enter a word: ")
phonetic_list = [format_words[letter] for letter in word.upper()]
print(phonetic_list)
