# -*- coding: utf-8 -*-
import jsonpickle
from Cards import CardHolder, CardsDataBase, Card
''' Модуль для описания игрока
'''
default_avatar = ["avatar1.png", "avatar2.png"]

class PlayerStats(object):
    """ Класс характеристики игрока
    """
    def __init__(self, coins = 0, health = 20, damage = 0, defense = 0):
        self.coins = coins
        self.health = health
        self.damage = damage
        self.defense = defense
        self.turn_coins = coins
        self.active_solider = 0

class Player():
    ''' Базовый класс игрока
    param : name -> string
    param : avatar -> string (image name)
    '''
    def __init__(self, name = "Default", avatar = default_avatar[0]):
        self.name = name
        self.avatar = avatar
        self.__Stats = PlayerStats()
        self.__Cards = {"InDeck" : CardHolder(CardsDataBase.GenerateDeck()),
                      "InPlay" : CardHolder(),
                      "InHand" : CardHolder(),
                      "InGraveyard" : CardHolder()}

    @property
    def Stats(self):
        """ Получение характеристик игрока
        """
        #check return self.__Stats
        tmp = self.__Stats
        return tmp

    @Stats.setter
    def Stats(self, value):
        raise AttributeError("Private member!")

    def GetCardHolder(self, store_name):
        """ Получение контейнера игровых карт
        param : store_name -> string ("InDeck", "InPlay", "InHand", "InGraveyard")
        return : CardHolder() or None
        """
        if store_name in self.__Cards:
            return self.__Cards[store_name]
        else:
            return None

    def MoveCard(self, card_index, source_holder, dest_holder):
        """ Переместить карту
        param : source_holder -> string
        param : dest_holder -> string
        """
        card_id = self.__Cards[source_holder].RemoveCard(card_index)
        self.__Cards[dest_holder].AddCard(card_id)

    def StartTurn(self):
        """ Начать ход
        """
        if self.__Stats.turn_coins < 10:
            self.__Stats.turn_coins += 1
        if self.__Cards["InHand"].GetCardsCount() < 5:
            self.MoveCard(0,"InDeck","InHand")
        self.__Stats.coins = self.__Stats.turn_coins

    def PlayCard(self, card_index):
        """ Разиграть карту
        param : card_index -> int
        return : string ("Ok" or "Error message")
        """
        play_card = self.__Cards["InHand"].GetCard(card_index)
        if play_card["cost"] > self.__Stats.coins:
            return "You haven't enough coins"

        if play_card["type"] == "soldier":
            if self.__Stats.active_solider == 3:
                return "You have max soldiers on table"
            else:                
                self.__Stats.active_solider += 1
                self.__Stats.damage += play_card["damage"]
               
        self.__Stats.coins -= play_card["cost"]
        #
        self.MoveCard(card_index, "InHand", "InPlay")
        #
        play_card.OnPlay()
        return "Ok"
               
    def EndTurn(self):
        pass

    def ChangeHelth(self, health):
        self.__Stats.health += health

    def Save(self):
        """ Сохранить игрока в json
        return : string (json format)
        """
        return jsonpickle.encode(self)
    
    @staticmethod
    def Load(json_str):
        """ Загрузить игрока из json
        param : string (json format)
        return : Player()
        """
        return jsonpickle.decode(json_str)