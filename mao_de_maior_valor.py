# -- coding: utf-8 --
from manipulador_funcoes import Manipular_funcoes

'''A classe maior_jogada analisa qual jogada é mais forte comparando jogadas que deram empate ,com esse método verifico
    dentre as jogadas que empataram qual tera maior pontuação de acordo com o valor das cartas.'''
class Maior_jogada(object):

    '''
        hand_manipulator vai receber uma classe que serve como auxílio para manipulação de funções
    '''
    def __init__(self):
        self.hand_manipulator = Manipular_funcoes()


    '''check_higher_four_of_a_kind: quando ocorrer empate em uma quadra essa função verifica as 
        cartas de maior (maior quadra) valor para critério de desempate utilizando para isso a função _check_higher_card
            parametros:
                cards: vetor de entrada já ordenado 
                another_cards: vetor de entrada já ordenado
            retorno:
                   WIN , LOSS , DRAW'''
    def check_higher_four_of_a_kind(self, cards, another_cards):
        card_value = self.hand_manipulator.get_four_of_a_kind_value(cards)
        another_card_value = self.hand_manipulator.get_four_of_a_kind_value(another_cards)
        return self._check_higher_card(card_value, another_card_value)


    '''check_higher_straight: quando ocorrer empate no straight essa função verifica as 
        cartas de maior valor para critério de desempate utilizando para isso a função _check_higher_card
               parametros:
                   cards: vetor de entrada já ordenado 
                   another_cards: vetor de entrada já ordenado
               retorno:
                   WIN , LOSS , DRAW'''
    def check_higher_straight(self, cards, another_cards):
        return self._check_higher_card(cards[0], another_cards[0])


    '''check_higher_three_of_a_kind: quando ocorrer empate na trinca essa função verifica as 
        cartas de maior valor para critério de desempate utilizando para isso a função _check_higher_card
                parametros:
                   cards: vetor de entrada já ordenado 
                   another_cards: vetor de entrada já ordenado
                retorno:
                        WIN , LOSS , DRAW'''
    def check_higher_three_of_a_kind(self, cards, another_cards):
        card_value = self.hand_manipulator.get_three_of_a_kind_value(cards)
        another_card_value = self.hand_manipulator.get_three_of_a_kind_value(another_cards)
        return self._check_higher_card(card_value, another_card_value)


    '''check_higher_two_pair: quando ocorrer empate em dois pares essa função verifica as 
        cartas de maior valor para critério de desempate utilizando para isso a função _check_higher_card
                parametros:
                   cards: vetor de entrada já ordenado 
                   another_cards: vetor de entrada já ordenado
                retorno:
                   WIN , LOSS , DRAW'''
    def check_higher_two_pair(self, cards, another_cards):
        higher_cards_pair_value = max(self.hand_manipulator.get_one_pair_value(cards),
                                      self.hand_manipulator.get_one_pair_value(
                                          self.hand_manipulator.slice_one_pair(cards)))
        higher_another_cards_pair_value = max(self.hand_manipulator.get_one_pair_value(another_cards),
                                              self.hand_manipulator.get_one_pair_value(
                                                  self.hand_manipulator.slice_one_pair(another_cards)))
        return self._check_higher_card(higher_cards_pair_value, higher_another_cards_pair_value)


    '''check_higher_one_pair: quando ocorrer empate em um par essa função verifica as 
        cartas de maior valor para critério de desempate utilizando o método hand_manipulator 
        Observação: nessa comparação pode ocorrer empate definitivo 
                parametros:
                   cards: vetor de entrada já ordenado 
                   another_cards: vetor de entrada já ordenado
                retorno:
                   WIN , LOSS , DRAW'''
    def check_higher_one_pair(self, cards, another_cards, tiebreak=False):
        cards_pair_value = self.hand_manipulator.get_one_pair_value(cards)
        another_cards_pair_value = self.hand_manipulator.get_one_pair_value(another_cards)
        if self.hand_manipulator.convert_to_numerical_value(cards_pair_value) == self.hand_manipulator.convert_to_numerical_value(another_cards_pair_value):
            return self.check_higher_card(self.hand_manipulator.slice_by_card(cards, cards_pair_value),
                                          self.hand_manipulator.slice_by_card(another_cards, another_cards_pair_value),
                                          True) if tiebreak else 'DRAW'
        elif self.hand_manipulator.convert_to_numerical_value(
                cards_pair_value) > self.hand_manipulator.convert_to_numerical_value(another_cards_pair_value):
            return 'WIN'
        return 'LOSS'


    '''check_higher_card: vai comparar as cartas das mãos de entrada e verificar quais são maiores  
        utilizando o metodo hand_manipulator 
        Observação: nessa comparação pode ocorrer empate definitivo 
                parametros:
                   cards: vetor de entrada já ordenado 
                   another_cards: vetor de entrada já ordenado
                retorno:
                   WIN , LOSS , DRAW'''
    def check_higher_card(self, cards, another_cards, tiebreak=False):
        if len(cards) == 0 or len(another_cards) == 0:
            return 'DRAW'
        cards_higher_value = self.hand_manipulator.get_higher_card_value(cards)
        another_cards_higher_value = self.hand_manipulator.get_higher_card_value(another_cards)
        if self.hand_manipulator.convert_to_numerical_value(
                cards_higher_value) == self.hand_manipulator.convert_to_numerical_value(another_cards_higher_value):
            return self.check_higher_card(self.hand_manipulator.slice_by_card(cards, cards_higher_value),
                                          self.hand_manipulator.slice_by_card(another_cards,
                                                                              another_cards_higher_value),
                                          True) if tiebreak else 'DRAW'
        elif self.hand_manipulator.convert_to_numerical_value(
                cards_higher_value) > self.hand_manipulator.convert_to_numerical_value(another_cards_higher_value):
            return 'WIN'
        return 'LOSS'


    '''_check_higher_card:  é um método auxiliar pra fazer comparação de duas cartas 
                parametros:
                   cards: vetor de entrada já ordenado 
                   another_cards: vetor de entrada já ordenado
                retorno:
                   WIN , LOSS , DRAW'''
    def _check_higher_card(self, card, another_card):
        if self.hand_manipulator.convert_to_numerical_value(card) == self.hand_manipulator.convert_to_numerical_value(
                another_card):
            return 'DRAW'
        elif self.hand_manipulator.convert_to_numerical_value(card) > self.hand_manipulator.convert_to_numerical_value(
                another_card):
            return 'WIN'
        return 'LOSS'