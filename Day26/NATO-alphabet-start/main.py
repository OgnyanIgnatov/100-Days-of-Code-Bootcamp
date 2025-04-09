import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_data = {row.letter:row.code for _,row in data.iterrows()}

{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name: ")
l = [dict_data[letter.capitalize()] for letter in name]
print(l)
