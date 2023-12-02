import random
def check_REPRESENTATION(number):
    if number == 1:
        return 'Ace'
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"
    elif number == 10:
        return "Ten"
    elif number == 11:
        return "Jack"
    elif number == 12:
        return "Queen"
    elif number == 13:
        return "King"

def print_card_type(card_type):
    if card_type == 'D':
        return 'Diamond'
    elif card_type == 'H':
        return'Heart'
    elif card_type == 'S':
        return 'Spade'
    elif card_type == 'C':
        return 'Club'
def check_color(card_type):
    if card_type =='D' or card_type =='H':
        return 'Red'
    else:
        return 'Black'

def deck():
    deck ='DHSC'
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    representation_no_card1 = random.randint(1,13)
    representation_no_card2 = random.randint(1, 13)
    color_of_card1 = check_color(card1)
    color_of_card2 = check_color(card2)
    if representation_no_card1 == representation_no_card2:
        print('both cards have same number')
    if color_of_card1 == color_of_card2:
        print('both cards have same color')
    if print_card_type(card1) == print_card_type(card2):
        print('both cards have same type')
    if abs(representation_no_card1 - representation_no_card2)==1:
        print('Cards are in sequence')
deck()


