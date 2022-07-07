'''
                = = = = = = = = = = = = = HAND CRICKET GAME = = = = = = = = = = = = = = = =
                ---------------------------------------------------------------------------
                This is the project based on an another very famous hand game that is widely
                played in schools during their class hours. It is known as 'HAND-CRICKET'.

                This is created by Vivek Kumar. You can surely use this for education
                purpose but beware If you get caught using it for commercially purpose
                then you have to face problems.

                YALA YOLO !!!
                ---------------------------------------------------------------------------

                PROJECT TITLE: HAND-CRICKET
                VERSION or DATE: v1.0 , 25-02-2020

'''

import random


def intro():
    intro_print = '''
    = = = = = = = = = = = = = HAND CRICKET GAME = = = = = = = = = = = = = = = =
    ---------------------------------------------------------------------------
    This is the project based on an another very famous hand game that is widely
    played in schools during their class hours. It is known as 'HAND-CRICKET'.

    This is created by Vivek Kumar. You can surely use this for education
    purpose but beware If you get caught using it for commercially purpose
    then you have to face problems.

    YALA YOLO !!!
    ---------------------------------------------------------------------------

    PROJECT TITLE: HAND-CRICKET
    VERSION or DATE: v1.0 , 25-02-2020

            '''
    print(intro_print)


def menu():
    print('''
    = = = = = = = = = = = = = MAIN MENU = = = = = = = = = = = = = =

    . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . .
    . . . . . . . ________________________________ . . . . . . . .
    . . . . . . |                                  | . . . . . . .
    . . . . . . |   PRESS 'S' TO START THE GAME    | . . . . . . .
    . . . . . . |                                  | . . . . . . .
    . . . . . . |   PRESS 'H' TO GET THE HELP      | . . . . . . .
    . . . . . . |                                  | . . . . . . .
    . . . . . . |   PRESS 'Q' TO QUIT THE GAME     | . . . . . . .
    . . . . . . | ________________________________ | . . . . . . .
    . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . .

    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    ''')

    k = input('Enter here --> ')
    k = k.upper()

    if k == 'S':
        game()

    elif k == 'H':

        print('''
            = = = = = = = = = = =   HELP   = = = = = = = = = = =

            You just have to enter any number between 1 to 6
            (including them) and they will get added as your runs
            in the game.
            But if your entered number gets matched with the Computer
            then you will get out.

            For more knowledge, explore the game !!!

        \n\n''')

        game()

    elif k == 'Q':
        print('Thanks for using !!!')
        exit()

    else:
        print("Invalid input.\n\n")


def game():
    bat_count = 0
    bowl_count = 0

    runs = 0
    pc_runs = 0

    print('''
     = = = = = = = = = = =   GAME STARTED   = = = = = = = = = = =

                          - - Toss Time - -

              Choose between Odd and Even

              '1' for Even

              '0' for Odd

    ''')

    toss_input = int(input("Enter here--> "))

    if toss_input != 0 and toss_input != 1:
        print("Invalid Input !!!")
        exit()

    print("ENTER ANY NUMBER BETWEEN 1 TO 6\n")
    user_input = int(input("Enter here--> "))
    pc_input = random.randint(1, 6)

    if user_input < 1 or user_input > 6:
        print("Invalid Input !!!")

    k = user_input + pc_input
    deci = 0
    toss_won = 0

    if k % 2 == 0:
        if toss_input ==  1:
            print("You won the toss :)")
            print('''
                   What do you want to do first Bat ot Bowl ?

                   Press '1' to Bat first or,
                   Press '0' to Bowl first

                   ''')
            deci = int(input("Enter here--> "))
            toss_won = 1

        else:
            print("You lose the toss :(")
            temp = random.randint(0,1)
            if temp == 1:
                print('Computer has chosen to Bat first.')
                runs = bat()
                pc_runs = bowl()
            else:
                print('Computer has chosen to Bowl first.')
                pc_runs = bowl()
                runs = bat()

    else:
        if toss_input ==  1:
            print("You won the toss :)")
            print('''
                   What do you want to do first Bat ot Bowl ?

                   Press '1' to Bat first or,
                   Press '0' to Bowl first

                   ''')
            deci = int(input("Enter here--> "))
            toss_won = 1

        else:
            print("You lose the toss :(")
            temp = random.randint(0,1)
            if temp == 1:
                print('Computer has chosen to Bat first.')
                runs = bat()
                pc_runs = bowl()
            else:
                print('Computer has chosen to Bowl first.')
                pc_runs = bowl()
                runs = bat()

        if toss_won == 1:
            if deci == 1:
                runs = bat()
                pc_runs = bowl()

            elif deci == 0:
                pc_runs = bowl()
                runs = bat()

            else:
                print("Invalid Input !!!")

    print('Your Runs = ', runs)
    print('Computer Runs = ', pc_runs)

    if pc_runs < runs:
        print(' YOU WON THE MATCH !!! ')
        print('''
             _________________________________________________________________
            |                                                                 |
            |    ....            ....      ............      ......      ...  |
            |    ....            ....    ................    ... ...     ...  |
            |    ....            ....    ...          ...    ...  ...    ...  |
            |    ....    ....    ....    ..            ..    ...   ...   ...  |
            |    ....    ....    ....    ...          ...    ...    ...  ...  |
            |    ....................    ................    ...     ... ...  |
            |      ................        ............      ...      ......  |
            | ________________________________________________________________|

        ''')
    elif pc_runs > runs:
        print(' YOU LOST THE MATCH !!! ')
        print('''
             __________________________________________________________________________________
            |                                                                                  |
            |    ....               ............        ................    ................   |
            |    ....             ................      ...           ..      ............     |
            |    ....             ...          ...      ...                       ...          |
            |    ....             ..            ..      ................          ...          |
            |    ....             ...          ...                   ...          ...          |
            |    ...........      ................      ..           ...          ...          |
            |    ...........        ............        ................           .           |
            | ________________________________________________________________________________ |

        ''')

    else:
        print('Match Draw !!!')


def bat():
    runs = 0

    wish_good = ['Yoho', 'Nice Shot', 'Keep it up', 'You are awesome', 'Osm Shot']
    wish_bad = ['OOPS', 'That was bad shot', 'Better luck next time', 'You are out', 'Bad luck']
    wish_boundary = ['Nice Boundary', 'Going right towards boundary ', 'OP', 'You are killing it', 'Nice Shot']

    l = random.randint(0, 4)

    print('\n\n\n\n\n')
    print('= = = = = = = = = =  BATING TIME = = = = = = = = = =')
    print('* Input any number between 1 to 6')
    print('* If your number gets matched with computer then you are out. ')
    print('* Press Q to Quit\n')

    user = ''

    while user != 'Q':
        user = int(input('\nEnter here -> '))

        pc = random.randint(1, 6)

        if user < 1 or user > 6:
            print('Invalid Input !!!')

        elif user == 'Q':
            end()

        elif user > 0 or user < 7:
            if user == pc:
                print("\n\nY O U  --> ", user , "\t\t\t", pc," <-- C O M P U T E R ")
                print("\n= = = = = = = = = = O U T = = = = = = = = = = ")
                print("\n\t\t", wish_bad[l])
                print("\n\t\tTotal Runs --> ", runs)
                break

            elif user == 4 or user == 6:
                runs += user
                print("\n\nY O U  --> ", user , "\t\t\t", pc," <-- C O M P U T E R ")
                print('\n\t\t', wish_boundary[l])
                print("\t\tTotal Runs --> ", runs)

            else:
                runs += user
                print("\n\nY O U  --> ", user , "\t\t\t", pc," <-- C O M P U T E R ")
                print('\n\t\t', wish_good[l])
                print("Total Runs --> ", runs)
    return runs


def bowl():
    pc_runs = 0

    print('\n\n\n\n\n')
    print('= = = = = = = = = =  BOWLING TIME = = = = = = = = = =')
    print('* Input any number between 1 to 6')
    print('* If your number gets matched with computer then you will get 1 wicket. ')
    print('* Press Q to Quit\n')

    user = ''

    while user != 'Q':
        user = int(input('\nEnter here -> '))

        pc = random.randint(1, 6)

        if user < 1 or user > 6:
            print('Invalid Input !!!')

        elif user == 'Q':
            end()

        elif user > 0 or user < 7:
            if user == pc:
                print("\n\nY O U  --> ", user , "\t\t\t", pc," <-- C O M P U T E R ")
                print("\n\t\t= = = = = OUT = = = = = ")
                print("\n\t\tYou Got the Wicket")
                break

            elif user != pc:
                pc_runs += pc
                print("\n\nY O U  --> ", user , "\t\t\t", pc," <-- C O M P U T E R ")
                print("\t\tTotal Computer runs --> ", pc_runs)

    return pc_runs


def end():

    print('\n\nI hope you have enjoyed this game !!!')
    exit()

intro()
menu()

print('\n\t- Vivek Kumar')
