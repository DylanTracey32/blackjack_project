import game_logic
import db

def title():
    print("BLACKJACK!\n"
          "Blackjack payout is 3:2\n")

def main():
    title()
    db.starting_balance() # Initializes starting balance if it isn't found
    
    while True:
        balance = db.read_balance()
        while True:
            if balance < 5:
                print(f"Money: {balance}")
                balance = db.buy_chips(balance)
                print()
            else:
                break
        game_logic.show_balance(balance)

        balance = game_logic.play_round(balance)

        replay = input("Play again? (y/n): ").lower()
        print()
        if replay != "y":
            print("Come back soon!\n"
                  "Bye!")
            break

if __name__ == '__main__':
    main()