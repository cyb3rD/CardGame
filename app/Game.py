# -*- coding: utf-8 -*-

from Player import Player, default_avatar
from AI import SimpleAI

class GameEvent(object):
    """ Класс действия в игре
    * future -> рефакторин в комманду
    """
    __game_events = {"PlayCard" : True, "EndTurn" : False}

    @staticmethod
    def GetEvent(game_event, event_param = ""):
        if game_event not in GameEvent.__game_events:
            raise ValueError(game_event + " is unknow event!")
        is_need_param = GameEvent.__game_events[game_event]
        is_param_get = event_param != ""
        if is_need_param != is_param_get:
            raise ValueError(game_event + " need param!")
        return {game_event : event_param}

class Game(object):
    """ Класс Игрового цикла
    """
    __self_Instance = None
    __self_Init = False
    __Players = {"Opponent" : None,
                 "Player" : None}

    def __init__(self):
        if Game.__self_Init == False:
            raise ValueError("Game not instantiation, use only GetInstance method!")
        if Game.__self_Instance != None:
            raise ValueError("Game always instantiation, use only GetInstance method!")
        self.__EventsStatus = []

    @classmethod
    def GetInstance(cls):
        """ Инстанцировать класс игры
        """
        if cls.__self_Init == False:
            cls.__self_Init = True
        if cls.__self_Instance == None:
            cls.__self_Instance = Game()
        return cls.__self_Instance

    @property
    def Opponent(self):
        return Game.__Players["Opponent"]

    @Opponent.setter
    def Opponent(self, value):
        raise AttributeError("Opponent is Private member!")

    @property
    def Player(self):
        return Game.__Players["Player"]

    @Player.setter
    def Player(self, value):
        raise AttributeError("Player is Private member!")

    @property
    def EventsStatus(self):
        return self.__EventsStatus

    @EventsStatus.setter
    def EventsStatus(self, value):
        raise AttributeError("EventsStatus is Private member!")

    @classmethod
    def GetPlayer(cls, player_name):
        """ Получение игрока из реестра
        param : string ("Opponent" or "Player")
        return : Player()
        """
        if cls.__self_Init != True:
            raise ValueError("Game is not instantiation, use GetInstance method!")
        if cls.__Players[player_name] == None:
            raise AttributeError("Game not started, use Start or Restore methods!")
        return cls.__Players[player_name]

    def Start(self):
        """ Старт игры
        """
        self.__EventsStatus = []
        Game.__Players["Opponent"] = Player("Computer")
        Game.__Players["Player"] = Player("Player", default_avatar[1])
        for card_index in range(5):
            self.Opponent.MoveCard(card_index,"InDeck","InHand")
            self.Player.MoveCard(card_index,"InDeck","InHand")
        self.Player.StartTurn()
        self.Opponent.StartTurn()

    def Restore(self, opponent_save_json, player_save_json):
        """ Востановление игры
        """
        Game.__Players["Opponent"] = Player.Load(opponent_save_json)
        Game.__Players["Player"] = Player.Load(player_save_json)

    def Update(self, game_event):
        """ Обновить состояние игры
        param : game_event -> dict from GameEvent.GetEvent()
        * future -> рефакторинг к виду Update(self)
        """
        self.__EventsStatus = []
        if "PlayCard" in game_event:
            #play card
            card_id = int(game_event["PlayCard"]) - 1            
            self.__EventsStatus.append(self.Player.PlayCard(card_id))            
            return
        if "EndTurn" in game_event:
            # разыгрываем карты игрока
            # передаем ход ai
            self.Opponent.StartTurn()
            ai = SimpleAI(self.Opponent)
            ai.Action()
            self.Opponent.EndTurn()
            # передаем ход игроку
            self.Player.StartTurn()
            return
        return
