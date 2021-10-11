
import random
suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
    'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.rank + 'of' + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    pass


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cars(self, new_cards):
        if isinstance(new_cards, list):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            # For a single card object

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


player_one = Player('One')
player_two = Player('Two')
new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cars(new_deck.deal_one())
    player_two.add_cars(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two wins !')

    if len(player_one.all_cards) == 0:
        print('Player Two, out of cards! Player One wins !')
        game_on = False
        break

# Start a new round

player_one_cards = [player_one.remove_one()]

player_two_cards = [player_two.remove_one()]