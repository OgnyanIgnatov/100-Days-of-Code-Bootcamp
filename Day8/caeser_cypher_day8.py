alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(message, shift):
    encrypted_message=""

    for char in message:
        index_of_encrypted = (alphabet.index(char) + shift) % len(alphabet)
        encrypted_message += alphabet[index_of_encrypted]
    
    print(encrypted_message)

encrypt("hellz", 1)

def decrypt(message, shift):
    decrypted_message=""

    for char in message:
        index_of_decrypted = (alphabet.index(char) - shift) % len(alphabet)
        decrypted_message += alphabet[index_of_decrypted]

    print(decrypted_message)

decrypt("ifmma", 1)


def Ceaser():
    print("Welcome to the Ceaser Cypher!")
    func = input("Enter \"encrypt\" or \"decrypt\": ")
    message = input("Type your message: ")
    shift = int(input("Enter the shift number: "))

    if func == "encrypt":
        encrypt(message, shift)
    elif func == "decrypt":
        decrypt(message, shift)
    else:
        print("Wrong command")

Ceaser()
    