# -- coding: utf-8 --
from pokerhand import PokerHand

'''Importa os mecanismos necessários para iniciar o algoritimo
    nesse arquivo sera mostrado 'WIN' ou 'LOSS em ordem de colocação'''

print(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5C 5H AC")))  # WIN1
print(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")))  # LOSS2
print(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")))  # WIN3
print(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")))  # LOSS4
print(PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")))  # LOSS5 #
print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")))  # WIN6
print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")))  # WIN7
print(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")))  # WIN8
print(PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")))  # WIN9 #
print(PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")))  # WIN10
print(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")))  # WIN11
print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")))  # WIN12
print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")))  # WIN13
print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")))  # WIN14
print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))  # WIN15
print(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))  # WIN16
print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")))  # WIN17
print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")))  # WIN18
print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")))  # WIN19
print(PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")))  # WIN20
print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")))  # WIN21 #
print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))  # LOSS22
print(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))  # WIN23
print(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")))  # LOSS24
print(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")))  # WIN25
print(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")))  # WIN26

