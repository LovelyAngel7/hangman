
import random

class Card:
    suits = ('spades','hearts','diamonds','clubs')
    values =(None,None,
             '2','3','4','5','6','7','8','9','10',
             'Jack','Queen','King','Ace')
    
    def __init__(self,v,s):
        """v,sは整数値です。suits,valuesリストにおけるインデックス値になります。"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        return self.suits[self.suit] + 'の' + self.values[self.value]

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1=input('プレイヤー1の名前')
        name2=input('プレイヤー2の名前')
        self.deck=Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def winPrint(self, winner):
        print('このラウンドは{}が勝ちました'.format(winner.name))

    def drawPrint(self): #drawPrint(self,p1,p2):　引数としてプレイヤーオブジェクトを受け取っていたが、よく考えると不要だ。
        print('{}は{}を、{}は{}を引きました。'.format(self.p1.name, self.p1.card, self.p2.name, self.p2.card))

    def result_Print(self, p1, p2):
        if p1.wins > p2.wins: #引数として受け取ったプレイヤーオブジェクトのウィンを取得
            return 'ゲーム終了。{}勝した{}の勝利です。'.format(p1.wins, p1.name)
        elif self.p1.wins == self.p2.wins: #別に引数として受け取らなくても参照可能なので、これでもいい
            return 'ゲーム終了。両者{}勝で引き分けです。'.format(p1.wins)
        if p1.wins < p2.wins:
            return 'ゲーム終了。{}勝した{}の勝利です。'.format(p2.wins, p2.name)


    def playGame(self):
        cards =self.deck.cards
        print('戦争を始めます')
        while len(cards) >= 2:
            response = input('q で終了。それ以外のキーでプレイ')
            if response =='q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.drawPrint()
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.winPrint(self.p1)
            else:
                self.p2.wins += 1
                self.winPrint(self.p2)
        
        print(self.result_Print(self.p1, self.p2))

game = Game()
game.playGame() #クラス内関数はインスタンス化してから実行する。単にGame.playGame()は実行できない。