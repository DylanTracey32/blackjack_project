# This module handles all wallet operations of "money.py".

import sys

WALLET = "money.txt"  # global variable for wallet file

def starting_balance():  # Gives player a starting balance of 100 chips
    try:
        with open(WALLET) as f:
            return WALLET
    except FileNotFoundError:
        with open(WALLET, "w") as f:
            f.write(str(100.0))

def read_balance():  # Reads money.txt to get player's current balance
    try:
        with open(WALLET) as f:
            return float(f.read())
    except FileNotFoundError:
        print("Unable to find wallet file!\n"
              "Shutting down program..")
        sys.exit(1)
        

def _change_balance(new_balance):  # Changes player's balance (internal function)
    with open(WALLET, "w") as f:
        f.write(f"{new_balance:.2f}")

def buy_chips(balance): 
    while True:
        chip_amount = input("Enter amount of chips to deposit (total must be over 5 chips): ").strip()
        try:
            chip_amount = round(float(chip_amount), 2)
            if chip_amount <= 0:
                print("Please enter a positive amount!")
            elif (chip_amount + balance) < 5:
                print("Please deposit enough to have 5 chips in your wallet!")
            else:    
                balance += chip_amount
                _change_balance(balance)
                print(f"\n{chip_amount} chips were deposited.")
                return balance
        except ValueError:
            print("Please enter a numeric value!")

    

def outcome(outcome, bet):  # Updates balance based on game outcome
    current_balance = read_balance()
    
    if outcome == "dealer":  # Player loses bet
        new_balance = current_balance - bet
    elif outcome == "player":  # Player wins bet
        new_balance = current_balance + bet
    elif outcome == "blackjack":  # Player gets blackjack
        new_balance = current_balance + int(bet * 1.5)
    elif outcome == "push": # tie game
        new_balance = current_balance
    else:
        raise ValueError("Invalid outcome specified")

    
    _change_balance(new_balance)
