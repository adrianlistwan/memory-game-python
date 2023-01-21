import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
height = 4
width = 5
    
def random_char(height, width):
    
    temp_list = [x for x in alphabet if alphabet.index(x) < int((height * width)/2)]
    # duplicate list
    temp_list2 = temp_list * 2
    random.shuffle(temp_list2)
    
    return temp_list2


# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# generate_board(height, width)
# height -> rows
# width -> columns 
 
def generate_board(height, width):
    board = []
    temp_alphabet = random_char(height, width)
    # generate rows
    for i in range(height):
        row = []
        counter = i*width
        for j in range(width):
            row.append(temp_alphabet[counter])
            counter += 1          
        board.append(row)

    return board

def main():
    print(random_char(height,width))
    print("tablica poniżej")
    print(generate_board(height,width))


if __name__ == "__main__":
    main()

# uwagi Sławka
# tablica 3x4 -> 12 komórek -> 6 liter // tworzymy generate board pomocnicza lista / wycinamy ile liteer 
# uzupełnianie 
# pop 