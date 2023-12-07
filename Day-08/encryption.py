# word=input("enter your word to encrypt")
# shift=int(input("enter shift position"))
# process=input("")
# alphabets=["a","b","c","d","e","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# def encrypt(word,position):
#     cipher_text=""
#     for letter in word:
#         position=alphabets.index(letter)
#         new_position=position+shift
#         new_letter=alphabets[new_position]
#         cipher_text+=new_letter
#     print(cipher_text)
# encrypt(word,shift)

word=input("enter the word")
shift=int(input("enter the number"))
code=input("encode or decode")
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encrypt(word,shift):
    cipher_text=""
    for letter in word:
        # position=alphabets.index(letter)
        position=ord(letter)-ord('a')
        print(position)
        if position>=25:
            position=position-25
            print(position)
        # print(position)
        if code=="encode":
            new_position=position+shift         
        elif code=="decode":
            new_position=position-shift
        new_letter=alphabets[new_position]
        cipher_text+=new_letter
    print(cipher_text)
encrypt(word,shift)
