import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
format_words = {row['letter']:row['code'] for (index, row) in data.iterrows()}

def gen_phonetic():  
    try:
        word = input("enter a word: ")
        output_list = [format_words[letter] for letter in word.upper()]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        gen_phonetic()   
    else:
        print(output_list)          

gen_phonetic()
