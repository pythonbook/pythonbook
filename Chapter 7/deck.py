import random
import math

class Deck(object):

    def __init__(self):
        self.reset()

    def reset(self):
        # 13 cards in each of 4 suits
        self.hist = [4]*13
        self.num_cards = 52

    def cards_left(self):
        return self.num_cards

    def draw_card(self):

        if self.num_cards == 0:
            print("No cards left to draw!")
            return
        
        # calculate CDF by summing
        # over all bins of the hist
        # from bin 0 to bin i
        CDF = [0]*13
        for i in range(len(self.hist)):
            for j in range(i+1):
                CDF[i] = CDF[i] + self.hist[j]

        card = 0

        # generate random number and
        # sample inverse CDF
        cum_prob = random.random()

        # scale to num cards
        cum_prob *= self.num_cards
        cum_prob = round(cum_prob)
        
        # lookup corresponding index
        for card in range(len(CDF)):
            if CDF[card] >= cum_prob:
                break               

        # update the historgram
        # we don’t need to update CDF here, it will
        # be done next time we call drawcard()
        self.hist[card] -= 1
        self.num_cards -= 1

        return card