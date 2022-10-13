import random
SUITS = ['♠️', '♥️', '♣️', '♦️']
RANK_VALUE = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player = Player()
        self.dealer = Dealer()
        self.deal_card(self.player)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.dealer)

        print("\nPlayer's cards: ")
        for card in self.player.hand:
            print(card)
        print(f"This hand is worth: {self.calculate_hand(self.player)}")
        print("\nDealer's cards: ")
        print(f"{self.dealer.hand[0]}")
        print("???")
        self.player_acts()
        

    def deal_card(self, person):
        card = self.deck.cards.pop()
        person.hand.append(card)

    def calculate_hand(self, person):
        total_points = 0
        for card in person.hand:
            total_points += card.value
        return total_points
    
    def player_acts(self):
        if self.calculate_hand(self.player) == 21:
            print("Blackjack! You win!")
        elif self.calculate_hand(self.player) < 21:
            print("\nWould you like to hit or stay?")
            response = input("Enter (h) for hit or (s) for stay: ")
            if response == "h":
                self.deal_card(self.player)
                for card in self.player.hand:
                    print(card)
                print(f"This hand is now worth: {self.calculate_hand(self.player)}")
                self.player_acts()
            if response == "s":
                self.dealer_acts()
        elif self.calculate_hand(self.player) > 21:
            print("Bust!")

    def dealer_acts(self):
        print(" ")
        if self.calculate_hand(self.dealer) == 21:
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            print("Dealer has blackjack!")
        elif self.calculate_hand(self.dealer) < 17:
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            self.deal_card(self.dealer)
            print(f"Dealer hits! {self.dealer.hand[-1]}")      
            self.dealer_acts()
        elif self.calculate_hand(self.dealer) > 21:
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            print("Dealer bust!")
        else:
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            print(f"Dealer stays with a hand worth: {self.calculate_hand(self.dealer)}")


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank_value in RANK_VALUE.items():
                new_card = Card(suit, rank_value[0], rank_value[1])
                self.cards.append(new_card)
    def shuffle_deck(self):
        random.shuffle(self.cards)

        
class Player:
    def __init__(self):
        self.hand = []
        pass
    
class Dealer:
    def __init__(self):
        self.hand = []
        pass
    
new_game = Game()

    
