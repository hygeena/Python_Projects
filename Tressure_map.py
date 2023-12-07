line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? (eg:A2)") # Where do you want to put the treasure?
char_position=position[0].lower()
abc=["a","b","c"]
char_index=abc.index(char_position)
num_position=int(position[1])-1
map[num_position][char_index]="X"
print(f"{line1}\n{line2}\n{line3}")