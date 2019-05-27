#!/usr/bin/python

secret_code = 'VICTORY'
clear_text  = 'ID TECH'

def encode(s, c):
    """
    s is the scret code
    c is the clear text
    """
    secret_code_list = list(s)
    clear_text_list  = list(c)

    encoded_text_list= []
    count = 0
    for letter in clear_text_list:
        if letter == ' ':
            encoded_text_list.append(' ')
            continue
        encoded_letter = (ord(secret_code_list[count]) - ord('A') +
                          ord(letter) - ord('A')) % 26 + ord('A')
        encoded_letter = chr(encoded_letter)
        count = (count + 1 ) % (len(secret_code_list))
        encoded_text_list.append(encoded_letter)

    encoded = ''.join(encoded_text_list)
    return encoded

def decode(s, e):
    """
    s is the scret code
    e is the encoded text
    """
    secret_code_list   = list(s)
    encoded_text_list  = list(e)
    decoded_text_list  = []
    count = 0
    for letter in encoded_text_list:
        if letter == ' ':
            decoded_text_list.append(' ')
            continue
        decoded_letter = (ord(letter) - ord(secret_code_list[count]) ) % 26 + ord('A')
        decoded_letter = chr(decoded_letter)
        count = (count + 1 ) % (len(secret_code_list))
        decoded_text_list.append(decoded_letter)

    decoded = ''.join(decoded_text_list)
    return decoded

encoded_text = encode(secret_code, clear_text)
decoded_text = decode(secret_code, encoded_text)

print 'secret code:     ', secret_code
print 'clear text:      ', clear_text
print 'encoded text:    ', encoded_text
print 'decoded text:    ', decoded_text
