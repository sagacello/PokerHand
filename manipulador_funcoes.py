# -- coding: utf-8 --
'''A classe manipular_funcoes é uma classe que serve de auxílio para
  manipular as funções ,alguns métodos genéricos foram criados para ajudar
  as funções em seus devidos processos'''
class Manipular_funcoes(object):

  '''O método recebe o dicionário imitando as cartas de um baralho,
      e para cada carta é atribuido um valor de acordo com as regras do poker'''
  def __init__(self):
    self.values = {
      '2': 1,
      '3': 2,
      '4': 3,
      '5': 4,
      '6': 5,
      '7': 6,
      '8': 7,
      '9': 8,
      'T': 9,
      'J': 10,
      'Q': 11,
      'K': 12,
      'A': 13
    }

  '''A função convert_to_numerical_pega somente os valores númericos do meu dicionário values
      parametro:
          cards : vetor de entrada já ordenado
      retorno:
          self.values[card[0]] : valor númerico referente a carta de cada par de carta'''
  def convert_to_numerical_value(self, card):
    return self.values[card[0]]


  '''A função sort_cards atua ordenado em ordem crescente os meus valores, e me retorna um conjunto de cartas ordenado 
        parametro:
          cards: vetor de entrada já ordenado
        retorno:
          sorted_cards :cartas ordenadas em ordem crescente '''
  def sort_cards(self, cards):
    card_values = sorted([self.convert_to_numerical_value(card) for card in cards])
    sorted_cards = []
    for card in cards:
      sorted_cards.insert(card_values.index(self.convert_to_numerical_value(card)), card)
      del card_values[card_values.index(self.convert_to_numerical_value(card))]
    return sorted_cards


  '''A função get_four_of_a_kind_value verifica qual carta se repete para formar uma quadra.  
          parametro:
            cards: vetor de entrada já ordenado
          retorno:
            card[0]: carta que forma a quadra'''
  def get_four_of_a_kind_value(self, cards):
    for card in cards:
      if [card[0] for card in cards].count(card[0]) == 4:
        return card[0]


  '''A função get_three_of_a_kind_value verifica qual carta se repete para formar uma trinca.  
            parametro:
              cards: vetor de entrada já ordenado
            retorno:
              card[0]: carta que forma a trinca'''
  def get_three_of_a_kind_value(self, cards):
    for card in cards:
      if [card[0] for card in cards].count(card[0]) == 3:
        return card[0]


  '''A função get_three_of_a_kind_value verifica qual carta se repete para formar um par.  
            parametro:
                cards: vetor de entrada já ordenado
            retorno:
                card[0]: carta que forma um par'''
  def get_one_pair_value(self, cards):
    for card in cards:
      if [card[0] for card in cards].count(card[0]) == 2:
        return card[0]


  '''A função  get_higher_card_value verifica qual maior carta na mao .  
            parametro:
              cards :vetor de entrada já ordenado
            retorno:
              cards[len(cards)-1][0]: maior carta da mão mantendo o naipe '''
  def get_higher_card_value(self, cards):
    return cards[len(cards)-1][0]


  '''A slice_one_pair_ separa um par do meu conjunto de cartas.  
            parametro:
                cards: vetor de entrada já ordenado
            retorno:
                cards: cartas sem o par que foi retirado'''
  def slice_one_pair(self, cards):
    return list(filter(lambda x: x[0] != self.get_one_pair_value(cards), cards))


  '''A função slice_by_card separa uma carta do meu conjunto de cartas.  
            parametro:
                cards: vetor de entrada já ordenado
            retorno:
                cards: cartas sem a carta que foi retirada'''
  def slice_by_card(self, cards, card):
    return list(filter(lambda x: x[0] != card[0], cards))