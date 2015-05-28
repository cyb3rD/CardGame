# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, session, url_for, g
from flask.ext.login import login_required, login_user, logout_user, current_user
from app import app, db, lm

from Game import Game, GameEvent
from Player import Player, default_avatar, PlayerStats
from Cards import Card, CardsDataBase, CardHolder
from Forms import LoginForm, RegisterForm
from models import User

@app.route('/', methods=['GET', 'POST'])
#Authentication required
@login_required
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    
    form = LoginForm()
    if request.method == 'GET':
        return render_template('Login.html', title=u'Вход', form=form)
    
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        registered_user = User.query.filter_by(username=username,password=password).first()
        if registered_user is None:
            flash('Username or Password is invalid')
            return redirect(url_for('register'))
        login_user(registered_user)
        flash('Logged in successfully')
    return redirect(url_for('index'))

@app.route('/register' , methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('Register.html', title=u'Регистрация', form=form)
    
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered! You can now Log In...')
    return redirect(url_for('login'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    pass