WALLET = "money.txt" # global variable for wallet file

def starting_balance(WALLET): # gives player a starting balance of 100 chips
    with open(WALLET, "w") as f:
        f.write(100)

def read_balance(WALLET): # read .txt file to get player's current balance
    with open(WALLET) as f:
        return int(f.read())
    
def change_balance(new_balance): # changes player balance
    with open(WALLET, "w") as f:
        f.write(new_balance)

def check_bet(bet_amount): # Confirms if players balance is sufficient for bet
    balance = read_balance()
    if bet_amount > balance:
        print("Please deposit more chips!")
        return False
    else:
        return True
    
def outcome(outcome, bet):
    if outcome == "dealer":
        bet = 0
        return bet
    elif outcome == "player":
        bet *= 2
        return bet
    elif outcome == "bj":
        bet *= 2.5
        return bet