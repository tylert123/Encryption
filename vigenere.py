from helpers import alphabet_position, rotate_character,rot_alphabet_position_upper,rot_alphabet_position_lower

def encrypt(text, key):
    encrypted = ''
    num = 0
    num1 = 0
    keypos = []
    for letter in range(len(key)):
        letter = key[num]
        keypos.append(alphabet_position(letter))
        num = num + 1

    num = 0
        
    for letter in range(len(text)):
        letter = text[num]
        if letter.isalpha():
            encryptedChar = rotate_character(letter,keypos[num1])
            encrypted = encrypted + encryptedChar
            num = num + 1
            num1 = (num1 + 1) % len(key)
            
        else:
            num = num + 1
            encrypted = encrypted + letter
            continue
        
    #for letter in range(len(text)):
    #    letter = text[num]
    #    encryptedChar = rotate_character(letter, key)
    #    encrypted = encrypted + encryptedChar
    #    num = num + 1
    return(encrypted)

def main():

    from sys import argv, exit

    if len(argv) <= 1:
        text = str(input('Please enter the message you would like to encrypt:'))
        key = str(input('Encryption key:'))
        print(encrypt(text,key))

    else:
        if argv[1].isalpha():
            text = str(input('Please enter the message you would like to encrypt:'))
            key = str(argv[1])
            print(encrypt(text,key))
        else:
            print('Please enter a keyword containing only alphabetic characters!')
            exit()
            

    #text = "The crow flies at midnight!"
    #key = 'boom'
    #print(encrypt(text,key))

if __name__ == "__main__":
    main()