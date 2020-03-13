# -- coding: utf-8 --
from pokerhand import PokerHand
import unittest

'''A classe PokerHandTest obtem os  mecanismos necessários para iniciar os testes '''
class PokerHandTest(unittest.TestCase):

    ''' Cada função dessa classe corresponde a um teste que será realizddo para cada vetor de entrada,
        esses vetores  correspondem  respectivamente as duas mãos de poker que devem ser comparadas ,
        sendo atribuidos em handOne e handTwo a classe que origina todos os métodos necessários para tratar
        esses vetores de acordo com as regras do poker. '''
    def test_um(self):
        handOne = PokerHand("TC TH 5C 5H KH")
        handTwo = PokerHand("9C 9H 5C 5H AC")
        result = handOne.compare_with(handTwo)
        self.assertTrue('WIN', result)
        print(f'test_um == {result}')


    def test_dois(self):
        handOne = PokerHand("TS TD KC JC 7C")
        handTwo = PokerHand("JS JC AS KC TD")
        result = handOne.compare_with(handTwo)
        self.assertTrue("LOSS", result)
        print(f'test_dois == {result}')

    def test_tres(self):
        handOne = PokerHand("7H 7C QC JS TS")
        handTwo = PokerHand("7D 7C JS TS 6D")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_tres == {result}')

    def test_quatro(self):
        handOne = PokerHand("5S 5D 8C 7S 6H")
        handTwo = PokerHand("7D 7S 5S 5D JS")
        result = handOne.compare_with(handTwo)
        self.assertEqual("LOSS", result)
        print(f'test_quatro == {result}')

    def test_cinco(self):
        handOne = PokerHand("AS AD KD 7C 3D")
        handTwo = PokerHand("AD AH KD 7C 4S")
        result = handOne.compare_with(handTwo)
        self.assertEqual("LOSS", result)
        print(f'test_cinco == {result}')

    def test_seis(self):
        handOne = PokerHand("TS JS QS KS AS")
        handTwo = PokerHand("AC AH AS AS KS")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_seis == {result}')

    def test_sete(self):
        handOne = PokerHand("TS JS QS KS AS")
        handTwo = PokerHand("TC JS QC KS AC")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_sete == {result}')

    def test_oito(self):
        handOne = PokerHand("TS JS QS KS AS")
        handTwo = PokerHand("QH QS QC AS 8H")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_oito == {result}')

    def test_nove(self):
        handOne = PokerHand("AC AH AS AS KS")
        handTwo = PokerHand("TC JS QC KS AC")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_nove == {result}')


    def test_dez(self):
        handOne = PokerHand("AC AH AS AS KS")
        handTwo = PokerHand("QH QS QC AS 8H")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_dez == {result}')

    def test_onze(self):
        handOne = PokerHand("TC JS QC KS AC")
        handTwo = PokerHand("QH QS QC AS 8H")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_onze == {result}')

    def test_doze(self):
        handOne = PokerHand("7H 8H 9H TH JH")
        handTwo = PokerHand("JH JC JS JD TH")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_doze == {result}')

    def test_treze(self):
        handOne = PokerHand("7H 8H 9H TH JH")
        handTwo = PokerHand("4H 5H 9H TH JH")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_treze == {result}')

    def test_quatorze(self):
        handOne = PokerHand("7H 8H 9H TH JH")
        handTwo = PokerHand("7C 8S 9H TH JH")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_quatorze == {result}')

    def test_quinze(self):
        handOne = PokerHand("7H 8H 9H TH JH")
        handTwo = PokerHand("TS TH TD JH JD")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_quinze == {result}')

    def test_dezesseis(self):
        handOne = PokerHand("7H 8H 9H TH JH")
        handTwo = PokerHand("JH JD TH TC 4C")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_dezesseis == {result}')

    def test_dezessete(self):
        handOne = PokerHand("JH JC JS JD TH")
        handTwo = PokerHand("4H 5H 9H TH JH")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_dezessete == {result}')

    def test_dezoito(self):
        handOne = PokerHand("JH JC JS JD TH")
        handTwo = PokerHand("7C 8S 9H TH JH")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_dezoito == {result}')

    def test_dezenove(self):
        handOne = PokerHand("JH JC JS JD TH")
        handTwo = PokerHand("TS TH TD JH JD")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_dezenove == {result}')

    def test_vinte(self):
        handOne = PokerHand("JH JC JS JD TH")
        handTwo = PokerHand("JH JD TH TC 4C")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_vinte == {result}')

    def test_vinte_um(self):
        handOne = PokerHand("4H 5H 9H TH JH")
        handTwo = PokerHand("7C 8S 9H TH JH")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_vinte_um == {result}')

    def test_vinte_dois(self):
        handOne = PokerHand("4H 5H 9H TH JH")
        handTwo = PokerHand("TS TH TD JH JD")
        result = handOne.compare_with(handTwo)
        self.assertEqual("LOSS", result)
        print(f'test_vinte_dois == {result}')

    def test_vinte_tres(self):
        handOne = PokerHand("4H 5H 9H TH JH")
        handTwo = PokerHand("JH JD TH TC 4C")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_vinte_tres == {result}')

    def test_vinte_quatro(self):
        handOne = PokerHand("7C 8S 9H TH JH")
        handTwo = PokerHand("TS TH TD JH JD")
        result = handOne.compare_with(handTwo)
        self.assertEqual("LOSS", result)
        print(f'test_vinte_quatro == {result}')

    def test_vinte_cinco(self):
        handOne = PokerHand("7C 8S 9H TH JH")
        handTwo = PokerHand("JH JD TH TC 4C")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_vinte_cinco == {result}')

    def test_vinte_seis(self):
        handOne = PokerHand("TS TH TD JH JD")
        handTwo = PokerHand("JH JD TH TC 4C")
        result = handOne.compare_with(handTwo)
        self.assertEqual("WIN", result)
        print(f'test_vinte_seis == {result}')

#unittest.main()
if __name__ == '__main__':
    unittest.main()