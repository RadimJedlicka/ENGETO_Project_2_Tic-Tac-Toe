playground = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
empty_playground = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
separator = '+---+---+---+'


def print_playground():
    for _ in empty_playground:
        print(separator)
        print(f"| {' | '. join(empty_playground[:3])} |")
        print(separator)
        print(f"| {' | '. join(empty_playground[3:6])} |")
        print(separator)
        print(f"| {' | '. join(empty_playground[6:])} |")
        print(separator)
        break


def main():
    print_playground()
    prepinac = True
    control_list = []
    control_list_o = set()
    control_list_x = set()
    while ' ' in empty_playground and prepinac:
        guess = is_input_suitable(enter='Player O | Please enter your move number: ')
        if control_list_o == upperrow:
            prepinac = False
        for index, symbol in enumerate(playground):
            if symbol == guess:
                if guess in control_list:
                    print('already taken')
                else:
                    empty_playground[index] = 'O'
                    print_playground()
                    control_list.append(guess)
                    control_list_o.add(guess)
        if ' ' not in empty_playground:
            print('Tied')

            break
        if control_list_o == upperrow or control_list_o == midrow or control_list_o == lowrow\
                or control_list_o == leftcol or control_list_o == midcol or control_list_o == rightcol\
                or control_list_o == diag1 or control_list_o == diag2:
            print('Player O won')
            break
        guess = is_input_suitable(enter='Player X | Please enter your move number: ')
        for index, symbol in enumerate(playground):
            if symbol == guess:
                if guess in control_list:
                    print('already taken')

                else:
                    empty_playground[index] = 'X'
                    print_playground()
                    control_list.append(guess)
                    control_list_x.add(guess)
        if ' ' not in empty_playground:
            print('Tied')
            break
        if control_list_x == upperrow or control_list_x == midrow or control_list_x == lowrow \
                or control_list_x == leftcol or control_list_x == midcol or control_list_x == rightcol \
                or control_list_x == diag1 or control_list_x == diag2:
            print('Player X won')
            break
    else:
        print('Tied')


upperrow = {'7', '8', '9'}
midrow = {'4', '5', '6'}
lowrow = {'1', '2', '3'}
leftcol = {'7', '4', '1'}
midcol = {'8', '5', '2'}
rightcol = {'9', '6', '3'}
diag1 = {'1', '5', '9'}
diag2 = {'7', '5', '3'}


def field_taken(guess, control_list):
    return guess not in control_list


def is_input_suitable(enter):
    while True:
        guess = (input(enter))
        if input_control(guess):
            return guess
        else:
            print(f'!!! Wrong input !!!'.upper(), '\n'
                  f'Must be number between 1-9')


def input_control(guess) -> bool:
    return guess.isdigit() and guess in playground


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


intro()
main()
