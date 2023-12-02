def sequence(card1,card2,card3):
    if abs(card1-card2) == 1 and abs(card3-card2)==1:
        return True
    return False

def same_type(card1,card2,card3):
    if card1 == card2==card3:
        return True
    return False

def two_same_type(card1,card2,card3):
    if card1 == card2 or card2==card3 or card1==card3:
        return True
    return False

def differnt_cards(card1,card2,card3):
    if card1==card2 or card1==card3 or card2==card3:
        return False
    return True

def sum_of_cards(card1,card2,card3):
    return card1+card2+card3

def two_cards_sequence(card1,card2,card3):
    if abs(card1-card2)==1 or abs(card1-card3)==1 or abs(card2-card3)==1:
        return True
    return False

import random
def main():
    p1card1 = random.randint(1, 13)
    p1card2 = random.randint(1, 13)
    p1card3 = random.randint(1, 13)

    while p1card1 == p1card2 or p1card2 == p1card3 or p1card1 == p1card3:
        p1card1 = random.randint(1, 13)
        p1card2 = random.randint(1, 13)
        p1card3 = random.randint(1, 13)
    p2card1 = random.randint(1, 13)
    p2card2 = random.randint(1, 13)
    p2card3 = random.randint(1, 13)

    while p2card1 ==(p1card1 or p1card2 or p2card3) or p2card2 ==(p1card1 or p1card2 or p2card3) or p2card3 ==(p1card1 or p1card2 or p2card3):
        p2card1 = random.randint(1, 13)
        p2card2 = random.randint(1, 13)
        p2card3 = random.randint(1, 13)

    deck = 'DHSC'
    p1card1_type = random.choice(deck)
    p1card2_type = random.choice(deck)
    p1card3_type = random.choice(deck)
    p2card1_type = random.choice(deck)
    p2card2_type = random.choice(deck)
    p2card3_type = random.choice(deck)

    if p1card1_type==p1card2_type==p1card3_type:
        if p1card2_type != p2card2_type or p2card1_type != p2card3_type or p2card2_type != p1card3_type:
            print('player 1 has won')
    elif p2card1_type == p2card2_type == p2card3_type:
        if p1card1_type != p1card2_type or p1card1_type != p1card3_type or p1card2_type != p1card3_type:
            print('player 1 has won')
    elif p1card1_type==p1card2_type==p1card3_type:
        if sequence(p1card1,p1card2,p1card3):
            print('player 1 has won')
        elif sequence(p2card1,p2card2,p2card3):
            print('player 2 has won')

    elif same_type(p1card1_type,p1card2_type,p1card3_type) == same_type(p2card1_type,p2card2_type,p2card3_type) and sequence(p1card1,p1card2,p1card3) == sequence(p2card1,p2card2,p2card3):
        if sum_of_cards(p1card1,p1card2,p1card3) > sum_of_cards(p2card1,p2card2,p2card3):
            print('player 1 has won')
        elif sum_of_cards(p1card1,p1card2,p1card3) < sum_of_cards(p2card1,p2card2,p2card3):
            print('player 2 has won')
        else:
            print('Match has drawn')
    elif two_same_type(p1card1_type,p1card2_type,p1card3_type):
        if differnt_cards(p2card1_type,p2card2_type,p2card3_type):
            print('player 2 has won')

    elif two_same_type(p2card1_type,p2card2_type,p2card3_type):
        if differnt_cards(p1card1_type,p1card2_type,p1card3_type):
            print('player 1 has won')

    elif two_cards_sequence(p1card1,p1card2,p1card3) == two_cards_sequence(p2card1,p2card2,p2card3)
main()

