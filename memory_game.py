import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# height = 4
width = 5


def random_char(height, width):

    temp_list = [x for x in alphabet if alphabet.index(
        x) < int((height * width)/2)]
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


def display_board(board):
    num_rows = len(board)
    num_cols = len(board[0])
    # display_main_board
    print()
    print("      ", end="")
    for i in range(num_cols):
        print(chr(ord('A') + i) + "   ", end="")
    print()

    print("     " + "-"*(num_cols*4 - 1))
    # display_rows
    for i in range(num_rows):
        print(i+1, end="   | ")
        for j in range(num_cols):
            print(board[i][j], end=" | ")
        print()
    print()


def get_hash_board(height, width):
    hash_board = []
    for i in range(height):
        hash_board.append([])
        for j in range(width):
            hash_board[i].append("#")
    print(hash_board)
    return hash_board


def crd_in_hash_board(hash_board, board, crd):
    x, y = crd
    hash_board[x][y] = board[x][y]


def get_level():
    print('''
           Select the difficulty level:
           Easy (5x4)   - 1
           Medium (5x6) - 2
           Hard (5x10)  - 3
           ''')
    while True:
        level = input("Choose option [1-3]")
        levels = [4, 6, 10]
        if int(level) not in [1, 2, 3]:
            print("condition = ", level not in [1, 2, 3])
            print("level = ", level)
            print("There is no such level")
            continue
        break
    height = levels[int(level)-1]
    return height


def get_coordinates(board):
    crd = input("Enter coordinates")
    crd_alpha, crd_num = crd
    # crd_num = int(crd_num)
    if len(crd) != 2 or not crd_alpha.isalpha() or not crd_num.isnumeric():
        print(len(crd) != 2)
        print(not crd_alpha.isalpha())
        print(crd_num.isnumeric())
        print("Please enter valid data")
    elif int(crd_num) > len(board) or crd_alpha not in alphabet[0:5]:
        print("Data out of range")
    else:
        return [crd_alpha, int(crd_num)-1]


def convert_crd(crd):
    dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
            "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}
    return [dict.get(crd[0]), crd[1]]


# def get_welcome_message():
#     print("Welcome to the Memory Game!" / n)


def main():
    height = get_level()
    board = generate_board(height, width)
    hash_board = get_hash_board(height, width)
    display_board(board)
    display_board(get_hash_board(height, width))
    crd = convert_crd(get_coordinates(board))
    crd_in_hash_board(hash_board, board, crd)
    display_board(hash_board)


if __name__ == "__main__":
    main()

# uwagi Sławka
# tablica 3x4 -> 12 komórek -> 6 liter // tworzymy generate board pomocnicza lista / wycinamy ile liteer
# uzupełnianie
# pop
