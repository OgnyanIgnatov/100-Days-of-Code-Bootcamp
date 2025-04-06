

def alg():

    names_list=[]
    with open("./Day24/Input/Names/invited_name.txt", mode="r") as names:
        for name in names.readlines():
            names_list.append(name.strip())

    text=str()
    with open("./Day24/Input/Letters/starting_letter.txt", "r") as letter:
        text = letter.read()

    for name in names_list:
        with open(f"./Day24/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_to:
                letter_to.write(text.replace("[name]", f"{name}"))
    

alg()              
    
