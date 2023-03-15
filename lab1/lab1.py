import string
from collections import OrderedDict

def find_letter_pos(matrix,letter):
    wyn={}
    for i in matrix:
        for j in i:
            if j == letter:
                wyn['row']=matrix.index(i)
                wyn['col']=i.index(j)
                return matrix.index(i),i.index(j)

def remove_duplicates(text):
    unique_chars = {}
    for char in text:
        if char not in unique_chars:
            unique_chars[char] = True
    return ''.join(unique_chars.keys())

def encrypt(text,matrix):
    if len(text) % 2 == 1:
        text += "X"
    ciphertext = ""
    for i in range(0, len(text), 2):
        row1,col1=find_letter_pos(matrix,text[i])
        row2,col2=find_letter_pos(matrix,text[i+1])
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

def decrypt(text,matrix):
    detext = ""
    for i in range(0, len(text), 2):
        row1,col1=find_letter_pos(matrix,text[i])
        row2,col2=find_letter_pos(matrix,text[i+1])
        if row1 == row2:
            detext += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            detext += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            detext += matrix[row1][col2] + matrix[row2][col1]

    return detext

key = "janeczek"
text = "Ala ma kota i pieska"

key = key.upper().replace(" ", "")
text = text.upper().replace(" ", "")
key = key.replace('J','I')
text = text.replace('J','I')
key=remove_duplicates(key)
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
for i in key:
    if i in alphabet:
        alphabet=alphabet.replace(i,'')
        
key += alphabet
matrix = [list(key[i:i+5]) for i in range(0, len(key), 5)]
print("Macierz")
for i in matrix:
    print(i)

ciphertext = encrypt(text,matrix)
print("Zaszyfrfowany teskt ",ciphertext)

detext = decrypt(ciphertext ,matrix)
print("Odszyfrowany teskt: ", detext)
