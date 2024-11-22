import deck

def title():
    print("BLACKJACK!\n"
          "Blackjack payout is 3:2\n")
    
def show_balance(money):
    print(f"Money:")

def deal_card(game_deck): #deals a card
    return game_deck.pop()

def starting_hand(game_deck, player_hand, dealer_hand): # starting hand for player and dealer
    player_hand.append(deal_card(game_deck))
    dealer_hand.append(deal_card(game_deck))
    player_hand.append(deal_card(game_deck))
    dealer_hand.append(deal_card(game_deck))

def check_value(hand): # return player or dealer's hand
    hand_value = 0
    aces = 0

    for card in hand:
        if card[0].lower() == "ace":
            aces += 1
        else:
            hand_value += card[2]

    for card in range(aces):
        if hand_value + 11 <= 21:
            hand_value += 11
        else:
            hand_value += 1
    return hand_value

def win_check(player_value):
    if player_value == 21:
        return True
    else:
        return False

def main():
    game_deck = deck.main()
    player_hand = []
    dealer_hand = []
    turn = 0
    money = 0
    bet = 0

    while True:
        title()
        show_balance()
        starting_hand(game_deck, player_hand, dealer_hand)
        player_value = check_value(player_hand)
        dealer_value = check_value(dealer_hand)
        print("YOUR CARDS:")
        display_cards()
        if win_check(player_value) == True:
            bet *= 1.5
            money += bet
            print("You got blackjack!\n")
        else:


        
        
if __name__ == "__main__":
    main()