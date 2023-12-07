rows=int(input("enter number of rows"))
cols=int(input("enter number of columns"))
position=input("enter the position")
rows_list=[]
cols_list=[]
map=[]
#for i in range(rows):
  #  for j in range(cols):
#       map.append(i)
   # map.append(i)
#print(map)
#print(cols_list)
map=[[0]*cols]*rows
print(map)
char_position=position[0].lower()
alphabets=["a","b","c","d","e","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
char_index=alphabets.index(char_position)
print(char_index)
num_position=int(position[1])-1
print(num_position)
map[num_position][char_index]="x"
print(map)