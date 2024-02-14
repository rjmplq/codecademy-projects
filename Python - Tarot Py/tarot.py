from random import randint

class Card:
    def __init__(self, name, arcana="minor"):
        self.name = name
        self.arcana = arcana
        self.position = 'upright'
        self.meaning = {}

    def __repr__(self) -> str:
        return self.name
    
    def add_meaning(self, position, meaning):
        self.meaning[position] = meaning

    def get_meaning(self):
        if randint(0,1) == 0:
            self.position = 'reversed'
            return self.meaning[self.position]
        return self.meaning[self.position]

class Deck:
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        self.card_count = 0

    def add_cards(self, cards):
        if type(cards) is list:
            self.cards += cards
        else:
            self.cards.append(cards)
        self.card_count = len(self.cards)
    
    def shuffle_cards(self):
        self.cards.shuffle()

class Spread:
    def __init__(self, name, description, cards_needed=1):
        self.name = name
        self.description = description
        self.cards_needed = cards_needed
        self.placements = {}

    def add_placements(self, placements):
        for placement in placements:
            self.placements[placement] = ""

    def start_reading(self, deck):
        cards_for_spread = []

        print("The {} spread will {}".format(self.name, self.description))
        print("Shuffle the cards and choose {}.".format(self.cards_needed))
        print("Shuffling cards.")

        if type(deck) is Deck:
            deck.shuffle_cards()
        else:
            print("Oops, please provide a deck of cards.")

        while self.cards_needed != len(cards_for_spread):
            card_picked = deck.cards[randint(0,deck.card_count-1)]
            if card_picked not in cards_for_spread:
                cards_for_spread.append(card_picked)
        
        for placement in self.placements:
            for card in cards_for_spread:
                self.placements[placement] = card

        print("The cards have been selected.")
        print("I will now reveal your fate.")

        for placement, card in self.placements:
            meaning = card.get_meaning()
            print("Your {placement} is the {card} in {position} position. It speaks of {meaning}".format(placement=placement, card=card.name, position=card.position, meaning=meaning))


        
the_world = Card("The World","major")
the_world.add_meaning("upright", "fullfilment, harmony, completion")
the_world.add_meaning("reversed","incompletion, no closure")

judgment = Card("Judgment","major")
judgment.add_meaning("upright","reflection, reckoning")
judgment.add_meaning("reversed","lack of self-awareness,doubnt,self-loating")

the_tower = Card("The Tower","major")
the_tower.add_meaning("upright","sudden upheaval, broken pride, disaster")
the_tower.add_meaning("reversed","disaster avoided, delayed disaster, fear or suffering")

test_deck = Deck("Test Deck")
test_deck.add_cards([the_world, the_tower, judgment])

one_card_spread = Spread("One Card Spread", "A test spread")
one_card_spread.add_placements(["your answer"])

one_card_spread.start_reading(test_deck)