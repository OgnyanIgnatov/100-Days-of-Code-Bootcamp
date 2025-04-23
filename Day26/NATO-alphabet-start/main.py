import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_data = {row.letter:row.code for _,row in data.iterrows()}

{"A": "Alfa", "B": "Bravo"}

while True:
    try:
        name = input("Enter your name: ")
        l = [dict_data[letter.capitalize()] for letter in name]
        print(l)
        break
    except: 
       print("Sorry, only letters in the alphabet please")
       
    
