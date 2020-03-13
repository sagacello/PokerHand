# -- coding: utf-8 --
from comparar_jogadas import Comparador_pokerhands
from manipulador_funcoes import Manipular_funcoes


'''Para a classe PokerHand foi construído um método que receberá o vetor de entrada que simula uma mão de poker, onde cada carta está no formato:(valor_númerico)(string)
que representam respectivamente o valor númerico da carta e o seu naipe.
Observação: O método que chama a função compare_royal_flush foi estruturado para começar a comparção do tipo de jogada mais valiosa e ir decrescendo de jogada'''

class PokerHand(object):

    ''' hand_comparator vai buscar a classe que fará as comparações entre as duas mãos
        hand_manipulator vai buscar uma classe que serve como auxílio para manipulação de funções
        card representa o vetor de entrada que será tratado de acordo com os métodos atribuidos a ele
            parametros:
                cards : vetor que simula a entrada de uma mão de poker
            retorno:
                Instancias da classe '''

    def __init__(self, cards):
        self.hand_comparator = Comparador_pokerhands()
        self.hand_manipulator = Manipular_funcoes()
        self.cards = self.hand_manipulator.sort_cards(cards.split())


    '''A função compare_with iniciará a comparação dos métodos que devem gerar as comparações
        entre as mãos poker e a partir destes métodos o resultado final é originado.
            parametros : 
                cards : vetor que simula  uma mão de cartas
                another_poker_hand: outro vetor que simula uma mão de cartas
                
            retorno :  
                'WIN' ,'LOSS' (resultados finais).'''
    def compare_with(self, another_poker_hand):
        return self.hand_comparator.compare_royal_flush(self.cards, another_poker_hand.cards)