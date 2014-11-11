import random

class Deck(object):

    def __init__(self):
        self.reset()

    def reset(self):
        # 13 cards in each of 4 suits
        self.hist = random.sample(range(1,53),52)
        self.num_cards = 52

    def cards_left(self):
        return self.num_cards

    def draw_card(self):

        if self.num_cards == 0:
            print("No cards left to draw!")
            return
        
        self.num_cards -= 1

        return self.hist[self.num_cards-1] % 13