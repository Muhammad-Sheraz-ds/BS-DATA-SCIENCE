import random
def snake_lader_game():
    ladder1_start = random.randint(0,99)
    ladder1_end = random.randint(0,99)
    while ladder1_end < ladder1_start:
        ladder1_start = random.randint(0,99)
        ladder1_end = random.randint(0,99)
    ladder2_start = random.randint(0,99)
    ladder2_end = random.randint(0,99)
    while ladder2_end < ladder2_start:
        ladder1_start = random.randint(0,99)
        ladder2_end = random.randint(0,99)
    ladder3_start = random.randint(0,99)
    ladder3_end = random.randint(0,99)
    while ladder3_end < ladder3_start:
        ladder3_start = random.randint(0,99)
        ladder3_end = random.randint(0,99)
    ladder4_start = random.randint(0,99)
    ladder4_end = random.randint(0,99)
    while ladder4_end < ladder4_start:
        ladder4_start = random.randint(0,99)
        ladder4_end = random.randint(0,99)

    snake1_start = random.randint(0,99)
    snake1_end = random.randint(0,99)
    while snake1_end>snake1_start:
        snake1_start = random.randint(0, 99)
        snake1_end = random.randint(0, 99)

    snake2_start = random.randint(0, 99)
    snake2_end = random.randint(0, 99)
    while snake2_end > snake2_start:
        snake2_start = random.randint(0, 99)
        snake2_end = random.randint(0, 99)

    snake2_start = random.randint(0, 99)
    snake2_end = random.randint(0, 99)
    while snake2_end > snake2_start:
        snake2_start = random.randint(0, 99)
        snake2_end = random.randint(0, 99)

    snake3_start = random.randint(0, 99)
    snake3_end = random.randint(0, 99)
    while snake3_end > snake3_start:
        snake3_start = random.randint(0, 99)
        snake3_end = random.randint(0, 99)

    snake4_start = random.randint(0, 99)
    snake4_end = random.randint(0, 99)
    while snake4_end > snake4_start:
        snake4_start = random.randint(0, 99)
        snake4_end = random.randint(0, 99)
    print(ladder1_start,ladder1_end)
    print(ladder2_start, ladder2_end)
    print(ladder3_start,ladder3_end)
    print(ladder4_start,ladder4_end)

    print(snake1_start,snake1_end)
    print(snake2_start,snake2_end)
    print(snake3_start,snake3_end)
    print(snake4_start,snake4_end)

    position = 0
    while position <=101:
        dice = random.randint(1,6)
        position += dice
        if position >= 101:
            break
        if position == ladder1_start:
            print('There is a ladder on cell',position,'piece has moved to cell',ladder1_end)
            position = ladder1_end
        elif position == ladder2_start:
            print('There is a ladder on cell',position,'piece has moved to cell',ladder2_end)
            position = ladder2_end
        elif position == ladder3_start:
            print('There is a ladder on cell',position,'piece has moved to cell',ladder3_end)
            position = ladder3_end
        elif position == ladder4_start:
            print('There is a ladder on cell',position,'piece has moved to cell',ladder4_end)
            position = ladder4_end
            break
        elif position== snake1_end:
            print('There is a ladder on cell',position,'piece has moved to cell',snake1_start)
            position = snake1_start
            break
        elif position== snake2_end:
            print('There is a ladder on cell',position,'piece has moved to cell',snake2_start)
            position = snake2_start

            break
        elif position== snake3_end:
            print('There is a ladder on cell',position,'piece has moved to cell',snake3_start)
            position = snake3_start
            break
        elif position== snake4_end:

            position = snake3_start
            position = snake4_start
        print('Dice has value',dice,'piece has moved to cell',position)

snake_lader_game()