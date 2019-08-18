def alphabet_position(letter):

    if letter.isupper() == True:
        upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        return(upper.index(letter))
        
    else:   
        lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        return(lower.index(letter))

def rot_alphabet_position_upper(num):
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return(upper[num])

def rot_alphabet_position_lower(num):
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return(lower[num])

def rotate_character(char, rot):

    if char.isalpha() == False:
        return(char)

    charPosition = alphabet_position(char)
    charRot = charPosition + rot

    if char.isupper() == True:

        if charRot <= 12:
            position = rot_alphabet_position_upper(charRot)
            return(position)

        if charRot > 12:
            charRot = charRot%26
            position = rot_alphabet_position_upper(charRot)
            return(position)
    else:
        if charRot <= 12:
            position = rot_alphabet_position_lower(charRot)
            return(position)

        if charRot > 12:
            charRot = charRot%26
            position = rot_alphabet_position_lower(charRot)
            return(position)