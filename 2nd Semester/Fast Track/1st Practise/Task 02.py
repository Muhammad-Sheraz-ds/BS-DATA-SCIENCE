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

def deck():
    deck ='DHSC'
    card = random.choice(deck)
    representation_no = random.randint(1,13)
    check_REPRESENTATION(representation_no)
    print(check_REPRESENTATION(representation_no),'of',print_card_type(card))
deck()


