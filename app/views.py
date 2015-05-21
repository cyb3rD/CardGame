# -*- coding: utf-8 -*-
from flask import render_template, request, flash
from app import app

from Player import Player, default_avatar, PlayerStats
from Cards import Card, CardsDataBase, CardHolder

@app.route('/', methods=['GET', 'POST'])
def index():
	# 1. Заглушка для сохранения состояния через сессию

    opponent = None
    player = None
    # 2. работа с post
    if request.method == 'POST':
        opponent = Player.Load(request.form["Player1"])
        player = Player.Load(request.form["Player2"])
        # BIG REFACTORING
        if request.form["command_event"] == "MoveCard":
            pcard_in_hand = player.GetCardHolder("InHand")
            pcard_in_table = player.GetCardHolder("InPlay")
            card_index = int(request.form["command_param"]) - 1
            pstat = player.GetStats()
            look_card = pcard_in_hand.GetCard(card_index)
            card_cost = look_card.GetCardData()["cost"]
            card_type = look_card.GetCardData()["type"]
            if pstat.coins >= card_cost:
                if card_type == "soldier":

                    creture_count = 0
                    for card in pcard_in_table.GetCardsIterable():
                        if card.GetCardData()["type"] == "soldier":
                            creture_count += 1
                    if creture_count >= 3:
                        flash("You have max soldiers on table")
                    else:
                        pcur_card = pcard_in_hand.RemoveCard(card_index)
                        pcard_in_table.AddCard(pcur_card)
                        # if card instant play - play it
                        pstat.coins -= card_cost
                        pstat.damage = 0
                        for cur_card in pcard_in_table.GetCardsIterable():
                            pstat.damage += cur_card.GetCardData()["damage"]    
                else:
                    pcur_card = pcard_in_hand.RemoveCard(card_index)
                    pcard_in_table.AddCard(pcur_card)
                    # if card instant play - play it
                    pstat.coins -= card_cost
                    pstat.damage = 0
                    for cur_card in pcard_in_table.GetCardsIterable():
                        pstat.damage += cur_card.GetCardData()["damage"]
            else:
                flash("You haven't enough coins")
        if request.form["command_event"] == "EndTurn":
            pstat = player.GetStats()
            if pstat.turn_coins < 10:
                pstat.coins = pstat.turn_coins
                pstat.coins += 1
                pstat.turn_coins = pstat.coins
            pcard_in_hand = player.GetCardHolder("InHand")
            cards_count = pcard_in_hand.GetCardsCount()
            if cards_count < 5:
                p_deck = player.GetCardHolder("InDeck")
                cur_card = p_deck.RemoveCard(0)
                pcard_in_hand.AddCard(cur_card)        
            # For AI
            opstat = opponent.GetStats()
            opstat.coins += 1
    else:
        # Create Opponent
        opponent = Player("Computer AI")
        o_deck = opponent.GetCardHolder("InDeck")
        o_hand = opponent.GetCardHolder("InHand")
        for index in range(5):
            cur_card = o_deck.RemoveCard(index)
            o_hand.AddCard(cur_card)
        # Create Player
        player = Player("Player", default_avatar[1])
        p_deck = player.GetCardHolder("InDeck")
        p_hand = player.GetCardHolder("InHand")
        for index in range(5):
            cur_card = p_deck.RemoveCard(index)
            p_hand.AddCard(cur_card)
        
    # 3. логика игры
    # FOR REFACTORING START(3)
    
   
    # FOR REFACTORING END (3)


    # рендринг страницы
    return render_template("GameTable.html", opponent = opponent, player = player)

@app.route('/test', methods=['GET', 'POST'])
def test():
    # Create Opponent
    opponent = Player("Computer AI")
    # Create Fake Hand
    card_in_hand = opponent.GetCardHolder("InHand")
    card_in_hand.AddCard(1).AddCard(2).AddCard(3).AddCard(4).AddCard(5)
    # Create Fake Table
    cards_in_table = opponent.GetCardHolder("InPlay")
    cards_in_table.AddCard(10).AddCard(8).AddCard(5)

    some_card = card_in_hand.RemoveCard(0)
    return str(some_card)
    tstr = ''
    #for card in cards_in_table.GetCardsIterable():
    #    str += card.GetCardData()['name'] + "<br/>"
    tstr += CardsDataBase.Cards[5]['name'] + "<br/>"
    for card in cards_in_table.CardsId:
        tstr += str(card) + "<br/>"
        cc = CardsDataBase.CreateCard(card)
        tstr += cc.GetCardData()["name"] + "<br/>"
    return tstr