import random

def get_ranks():
    return ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def get_suits():
    return ["Spades", "Clubs", "Hearts", "Diamonds"]

def generate_deck(ranks, suits):
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit, None])
    return deck

def assign_values(deck):
    for card in deck:
        if card[0].isdigit():
            card[2] = int(card[0])
        elif card[0] in ["Jack", "Queen", "King"]:
            card[2] = 10
        elif card[0] == "Ace":
            card[2] = [1, 11]

def shuffle(deck):
    random.shuffle(deck)
    return(deck)

def main():
    ranks = get_ranks()
    suits = get_suits()
    deck = generate_deck(ranks, suits)
    assign_values(deck)
    shuffle(deck)
    return deck

if __name__ == "__main__":
    main()
