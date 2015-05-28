# -*- coding: utf-8 -*-
from random import shuffle

""" Модуль описания игровых карт
"""

class Card(object):
    """ Класс Игровой карты
    """
    def __init__(self, card_data):
        """ Конструктор
        param : card_data -> dictonary{key: value}
        """
        self.__card_data = card_data
        self.__isDestroy = False
    
    def __getitem__(self, card_param):
        """ Возвращает параметр карты
        param : card_param -> string (key)
        return : Param Value or None
        """
        tmp = self.__card_data[card_param] if card_param in self.__card_data else None
        return tmp

    def __setitem__(self, card_param, value):
        raise AttributeError("Private member!")

    def isDestroy(self):
        """ Уничтожена ли карта
        """
        return self.__isDestroy

    def OnPlay(self):
        """ Срабатывает при входе в игру
        """
        pass

    def OnDestroy(self):
        """ Срабатывает при уничтожении
        """
        pass

class CardHolder(object):
    """ Класс контейнера для игровых карт
    """
    def __init__(self, cards_list = None):
        """ Конструктор
        param : cards_list -> list[id, id, ....]
        *id - идентификатор карты в базе (CardsDataBase)
        """
        if cards_list == None:
            self.__cards = []
        else:
            self.__cards = cards_list

    def AddCard(self, card_id):
        """ Добавить карту в контейнер
        param : card_id -> int (id from cards data base CardsDataBase)
        return : self
        """
        self.__cards.append(card_id)
        return self

    def RemoveCard(self, card_index):
        """ Удаляет карту из контейнера по индексу
        param : card_index -> int
        return : removed card card_id or None
        """
        if card_index > self.__cards or card_index < 0:
            return None
        card_id = self.__cards[card_index]
        del self.__cards[card_index]
        return card_id

    def GetCardsIterable(self):
        """ Итеративно создает карты из контейнера
        return : yield Card() 
        """
        for card_id in self.__cards:
            yield CardsDataBase.CreateCard(card_id)

    def GetCard(self, card_index):
        """ Создает карту из контейнера по индексу
        param : card_index -> int
        return : Card()
        """
        return CardsDataBase.CreateCard(self.__cards[card_index])

    def GetCardsCount(self):
        """ Возвращает кол-во карт в контейнере
        return : int
        """
        return len(self.__cards)

class CardsDataBase(object):
    """ Статический класс данных игровых карт
    """
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
    def GenerateDeck():
        """ Генерирует игровую коллоду
        return : list[id, id, ...]
        """
        lst = []
        for i in range(25):
            lst.append(i)
        shuffle(lst)
        return lst      
    
    @staticmethod
    def CreateCard(card_id):
        """ Создает игровую карту
        param : card_id -> int
        return : Card() or None
        """
        if card_id < 0 or card_id > CardsDataBase.Cards:
            return None
        return Card(CardsDataBase.Cards[card_id])
