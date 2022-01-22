# Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně.
# Jde o hru pro dva hráče (příp. počítač).
#
# Program bude obsahovat:
# 1. Program pozdraví uživatele
# 2. Vypíše v krátkosti pravidla hry
# 3. Zobrazí hrací plochu
# 4. Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
# TODO 5. Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
# TODO 6. Pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní.
# TODO 7. Pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
# TODO 8. Jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy
# TODO 9. Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát.
#         Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
# TODO 10. Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.

playground = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
empty_playground = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
separator = '+---+---+---+'

def print_playground(separator, empty_playground):
    for _ in range(3):
        print(separator)
        print(f"| {' | '. join(empty_playground[:3])} |")
        print(separator)
        print(f"| {' | '. join(empty_playground[3:6])} |")
        print(separator)
        print(f"| {' | '. join(empty_playground[6:])} |")
        print(separator)
        break


# print_playground(separator, playground)


def main():
    print_playground(separator, empty_playground)

    while True:
        put_stone_O = input('Player O | Please enter your move number: ')
        for index, symbol in enumerate(playground):
            if symbol == put_stone_O:
                empty_playground[index] = 'O'
                print_playground(separator, empty_playground)

        put_stone_X = input('Player X | Please enter your move number: ')
        for index, symbol in enumerate(playground):
            if symbol == put_stone_X:
                empty_playground[index] = 'X'
                print_playground(separator, empty_playground)




# def is_input_suitable(enter='Player O | Please enter your move number: '):
#     while True:
#         guess = (input(enter))
#         if input_control(guess):
#             return guess
#         else:
#             print(f'!!! Wrong input !!!'.upper(), '\n'
#                   f'Must be number 1-9,')
#             print(separator)
#
#
# def input_control(guess) -> bool:
#     return guess.isdigit() and guess in positions.values()











def intro():
    print('''Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game'''
          )



# intro()
main()
