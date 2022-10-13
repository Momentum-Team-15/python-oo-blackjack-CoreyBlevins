import random
SUITS = ['♠️', '♥️', '♣️', '♦️']
RANK_VALUE = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.tally = 1
        self.start_game()

    def start_game(self):
        self.deck.cards.clear()
        self.deck.build_deck()
        self.player.hand.clear()
        self.dealer.hand.clear()
        self.deck.shuffle_deck()
        self.deal_card(self.player)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.dealer)
        print(f"Round: {self.tally}")
        print(f"Deck is {len(self.deck.cards)}")
        print("\nDealer's cards: ")
        print(f"{self.dealer.hand[0]}")
        print("???")
        print("\nPlayer's cards: ")
        for card in self.player.hand:
            print(card)
        print(f"This hand is worth: {self.calculate_hand(self.player)}")
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
        self.player_twenty_one = False
        if len(self.player.hand) == 2 and self.calculate_hand(self.player) == 21:
            print("\n *Blackjack! You win!*")
            self.continue_playing()
        elif len(self.player.hand) > 2 and self.calculate_hand(self.player) == 21:
            self.player_twenty_one = True
            print("You have 21!")
            self.dealer_acts()
            self.end_round_score()
            self.continue_playing()
        elif self.calculate_hand(self.player) < 21:
            self.hit_or_stay()
        elif self.calculate_hand(self.player) > 21:
            print("Bust!")
            self.continue_playing()

    def hit_or_stay(self):
        print("\nWould you like to hit or stay?")
        response = input("Enter (h) for hit or (s) for stay: ").lower()
        if response == "h":
            self.deal_card(self.player)
            for card in self.player.hand:
                print(card)
            print(f"Your hand is now worth: {self.calculate_hand(self.player)}")
            self.player_acts()
        elif response == "s":
            self.dealer_acts()
        else:
            self.hit_or_stay()

    def dealer_acts(self):
        print(" ")
        self.dealer_blackjack = False
        self.dealer_twenty_one = False
        self.dealer_bust = False
        if len(self.dealer.hand) == 2 and self.calculate_hand(self.dealer) == 21:
            self.dealer_blackjack = True
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            print("Dealer has blackjack!")
            self.end_round_score()
            self.continue_playing()
        elif len(self.dealer.hand) > 2 and self.calculate_hand(self.dealer) == 21:
            self.dealer_twenty_one = True
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            print("Dealer has 21!")
            self.end_round_score()
            self.continue_playing()
        elif self.calculate_hand(self.dealer) < 17:
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            self.deal_card(self.dealer)
            print(f"Dealer hits! {self.dealer.hand[-1]}")
            self.dealer_acts()
        elif self.calculate_hand(self.dealer) > 21:
            self.dealer_bust = True
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            print("Dealer bust!")
            self.end_round_score()
            self.continue_playing()
        else:
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand is worth: {self.calculate_hand(self.dealer)}")
            print(f"Dealer stays with a hand worth: {self.calculate_hand(self.dealer)}")
            self.end_round_score()
            self.continue_playing()

    def end_round_score(self):
        print(f"\n  Player hand value: {self.calculate_hand(self.player)}")
        print(f"  Dealer hand value: {self.calculate_hand(self.dealer)}")
        if self.dealer_blackjack is True:
            print("    *Dealer has blackjack!*")
        elif self.dealer_twenty_one is True and self.player_twenty_one is False:
            print("    Dealer has 21!")
        elif self.dealer_twenty_one is True and self.player_twenty_one is True:
            print("    Push")
        elif self.dealer_bust is True:
            print("    Dealer bust!")
        elif self.calculate_hand(self.player) > self.calculate_hand(self.dealer):
            print("    *Player wins!*")
        elif self.calculate_hand(self.player) == self.calculate_hand(self.dealer):
            print("    Push")
        else:
            print("    Dealer wins.")         

    def continue_playing(self):
        print("\nWould you like to keep playing?")
        play_response = input("Enter (y) for yes or (n) for no: ")
        if play_response == "y":
            self.tally += 1
            self.start_game()
        elif play_response == "n":
            exit()
        else:
            self.continue_playing()

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
    def build_deck(self):
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

Game()