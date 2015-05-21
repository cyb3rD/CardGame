# -*- coding: utf-8 -*-
from random import shuffle


class Card():
    def __init__(self, card_data):
        self.CardData = card_data

    def GetCardData(self):
        return self.CardData

class CardHolder():
    def __init__(self, cards_list = None):
        if cards_list == None:
            self.CardsId = []
        else:
            self.CardsId = cards_list

    def AddCard(self, card_id):
        self.CardsId.append(card_id)
        return self

    def RemoveCard(self, card_index):
        card_id = self.CardsId[card_index]
        #self.CardsId.remove(card_index)
        del self.CardsId[card_index]
        return card_id

    def GetCardsIterable(self):
        for card_id in self.CardsId:
            yield CardsDataBase.CreateCard(card_id)

    def GetCard(self, card_index):
        return CardsDataBase.CreateCard(self.CardsId[card_index])

    def GetCardsCount(self):
        return len(self.CardsId)

class CardsDataBase():
    Cards = [{"name" : "odar", "type" : "weapon", "cost" : 3, "damage" : 0},
              {"name" : "olyk", "type" : "weapon", "cost" : 4, "damage" : 0},
              {"name" : "omolot", "type" : "weapon", "cost" : 5, "damage" : 0},
              {"name" : "osekira", "type" : "weapon", "cost" : 1, "damage" : 0},
              {"name" : "oyad", "type" : "weapon", "cost" : 4, "damage" : 0},
              {"name" : "sdrakon", "type" : "soldier", "cost" : 8, "damage" : 8},
              {"name" : "sdvorf", "type" : "soldier", "cost" : 6, "damage" : 4},
              {"name" : "sgolem", "type" : "soldier", "cost" : 7, "damage" : 7},
              {"name" : "siskatel", "type" : "soldier", "cost" : 3, "damage" : 1},
              {"name" : "skomandir", "type" : "soldier", "cost" : 6, "damage" : 4},
              {"name" : "slunnaya", "type" : "soldier", "cost" : 4, "damage" : 3},
              {"name" : "slychnica", "type" : "soldier", "cost" : 2, "damage" : 1},
              {"name" : "sprovidec", "type" : "soldier", "cost" : 3, "damage" : 2},
              {"name" : "sshitonosec", "type" : "soldier", "cost" : 5, "damage" : 3},
              {"name" : "ssluzhitel", "type" : "soldier", "cost" : 4, "damage" : 3},
              {"name" : "svolk", "type" : "soldier", "cost" : 1, "damage" : 2},
              {"name" : "svorgen", "type" : "soldier", "cost" : 4, "damage" : 6},
              {"name" : "svozhak", "type" : "soldier", "cost" : 2, "damage" : 2},
              {"name" : "szashitnik", "type" : "soldier", "cost" : 1, "damage" : 1},
              {"name" : "sznahar", "type" : "soldier", "cost" : 1, "damage" : 1},
              {"name" : "zkasanie", "type" : "spell", "cost" : 3, "damage" : 0},
              {"name" : "zlych", "type" : "spell", "cost" : 3, "damage" : 0},
              {"name" : "zstrely", "type" : "spell", "cost" : 2, "damage" : 0},
              {"name" : "zteni", "type" : "spell", "cost" : 3, "damage" : 0},
              {"name" : "ztexnic", "type" : "spell", "cost" : 5, "damage" : 0},
              ]
    @staticmethod
    def GenerateDeckIDs():
      lst = []
      for i in range(25):
        lst.append(i)
      shuffle(lst)
      return lst      
    
    @staticmethod
    def CreateCard(card_id):
        if card_id < 0 or card_id > CardsDataBase.Cards:
            card_id = 0
        return Card(CardsDataBase.Cards[card_id])
