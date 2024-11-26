WALLET = "money.txt"  # global variable for wallet file

def starting_balance():  # Gives player a starting balance of 100 chips
    try:
        return WALLET
    except FileNotFoundError:
        with open(WALLET, "w") as f:
            f.write(str(100.0))

def read_balance():  # Reads money.txt to get player's current balance
    with open(WALLET) as f:
        return float(f.read())

def _change_balance(new_balance):  # Changes player's balance (internal function)
    with open(WALLET, "w") as f:
        f.write(str(new_balance))

def outcome(outcome, bet):  # Updates balance based on game outcome
    current_balance = read_balance()
    
    if outcome == "dealer":  # Player loses bet
        new_balance = current_balance - bet
    elif outcome == "player":  # Player wins bet
        new_balance = current_balance + bet
    elif outcome == "blackjack":  # Player gets blackjack
        new_balance = current_balance + int(bet * 1.5)
    else:
        raise ValueError("Invalid outcome specified")
    
    _change_balance(new_balance)
