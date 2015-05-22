# -*- coding: utf-8 -*-
import jsonpickle
from Cards import CardHolder, CardsDataBase
''' Модуль для описания игрока
'''
default_avatar = ["avatar1.png", "avatar2.png"]

class PlayerStats():
    def __init__(self, coins = 1, health = 20, damage = 0, defense = 0):
        self.coins = coins
        self.health = health
        self.damage = damage
        self.defense = defense
        self.turn_coins = coins

class Player():
    ''' Базовый класс игрока
    '''
    def __init__(self, name = "Default", avatar = default_avatar[0], stats = None):
        self.name = name
        self.avatar = avatar
        if stats == None:
            self.stats = PlayerStats()
        else:
            self.stats = stats
        self.Cards = {"InDeck" : CardHolder(CardsDataBase.GenerateDeckIDs()),
                      "InPlay" : CardHolder(),
                      "InHand" : CardHolder(),
                      "InGraveyard" : CardHolder()}

    def GetStats(self):
        return self.stats

    def GetCardHolder(self, store_name):
        if store_name in self.Cards:
            return self.Cards[store_name]
        else:
            return None

    def Save(self):
        return jsonpickle.encode(self)
    
    @staticmethod
    def Load(json_str):
        return jsonpickle.decode(json_str)