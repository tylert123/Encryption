from helpers import alphabet_position, rotate_character,rot_alphabet_position_upper,rot_alphabet_position_lower

def encrypt(text, rot):
    encrypted = ''
    num = 0
    for letter in range(len(text)):
        letter = text[num]
        encryptedChar = rotate_character(letter, rot)
        encrypted = encrypted + encryptedChar
        num = num + 1
    return(encrypted)

def main():
    from sys import argv, exit

    if len(argv) <= 1:
        text = str(input('Please enter the message you would like to encrypt:'))
        rotation = int(input('Rotate by:'))
        print(encrypt(text,rotation))

    else:
        if argv[1].isalpha:
            print('Please type a number!')
            exit()
        else:
            text = str(input('Please enter the message you would like to encrypt:'))
            rotation = int(argv[1])
            print(encrypt(text,rotation))
        
if __name__ == "__main__":
    main()