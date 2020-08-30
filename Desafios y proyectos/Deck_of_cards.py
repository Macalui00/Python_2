from random import shuffle

# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def __repr__(self): 
        return f"{self.value} of {self.suit}"

# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck.

class Deck:
    def __init__(self):
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cartas = [Card(suit,value) for suit in suits for value in values]
        
    def count(self):
        return len(self.cartas)

    def __repr__(self):
        return f"El mazo actualmente posee {self.count()} cartas"

    def _deal(self,num):
        contador = self.count
        cantActual = contador - num
        cartas = []
        if contador == 0:
            raise ValueError("El mazo esta vacío")
        while cantActual > 0:
            cartas.push(self.cartas.pop())
        return cartas

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Solo mazos completos pueden ser mezclados")
        shuffle(self.cartas)
        return self
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()
        