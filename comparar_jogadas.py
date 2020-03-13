# -- coding: utf-8 --

from verificar_jogadas import Verificador_de_jogadas
from mao_de_maior_valor import Maior_jogada


'''Na classe comparar_jogadas vou ter todas as funções de comparação para cada tipo de jogada entre duas mãos, 
recebo duas mãos para cada função e vejo qual é mais forte devido ao seu agrupamento , a comparação é processada do maior 
valor para o de menor valor ,ou seja, começa verificando o compare_royal_flush e vai decrescendo de valor de jogada de acordo 
com as regras do poker '''
class Comparador_pokerhands(object):


  '''hand_ratings_verifier recebe a classe verificar_jogadas para analisar o tipo de jogada referente as cartas
     higher_hands_checker recebe a classe maior_jogada que vai estabelecer qual é a melhor jogada entre as duas mãos de poker
     que estão sendo comaparadas'''
  def __init__(self):
    self.hand_ratings_verifier = Verificador_de_jogadas()
    self.higher_hands_checker = Maior_jogada()


  '''O método compare_royal_flush verifica se entre duas mãos existe um Royal Straight Flush. Em caso positivo, retorna-se o vencedor ou empate.
    Em caso negativo, desencadeia-se uma cadeia de comparações a fim de encontrar qual mão vencerá ou se há um empate.
        parametro:
          cards: vetor de entrada já ordenado
          another_cards: vetor de entrada já ordenado
        retorno:
          WIN ,LOSS ,(DRAW)
          compare_straight_flush: função para straight flush'''
  def compare_royal_flush(self, cards, another_cards):
    if self.hand_ratings_verifier.is_royal_flush(cards):
      return 'DRAW' if self.hand_ratings_verifier.is_royal_flush(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_royal_flush(another_cards) else self.compare_straight_flush(cards, another_cards)


  '''O método compare_straight_flush vai comparar as duas mãos de entrada e verificar qual jogada foi estabelicida de acordo com método de verificação(hand_ratings_verifier), 
    se a jodaga ocorrer somente em uma das mãos, então a função vai definir vitória ou derrota para a mão que obteve a jogada, se não ocorrer essas condições 
    e ambas as mãos estiverem com a mesma jogada, será estabelecido o método (higher_hands_checker) para analisar qual mão tem as cartas de maior valor.
    Se as cartas não entrarem nessas condições descritas a próxima função de menor valor demandará um novo teste.
        parametro:
          cards: vetor de entrada já ordenado
          another_cards: vetor de entrada já ordenado
        retorno:
          WIN ,LOSS 
          compare_four_of_a_kind: função para comparar quadra'''
  def compare_straight_flush(self, cards, another_cards):
    if self.hand_ratings_verifier.is_straight_flush(cards):
      return self.higher_hands_checker.check_higher_straight(cards, another_cards) if self.hand_ratings_verifier.is_straight_flush(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_straight_flush(another_cards) else self.compare_four_of_a_kind(cards, another_cards)


  '''O método compare_four_of_a_kind vai comparar as duas mãos de entrada e verificar qual jogada foi estabelicida de acordo com método de verificação(hand_ratings_verifier), 
    se a jodaga ocorrer somente em uma das mãos, então a função vai definir vitória ou derrota para a mão que obteve a jogada, se não ocorrer essas condições 
    e ambas as mãos estiverem com a mesma jogada, será estabelecido o método (higher_hands_checker) para analisar qual mão tem as cartas de maior valor.
    Se as cartas não entrarem nessas condições descritas a próxima função de menor valor processará um novo teste.
        parametro:
          cards: vetor de entrada já ordenado
          another_cards: vetor de entrada já ordenado
        retorno:
          WIN ,LOSS '''
  def compare_four_of_a_kind(self, cards, another_cards):
    if self.hand_ratings_verifier.is_four_of_a_kind(cards):
      return self.higher_hands_checker.check_higher_four_of_a_kind(cards, another_cards) if self.hand_ratings_verifier.is_four_of_a_kind(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_four_of_a_kind(another_cards) else self.compare_full_house(cards, another_cards)


  '''O método compare_full_house vai comparar as duas mãos de entrada e verificar qual jogada foi estabelicida de acordo com método de verificação(hand_ratings_verifier), 
      se a jodaga ocorrer somente em uma das mãos, então a função vai definir vitória ou derrota para a mão que obteve a jogada, se não ocorrer essas condições 
      e ambas as mãos estiverem com a mesma jogada, será estabelecido o método (higher_hands_checker) para analisar qual mão tem as cartas de maior valor.
      Se as cartas não entrarem nessas condições descritas a próxima função de menor valor processará um novo teste.
          parametro:
            cards: vetor de entrada já ordenado
            another_cards: vetor de entrada já ordenado
          retorno:
            WIN ,LOSS '''
  def compare_full_house(self, cards, another_cards):
    if self.hand_ratings_verifier.is_full_house(cards):
      return self.higher_hands_checker.check_higher_three_of_a_kind(cards, another_cards) if self.hand_ratings_verifier.is_full_house(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_full_house(another_cards) else self.compare_flush(cards, another_cards)


  '''O método compare_flush vai comparar as duas mãos de entrada e verificar qual jogada foi estabelicida pela função de verificação(hand_ratings_verifier), 
     e então concluir vitória , derrota ou empate (nesse caso em específico pode empatar), se não ocorrer essas condições a próxima função 
     de menor valor será direcionada para fazer o novo teste.
          parametro:
            cards: vetor de entrada já ordenado
            another_cards: vetor de entrada já ordenado
          retorno:
            WIN ,LOSS ,(DRAW)'''
  def compare_flush(self, cards, another_cards):
    if self.hand_ratings_verifier.is_flush(cards):
      return 'DRAW' if self.hand_ratings_verifier.is_flush(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_flush(another_cards) else self.compare_straight(cards, another_cards)


  '''O método compare_straight vai comparar as duas mãos de entrada e verificar qual jogada foi estabelicida de acordo com método de verificação(hand_ratings_verifier), 
        se a jodaga ocorrer somente em uma das mãos, então a função vai definir vitória ou derrota para a mão que obteve a jogada, se não ocorrer essas condições 
        e ambas as mãos estiverem com a mesma jogada, será estabelecido o método (higher_hands_checker) para analisar qual mão tem as cartas de maior valor.
        Se as cartas não entrarem nessas condições descritas a próxima função de menor valor demandará um novo teste.
            parametro:
              cards: vetor de entrada já ordenado
              another_cards: vetor de entrada já ordenado
            retorno:
              WIN ,LOSS '''
  def compare_straight(self, cards, another_cards):
    if self.hand_ratings_verifier.is_straight(cards):
      return self.higher_hands_checker.check_higher_straight(cards, another_cards) if self.hand_ratings_verifier.is_straight(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_straight(another_cards) else self.compare_three_of_a_kind(cards, another_cards)


  '''O método compare_three_of_a_kind vai comparar as duas mãos de entrada e verificar qual jogada foi estabelicida de acordo com método de verificação(hand_ratings_verifier), 
      se a jodaga ocorrer somente em uma das mãos, então a função vai definir vitória ou derrota para a mão que obteve a jogada, se não ocorrer essas condições 
      e ambas as mãos estiverem com a mesma jogada, será estabelecido o método (higher_hands_checker) para analisar qual mão tem as cartas de maior valor.
      Se as cartas não entrarem nessas condições descritas a próxima função de menor valor processará um novo teste.
          parametro:
            cards: vetor de entrada já ordenado
            another_cards: vetor de entrada já ordenado
          retorno:
            WIN ,LOSS '''
  def compare_three_of_a_kind(self, cards, another_cards):
    if self.hand_ratings_verifier.is_three_of_a_kind(cards):
      return self.higher_hands_checker.check_higher_three_of_a_kind(cards, another_cards) if self.hand_ratings_verifier.is_three_of_a_kind(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_three_of_a_kind(another_cards) else self.compare_two_pair(cards, another_cards)


  '''O método compare_two_pair vai comparar as duas mãos de entrada e verificar qual jogada foi estabelicida de acordo com método de verificação(hand_ratings_verifier), 
      se a jodaga ocorrer somente em uma das mãos, então a função vai definir vitória ou derrota para a mão que obteve a jogada, se não ocorrer essas condições 
      e ambas as mãos estiverem com a mesma jogada, será estabelecido o método (higher_hands_checker) para analisar qual mão tem as cartas de maior valor.
      Se as cartas não entrarem nessas condições descritas a próxima função de menor valor processará um novo teste.
          parametro:
            cards: vetor de entrada já ordenado
            another_cards: vetor de entrada já ordenado
          retorno:
            WIN ,LOSS  '''
  def compare_two_pair(self, cards, another_cards):
    if self.hand_ratings_verifier.is_two_pair(cards):
      return self.higher_hands_checker.check_higher_two_pair(cards, another_cards) if self.hand_ratings_verifier.is_two_pair(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_two_pair(another_cards) else self.compare_one_pair(cards, another_cards)


  '''O método compare_one_pair vai comparar as duas mãos de entrada e verificar qual jogada foi estabelicida de acordo com método de verificação(hand_ratings_verifier), 
      se a jodaga ocorrer somente em uma das mãos, então a função vai definir vitória ou derrota para a mão que obteve a jogada, se não ocorrer essas condições 
      e ambas as mãos estiverem com a mesma jogada, será estabelecido o método (higher_hands_checker) para analisar qual mão tem as cartas de maior valor.
      Se as cartas não entrarem nessas condições descritas a próxima função de menor valor processará um novo teste.
          parametro:
            cards: vetor de entrada já ordenado
            another_cards: vetor de entrada já ordenado
          retorno:
            WIN ,LOSS '''
  def compare_one_pair(self, cards, another_cards):
    if self.hand_ratings_verifier.is_one_pair(cards):
      return self.higher_hands_checker.check_higher_one_pair(cards, another_cards, True) if self.hand_ratings_verifier.is_one_pair(another_cards) else 'WIN'
    else:
      return 'LOSS' if self.hand_ratings_verifier.is_one_pair(another_cards) else self.compare_high_card(cards, another_cards)


  '''O método compare_high_card vai comparar as duas mãos de entrada e verificar qual obteve a maior carta através do método (higher_hands_checker)
    que vai analisar qual mão contém as cartas de maior valor.
            parametro:
              cards: vetor de entrada já ordenado
              another_cards: vetor de entrada já ordenado
            retorno:
                   WIN , LOSS , DRAW'''
  def compare_high_card(self, cards, another_cards):
    return self.higher_hands_checker.check_higher_card(cards, another_cards)