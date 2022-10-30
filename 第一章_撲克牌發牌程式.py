# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:29:50 2022

@author: 榮 鼎
"""
#撲克牌發牌程式
class Card():
    Ranks=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits=["梅", "方", "紅", "黑"]
    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up 
    def __str__(self):
        if self.is_face_up :
            sep = self.suit+self.rank
        else:
            sep="XX"
        return sep
    def pic_order(self):
        if self.rank=="A":
            Facenum = 1
        elif self.rank =="J":
            Facenum = 11
        elif self.rank =="Q":
            Facenum = 12
        elif self.rank =="K":
            Facenum = 13
        else:
            Facenum = int(self.rank)
        if self.suit =="梅":
            suit = 1
        elif self.suit == "方":
            suit = 2
        elif self.suit == "紅":
            suit = 3  
        else:
            suit = 4
        return (suit-1)*13+Facenum
    def flip(self):
        self.is_face_up=not self.is_face_up

class Hand():
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep=""
            for card in self.cards:
                rep+=str(card)+"\t"
        else:
            rep="無牌"
        return rep
    def clear(self):
        self.cards=[]
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
class Poke(Hand):
    def populate(self):
        for suit in Card.suits:
            for rank in Card.Ranks:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand=13):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print("不能繼續發牌")
if __name__=="__main__":
    print("playing card")
    players=[Hand(),Hand(),Hand(),Hand()]
    poke1=Poke()
    poke1.populate()
    poke1.shuffle()
    poke1.deal(players,13)
    
    n=1
    for hand in players:
        print("牌手",n,end=":")
        print(hand)
        n=n+1
    input("")
           
        
#P1-41-44       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        