import random


one = '''
1111
  11
  11
  11
111111 '''

two = '''
 2222
22  22
   22
  22
222222222 '''

three = '''
333333
    33
333333
    33
333333
'''

four = '''
44  44
44  44
444444
    44
    44  '''

five = '''
555555
55
555555
    55
55555  '''

six = '''
666666
66
666666
66  66
666666'''

seven = '''
777777
    77
    77
    77
    77 '''
eight = '''

888888
88  88
888888
88  88
888888  '''

nine = '''
999999
99  99
999999
    99
999999  '''

ten = '''

1111    00000000
  11    0      0
  11    0      0
  11    0      0
111111  00000000  '''

dummy1 = ''
dummy2 = ''

game_images = [dummy1, one, two, three, four, five, six, seven, eight, nine, ten, dummy2]


def game():

    is_game_continue = True

    if user_choice > 10 or user_choice <= 0:
        is_game_continue = False
        print("ENTER THE VALID SCORE ")

    else:
        is_game_continue = True
        print(game_images[user_choice])
        print("computer choice")
        print(game_images[computer_choice])

        if user_choice > computer_choice or user_choice < computer_choice:
            is_game_continue = True
            print(f"score={user_choice}")
            print(f"boweler guess={computer_choice}")
        else:
            is_game_continue = False
            print("BATTING PERSON OUT")


play = str(input("YOU WANT PLAY GAME yes OR no="))
user_choice = 0
if (play == "yes"):

    balls = int(input("HOE MANY BALLS WISE TO PLAY="))
    for over in range(balls):
        user_choice = int(input("ENTER YOU SCORE 1 to 10:"))
        computer_choice = random.randint(1, 10)
        game()

else:
    print("WHAT? DO YOU SAY! YOU CAN'T PALY CRICKET ")


