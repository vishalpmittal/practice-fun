import random

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
rank_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
    
    def __str__(self):
        return f'--> Deck: {len(self.cards)} cards\n' + ', '.join([str(card) for card in self.cards])
            
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        single_card = self.cards.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self,card):
        self.cards.append(card)

    def total(self):
        total = 0
        aces = 0
        for card in self.cards:
            if card.rank == 'A':
                    aces += 1
            else: 
                total+= rank_values[card.rank]

        for _ in range(aces):
            total = total + 1 if total >= 11 else total + 11
       
        return total

    def __str__(self):
        return 'Cards:  ' + ', '.join([str(card) for card in self.cards]) + ', Value: ' + str(self.total())


class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.dealer_hand = Hand()
        for _ in range(2):
            self.hit_dealer()

        self.player_hand = Hand()
        for _ in range(2):
            self.hit_player()

    def show_both_hands(self):
        return '--> Dealer\'s Hand: ' + str(self.dealer_hand) + '\n--> Player\'s Hand: ' + str(self.player_hand)

    def show_player_hand(self):
        return '--> Player\'s Hand: ' + str(self.player_hand)

    def __str__(self):
        return str(self.deck) + '\n' + str(self.show_both_hands())

    def hit_player(self):
        self.player_hand.add_card(self.deck.deal())

    def hit_dealer(self):
        self.dealer_hand.add_card(self.deck.deal())

    def check(self, prior_choice = 'h'):
        player_total = self.player_hand.total()
        dealer_total = self.dealer_hand.total()

        if player_total == 21:
            print('\n*** Congratulations! You got a Blackjack!')
            print(self.show_both_hands())
            return 'finish'

        elif dealer_total == 21:
            print('\n*** Sorry, you lose. The dealer got a blackjack.')
            print(self.show_both_hands())            
            return 'finish'

        elif player_total > 21:
            print('\n*** Sorry. You busted. You lose.')
            print(self.show_both_hands())
            return 'finish'
    
        elif dealer_total > 21:
            print('\n*** Dealer busts. You win!')
            print(self.show_both_hands())
            return 'finish'
    
        elif player_total < dealer_total and prior_choice == 's':
            print('\n*** Sorry. Your score isn\'t higher than the dealer. You lose.')
            print(self.show_both_hands())
            return 'finish'

        elif player_total > dealer_total and prior_choice == 's':
            print('\n*** Congratulations. Your score is higher than the dealer. You win')
            print(self.show_both_hands())
            return 'finish'

    @staticmethod
    def play():
        choice = 0
        print('---------Welcome To Blackjack!!-------------')
        bjg = BlackJackGame()

        while choice != 'q':
            print(bjg.show_both_hands())

            choice = input('Do you want to [H]it, [S]tand, or [Q]uit: ').lower()
            if choice == 'h':
                bjg.hit_player()
                while bjg.dealer_hand.total() < 17:
                    bjg.hit_dealer()
                if bjg.check() == 'finish':
                    print('\n----------New Game Start!!-----------')
                    bjg = BlackJackGame()

            elif choice == 's':
                while bjg.dealer_hand.total() < 17:
                    bjg.hit_dealer()
                bjg.check(prior_choice = 's')
                print('\n----------New Game Start!!-----------')
                bjg = BlackJackGame()

            elif choice == 'q':
                print('Bye, See you later!!')
                exit()


BlackJackGame.play()
