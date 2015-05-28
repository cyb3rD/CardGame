# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app

from Game import Game, GameEvent
from Player import Player, default_avatar, PlayerStats
from Cards import Card, CardsDataBase, CardHolder

@app.route('/', methods=['GET', 'POST'])
def index():
    game = Game.GetInstance()
    # Если не Post
    if request.method != 'POST':
        game.Start()
    # Если Post
    else:
        game_event = GameEvent.GetEvent(request.form["command_event"], request.form["command_param"])
        game.Restore(request.form["Player1"], request.form["Player2"])
        game.Update(game_event)
    # рендринг страницы
    return render_template("GameTable.html", opponent = game.Opponent, player = game.Player, game = game)
