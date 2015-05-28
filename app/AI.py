# -*- coding: utf-8 -*-
""" Модуль AI
"""
from Player import Player

import Cards

class SimpleAI(object):
    """ Простой AI
    """
    def __init__(self, player):
        self.__Player = player
         
    def Action(self):
        """ Совершить действия
        """
        events_log = []
        while True:
            card_index = self.__GetPlayableCard()
            if card_index != -1:
                simple_event = self.__Player.PlayCard(card_index)
                if simple_event != "Ok":
                    break
                events_log.append(simple_event)   
            else:
                break
        return events_log

    def __GetPlayableCard(self):
        """ Получить первую карту которую можно разиграть
        return : int -> card_index or -1
        """
        player_stats = self.__Player.Stats
        cards_in_hand = self.__Player.GetCardHolder("InHand")
        for index, card in enumerate(cards_in_hand.GetCardsIterable()):
            if card["cost"] <= player_stats.coins:
                return index
        return -1