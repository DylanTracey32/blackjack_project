import deck
import db
    

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

def display_cards(hand):
    for card in hand:
        print(f"{card[0]} of {card[1]}")


def outcome(scenario, bet):
    if scenario == "blackjack":
        print("\nYou got blackjack!\n")
        db.outcome("blackjack", bet) 
    elif scenario == "player":
        print(f"\nCongratulations, you win {bet} chips!")
        db.outcome("player", bet)
    elif scenario == "dealer":
        print("\nSorry. You lose.")
        db.outcome("dealer", bet)
    elif scenario == "push":
        print("\nTie game! your bet was returned.")
        db.outcome("push", bet)
    show_balance(db.read_balance())
    print()

def player_gameplay(player_hand):
    while True:
        choice = input("Hit or stand? (hit/stand): ").lower()
        if choice == "hit":
            player_hand.append(deal_card())
            print("\nYOUR CARDS:")
            display_cards(player_hand)
            print()
            player_value = check_value(player_hand)
            if player_value > 21:
                return "dealer", player_value # Called in play_round(balance)
        elif choice == "stand":
            return "player", check_value(player_hand)
        else:
            print("Please enter either hit or stand!\n")


def dealer_gameplay(dealer_hand):
    while True:
        dealer_value = check_value(dealer_hand)
        if dealer_value < 17:
            dealer_hand.append(deal_card())
        else:
            return dealer_value

def display_points(player_value, dealer_value):
    print(f"\nYOUR POINTS:     {player_value}\n"
          f"DEALER'S POINTS: {dealer_value}")

def play_round(balance): # Primary function for game operation
    player_hand = []
    dealer_hand = []

    bet = input_bet(balance)
    #reset_cards(player_hand, dealer_hand) # Resets cards for after first round
    starting_hand(player_hand, dealer_hand) # Assigns starting hand without showing user

    print("\nDEALER'S SHOW CARD:")
    display_show_card(dealer_hand)
    print("YOUR CARDS:")
    display_cards(player_hand)
    print()
    player_value = check_value(player_hand)
    if player_value == 21:
        outcome("blackjack", bet)
        return db.read_balance()
    
    scenario, player_value = player_gameplay(player_hand)

    if scenario == "dealer":
        outcome("dealer", bet)
        return db.read_balance()
    
    print("\nDEALER'S CARDS:")
    dealer_value = dealer_gameplay(dealer_hand)
    display_cards(dealer_hand)

    display_points(player_value, dealer_value)

    if dealer_value > 21 or dealer_value < player_value:
        outcome("player", bet)
    elif dealer_value > player_value:
        outcome("dealer", bet)
    else:
        outcome("push", bet)

    return db.read_balance()