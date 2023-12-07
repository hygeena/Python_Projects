''' 
    1. Accept n and m
    2. Validate n and m
    3. Construct map
    4. Accept position
    5. Decode position and mark on map
    6. Display map 
'''

rows=int(input("enter number of rows"))
cols=int(input("enter number of columns"))
if rows>1000:
    print("rows should be less than or equal to 1000")
elif cols>26:
    print("coulmns should be less than or equal to 26")
else:
    position=input("enter the position")
    map=[]
    for i in range(rows):
        temp_list=[]
        temp_list=[[0]*cols]
        map.append(temp_list)
    #map=[[0]*cols]*rows
    print(map)
    char_position=position[0].lower()
    alphabets=["a","b","c","d","e","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    char_index=alphabets.index(char_position)
    print(char_index)
    num_position=int(position[1])-1
    print(num_position)
    map[num_position][char_index]="x"
    print(map)
    
