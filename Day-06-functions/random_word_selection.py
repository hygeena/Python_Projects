import random
# word_list=["annie","margaretta","rose"]
# chosen_word=random.choice(word_list)
# print(chosen_word)
# word=input("guess a letter").lower()
# for letter in chosen_word:
#     if letter==word:
#         print("right")
#     else:
#         print("wrong")

#program to replace the word with "_"

word_list=["camel","tiger","cheetah"]
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
print(chosen_word)
display=[]
for letter in chosen_word:
    display+="_"
print(display)
end_of_game=False
while not end_of_game:
    guess=input("guess your letter")
    for position in range(word_length):
        letter=chosen_word[position]
        print(f"current position:{position}\n Current letter: {letter} \n Guessed letter: {guess}")
        if letter==guess:
            display[position]=letter
print(display)
if "_" not in display:
    end_of_game=True
    print("You Win")
else:
    print("No match")
    