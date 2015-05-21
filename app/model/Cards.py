# -*- coding: utf-8 -*-

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
        return CardsDataBase.CreateCard(card_index)


class CardsDataBase():
    Cards = [{"name" : "odar", "type" : "weapon"},
              {"name" : "olyk", "type" : "weapon"},
              {"name" : "omolot", "type" : "weapon"},
              {"name" : "osekira", "type" : "weapon"},
              {"name" : "oyad", "type" : "weapon"},
              {"name" : "sdrakon", "type" : "soldier"},
              {"name" : "sdvorf", "type" : "soldier"},
              {"name" : "sgolem", "type" : "soldier"},
              {"name" : "siskatel", "type" : "soldier"},
              {"name" : "skomandir", "type" : "soldier"},
              {"name" : "slunnaya", "type" : "soldier"},
              {"name" : "slychnica", "type" : "soldier"},
              {"name" : "sprovidec", "type" : "soldier"},
              {"name" : "sshitonosec", "type" : "soldier"},
              {"name" : "ssluzhitel", "type" : "soldier"},
              {"name" : "svolk", "type" : "soldier"},
              {"name" : "svorgen", "type" : "soldier"},
              {"name" : "svozhak", "type" : "soldier"},
              {"name" : "szashitnik", "type" : "soldier"},
              {"name" : "sznahar", "type" : "soldier"},
              {"name" : "zkasanie", "type" : "spell"},
              {"name" : "zlych", "type" : "spell"},
              {"name" : "zstrely", "type" : "spell"},
              {"name" : "zteni", "type" : "spell"},
              {"name" : "ztexnic", "type" : "spell"},
              ]

    @staticmethod
    def CreateCard(card_id):
        if card_id < 0 or card_id > CardsDataBase.Cards:
            card_id = 0
        return Card(CardsDataBase.Cards[card_id])
