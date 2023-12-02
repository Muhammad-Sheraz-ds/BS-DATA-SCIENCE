import random
def snake_lader_game():
    list = [0] * 100
    ladder1 = random.randint(0,99)
    ladder2 = random.randint(0,99)
    ladder3 = random.randint(0,99)
    ladder4 = random.randint(0,99)
    list[ladder1] = random.randint(ladder1,99)
    list[ladder2] = random.randint(ladder2,99)
    list[ladder3] = random.randint(ladder3,99)
    list[ladder4] = random.randint(ladder4,99)

    snake1 = random.randint(0,99)
    snake2 = random.randint(0,99)
    snake3 = random.randint(0,99)
    snake4 = random.randint(0,99)
    list[snake1] = random.randint(0,snake1)
    list[snake2] = random.randint(0,snake2)
    list[snake3] = random.randint(0,snake3)
    list[snake4] = random.randint(0,snake4)
    position = 0
    piece = 0
    while position < 100:
        dice = random.randint(1,7)
        position+=dice
        if list[position]> position and list[position]!=0:
            print('There is a ladder on cell', position, 'piece has moved to cell',list[position])
            position = list[position]
        elif list[position]< position and list[position]!=0:
            print('There is a Snake on cell',position,'piece has moved to cell',list[position])
            position = list[position]
        else:
            print('Dice has value', dice, 'piece has moved to cell', position)


snake_lader_game()