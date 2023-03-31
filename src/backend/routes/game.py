from backend.controllers import game
from flask import request, redirect, url_for

def inicia_app(app):
    @app.route('/games', methods=['GET'])
    def lista_jogos():
        teste =  game.get_all_games()
        print(teste)
        return ''
    
    @app.route('/new_game', methods=['POST'])
    def cria_novo_jogo():
        name = request.form['name']
        platform = request.form['platform']
        price =  request.form['price']
        amount =  request.form['amount']
        game.create_new_game(name, platform, price, amount)
        
        return 'adicionou'
    