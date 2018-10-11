import random


def draw_card():
    """
    This function draws a random card from 1-10.
    :return:
    """
    return random.randint(1, 10)


def dealer_cards():
    """
    This function draws the dealers cards and prints what the dealer drew
    :return:
    """
    card4 = draw_card()
    card5 = draw_card()
    draw_card()
    print("The dealer drew a", card4)
    draw_card()
    print("The dealer also drew a", card5)
    print("The dealers total is", card4 + card5)
    return card4 + card5


def win(player, dealer):
    """
    This function defines a win or loss by saying if the players value is more, they win
    :param player:
    :param dealer:
    :return:
    """
    if player > dealer:
        print("You have won!")
    elif dealer > player:
        print("The dealer has won")
    else:
        print("Its a tie")


def main():
    card1=s=draw_card()
    card2=draw_card()
    card3=draw_card()
    total = card1 + card2
    draw_card()
    print("You drew a", card1)
    draw_card()
    print("You drew a", card2)
    print(card1 + card2)
    print("Your total is", total)
    hit_or_stay = input("Would you like to hit or stay?")
    if hit_or_stay == "hit":
        draw_card()
        print("You drew a", card3)
        print(card1 + card2 + card3)
        total = total + card3
        print("Your new total is", total)
    if total > 21:
        print("Sorry you loose")

    else:
        dealer = dealer_cards()
        win(total, dealer)


main()








