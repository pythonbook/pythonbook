import deck

card_val = [2,3,4,5,6,7,8,9,10,10,10,10,11]

def calc_hand_val(hand):
    # sort hand of cards so we treat aces last
    hand.sort()

    # add up all values until aces
    # are encountered; then add them
    # as either 11 or 1 depending on
    # current value of hand
    value = 0
    for i in range(len(hand)):
        # not an ace (index 12)
        if hand[i] != 12:
            value += card_val[hand[i]]
        else:
            if value > 10:
                value += 1
            else:
                value += 11
    return value

def blackjack():

    # init deck of cards
    cards = deck.Deck()

    # Dealer and player draw two cards
    dealer = []
    player = []

    # The first dealer card is facing
    # up, so we'll call this upcard
    upcard = cards.draw_card()
    
    dealer.append(upcard)
    dealer.append(cards.draw_card())

    player.append(cards.draw_card())
    player.append(cards.draw_card())

    # Strategy: we only see one of the
    # dealer's cards, if it is 2 or 3, we
    # hit until we reach 13.  If it is 4, 5
    # or 6, we hit until we reach 12.  If
    # it is 7 or higher, we hit until 17
    upcard_val = card_val[upcard]
    
    threshold = 17
    if upcard_val <= 3:
        threshold = 13
    elif upcard_val <= 6:
        threshold = 12

    # Draw cards until threshold is reached
    while calc_hand_val(player) < threshold:
        player.append(cards.draw_card())

    # check to see if we busted
    if calc_hand_val(player) > 21:
        return False

    # At this point the dealer will either
    # stand on 17 or higher, or draw on 16
    # or lower (house rules)
    while calc_hand_val(dealer) < 17:
        dealer.append(cards.draw_card())

    # check to see if dealer busted
    # in which case we won
    if calc_hand_val(dealer) > 21:
        return True

    # neither player busts, who has
    # the higher value?
    return (calc_hand_val(player) >
           calc_hand_val(dealer))

def blackjack_win_prob(N):
    wins = 0
    
    for i in range(N):
        if blackjack():
            wins += 1

    return wins/N
