import deck
import db

def title():
    print("BLACKJACK!\n"
          "Blackjack payout is 3:2\n")
    

def show_balance(balance):
    print(f"Money: {balance}")


def input_bet(balance):  # Returns a valid bet
    while True:
        bet_input = input("Bet amount: ").strip()
        
        try:
            bet = float(bet_input)
            if bet <= 0:
                print("Please enter a positive amount!")
            elif bet < 5:
                print("Minimum bet is 5!")
            elif bet > 1000:
                print("Maximum bet is 1,000!")
            elif bet > balance:
                print("Insufficient funds!")
            else:
                return bet
        except ValueError:
            print("Please enter a numeric value!")




def deal_card(): # Deals a card
    return deck.main()


def starting_hand(player_hand, dealer_hand): # Starting hand for player and dealer
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())


def check_value(hand): # Checks player or dealer's hand value
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


def display_show_card(dealer_hand):
    show_card = dealer_hand[0]
    print(f"{show_card[0]} of {show_card[1]}\n")
    if show_card[0] == "Ace":
        print("Dealer's hand value: 1/11\n")
    else:
        print(f"Dealer's hand value: {show_card[2]}\n")


def display_cards(hand):
    for card in hand:
        print(f"{card[0]} of {card[1]}")
    print()


def check_blackjack(player_value):
    if player_value == 21:
        return True
    else:
        return False
    

def player_gameplay(player_hand, player_value, bet):
    while True:
        choice = input("Hit or stand? (hit/stand): ").lower()
        if choice == "hit":
            player_hand.append(deal_card())
            print("\nYOUR CARDS:")
            display_cards(player_hand)
            player_value = check_value(player_hand)
            print(f"Your hand value: {player_value}\n")
            if check_bust(player_value) == True:
                db.outcome("dealer", bet)
                print("Sorry. You lose.")
                break
        elif choice == "stand":
            player_value = check_value(player_hand)
            return player_value
        else:
            print("Please enter either hit or stand!\n")


def dealer_gameplay(dealer_hand, dealer_value, bet):
    while True:
        dealer_value = check_value(dealer_hand)
        if dealer_value < 17:
            dealer_hand.append(deal_card())
        elif 22 > dealer_value <= 21:
            return dealer_value
        else:
            db.outcome("player", bet)
            print(f"Congratulations, you win {bet / 2} chips!")
        

def check_bust(hand_value):
    if hand_value > 21:
        return True
    

def main():
    player_hand = []
    dealer_hand = []

    title()
    db.starting_balance() # Initializes starting balance if it isn't found
    
    while True:
        balance = db.read_balance()
        show_balance(balance)
        bet = input_bet(balance)
        starting_hand(player_hand, dealer_hand) # Assigns starting hand without showing user
        player_value = check_value(player_hand)
        dealer_value = check_value(dealer_hand)
        print()
        print("DEALER'S SHOW CARD:")
        display_show_card(dealer_hand)
        print("YOUR CARDS:")
        display_cards(player_hand)
        print(f"Your hand value: {check_value(player_hand)}\n")
        if check_blackjack(player_value) == True:
            db.outcome("blackjack", bet)
            print("You got blackjack!\n")
        else:
            player_value = player_gameplay(player_hand, player_value, bet)
            dealer_value = dealer_gameplay(dealer_hand, dealer_value, bet)
            if dealer_value > player_value:
                db.outcome("dealer", bet)
                print("Sorry. You lose.")

            elif dealer_value < player_value:
                db.outcome("player", bet)
                print(f"Congratulations, you win {bet / 2} chips!")
            else:
                print("DEALER'S CARDS:\n")
                display_cards(dealer_hand)
                print("Push, your bet was returned.")

            replay = input("Play again? (y/n): ").lower()
            if replay != "y":
                print()
                print("Come back soon!\n"
                      "Bye!")
                break
            
                
if __name__ == "__main__":
    main()