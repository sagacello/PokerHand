# -- coding: utf-8 --
from manipulador_funcoes import Manipular_funcoes


'''suits é um dicionário que representa os naipes de um baralho'''
suits = {
    'S': 'spades',
    'H': 'hearts',
    'D': 'diamonds',
    'C': 'clubs'
}

'''A classe verificador_de_jogadas serve para analisar qual tipo de jogada é correspondente com cada mão de entrada
    recebendo um único método hand_manipulator que é utilizado para ajudar na construção das funções'''
class Verificador_de_jogadas(object):

    ''' Todas as funções a seguir são para verificar as jogadas e o método
       hand_manipulator foi chamado para ajudar na manipulação das funções, '''
    def __init__(self):
        self.hand_manipulator = Manipular_funcoes()


    '''is_royal_flush :recebe as cartas e verifica se a jogada é flush e no seu retorno verifica se a jogada é straight,
        e se for será direcionado em outra condicional , se não for retornará sua expressão boleana .
            parametros:
                cards: vetor de entrada já ordenado
            retorno:
                True ou False'''
    def is_royal_flush(self, cards):
        if self.is_flush(cards):
            return self.is_straight(cards, True)
        return False


    '''is_straight_flush:recebe as cartas e verifica se a jogada é flush e se for cai na condilçao para  verificar
       se a jogada tambem é straight
            parametros:
                cards: vetor de entrada já ordenado
            retorno:
                True ou False'''
    def is_straight_flush(self, cards):
        if self.is_flush(cards):
            return self.is_straight(cards)
        return False


    '''is_four_of_a_kind:recebe as cartas e verifica se a jogada é uma quadra se for retorna True se não retorna False 
            parametros:
                cards: vetor de entrada já ordenado
            retorno:
                True ou False'''
    def is_four_of_a_kind(self, cards):
        for card in cards:
            if [card[0] for card in cards].count(card[0]) == 4:
                return True
        return False


    '''is_full_house:recebe as cartas e verifica se a jogada é full_house se for retorna True se não retorna False
            parametros:
                cards: vetor de entrada já ordenado
            retorno:
                True ou False'''
    def is_full_house(self, cards):
        set_cards = list(set([card[0] for card in cards]))
        return True if len(set_cards) == 2 and [card[0] for card in cards].count(set_cards[0]) in (2, 3) else False


    '''is_flush:recebe as cartas e verifica se a jogada é flush se for retorna a expressão boleana da condicioonal implicita
            parametros:
                    cards: vetor de entrada já ordenado
            retorno:
                True ou False'''
    def is_flush(self, cards):
        suits_set = list(set([card[1] for card in cards]))
        return len(suits_set) == 1 and suits_set[0] in suits.keys()


    '''is_straight:recebe as cartas e verifica se a jogada é is_straight se for retorna True se não retorna False
            parametros:
                    cards: vetor de entrada já ordenado
            retorno:
                True ou False'''
    def is_straight(self, cards, check_royal=False):
        is_straight_var = all(self.hand_manipulator.convert_to_numerical_value(i) - 1 == self.hand_manipulator.convert_to_numerical_value( j) for i, j in zip(cards, cards[1:]))
        if check_royal is True:
            return is_straight_var and cards[len(cards) - 1][0] == 'T'
        return is_straight_var


    '''is_three_of_a_kind:recebe as cartas e verifica se a jogada é uma trinca se for retorna True se não retorna False
            parametros:
                    cards: vetor de entrada já ordenado
            retorno:
                True ou False'''
    def is_three_of_a_kind(self, cards):
        for card in cards:
            if [card[0] for card in cards].count(card[0]) == 3:
                return True
        return False


    '''is_two_pair:recebe as cartas e verifica se a jogada é uma combinação de dois pares se for retorna True se não retorna False
            parametros:
                    cards: vetor de entrada já ordenado
            retorno:
                True ou False'''
    def is_two_pair(self, cards):
        if self.is_one_pair(cards):
            if self.is_one_pair(self.hand_manipulator.slice_one_pair(cards)):
                return True
        return False


    '''is_two_pair:recebe as cartas e verifica se a jogada é um par se for retorna True se não retorna False
                parametros:
                    cards: vetor de entrada já ordenado
                retorno:
                    True ou False'''
    def is_one_pair(self, cards):
        for card in cards:
            if [card[0] for card in cards].count(card[0]) == 2:
                return True
        return False