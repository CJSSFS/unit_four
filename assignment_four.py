import random


def draw_card():
    return random.randint(1, 10)


def dealer_cards():
    value4=draw_card()
    value5=draw_card()
    draw_card()
    print("The dealer drew a", value4)
    draw_card()
    print("The dealer also drew a", value5)




def hit():
    return hit()


def main():
    card1=draw_card()
    card2=draw_card()
    card3=draw_card()
    draw_card()
    print("You drew a", card1)
    draw_card()
    print("You drew a", card2)
    print("Would you like to hit or stay?")
    if hit input()