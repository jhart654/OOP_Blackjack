import random

class blackjack:
    pass

    def __init__(self, player = random.randint(1, 12), dealer = random.randint(1, 12)):
        self.dealer = dealer
        self.player = player

        self.firstDealerCard = random.randint(1,12)
        self.secondDealerCard = self.dealer + self.firstDealerCard
        print(f'Dealer first Card: {self.dealer}')
        print(f'Dealer second card: {self.firstDealerCard}')
        self.firstPlayerCard = random.randint(1,12)  
        print(f'Player first card:  {self.player}')
        print(f'Player second card: {self.firstPlayerCard}')
        self.playerFirstHand = self.player + self.firstPlayerCard

    def playerDeal(self):
        while True:
            self.playerQuestion = input('Would you like to hit or stand? ')
            if self.playerQuestion == 'hit':
                self.newCard = random.randint(1, 12)
                self.playerFirstHand += self.newCard
                self.firstDealerCard += self.newCard
                print(self.playerFirstHand)
                if self.playerFirstHand > 21:
                    print('Busted')
                    break
            elif self.playerQuestion == 'stand':
                break
        
    def winner(self):
        if self.playerFirstHand > 21:
            print('You Lost')
        elif self.playerFirstHand < self.secondDealerCard:
            print('Dealer wins')
            print(f'Player = {self.playerFirstHand}')
            print(f'Dealer = {self.secondDealerCard}')
        elif self.playerFirstHand > self.secondDealerCard:
            print('Player wins!!')
            print(f'Player = {self.playerFirstHand}')
            print(f'Dealer =  {self.secondDealerCard}')
        elif self.playerFirstHand == self.secondDealerCard:
            print('Draw')

            
 
newGame = blackjack()
newGame.playerDeal()
newGame.winner()
