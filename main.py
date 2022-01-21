# Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně.
# Jde o hru pro dva hráče (příp. počítač).
#
# Program bude obsahovat:
# TODO 1. Program pozdraví uživatele
# TODO 2. Vypíše v krátkosti pravidla hry
# TODO 3. Zobrazí hrací plochu
# TODO 4. Zobrazí hrací plochu Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
# TODO 5. Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
# TODO 6. Pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní.
# TODO 7. Pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
# TODO 8. Jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy
# TODO 9. Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát.
#         Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
# TODO 10. Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.


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


def main():
    print('Lets go')


intro()
main()
