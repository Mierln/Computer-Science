import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
 
class Cards:
    
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks

    def __str__(self):
        return f"{self.ranks} of {self.suits}"

class Deck:

    def __init__(self):
        self.deck = []
        for a in suits:
            for b in ranks:
                self.deck.append(Cards(a, b))

    def __str__(self):
        deck_com = ""
        for card in self.deck:
            deck_com += '\n' + card.__str__()
        return("Deck:" + deck_com)
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0 
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.ranks]
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

class Chips:
    
    def __init__(self):
        self.total = 1000
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't more than",chips.total)
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("\nWould you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(dealer.cards[0])  
    print("\nPlayer's Hand:")
    for card in player_hand.cards:
        print(card)
    
def show_all(player,dealer):
    print("\nDealer's Hand:")
    for card in dealer_hand.cards:
        print(card)
    print("Dealer's Hand =", dealer.value)
    
    print("\nPlayer's Hand:")
    for card in player_hand.cards:
        print(card)
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

print("\n"*100)
print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11 (auto).\nStarting Balance: 1000\n')
deck = Deck()
for _ in range(30):
    deck.shuffle()
player_chips = Chips() 

while True:
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    take_bet(player_chips)
    
   
    show_some(player_hand,dealer_hand)
    
    while playing:
        
        hit_or_stand(deck,player_hand) 
    
        show_some(player_hand,dealer_hand)  
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    print("\nYour balance",player_chips.total)

    if player_chips.total == 0:
        print("YOU HAVE NO BALANCE LEFT")
        break
    
    new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break