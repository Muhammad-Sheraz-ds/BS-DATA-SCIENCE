import random

def card_type(card_type):
    if card_type == 'D':
        return 'Diamond'
    elif card_type == 'H':
        return'Heart'
    elif card_type == 'S':
        return 'Spade'
    elif card_type == 'C':
        return 'Club'


def different_card():
    deck = 'DHSC'
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    card3 = random.choice(deck)
    while card1 == card2 or card2 == card3 or card1 == card3:
        card1 = random.choice(deck)
        card2 = random.choice(deck)
        card3 = random.choice(deck)
    print(f'card1: {card1} card2: {card2} card3: {card3}')



different_card()