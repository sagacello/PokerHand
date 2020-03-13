# Introdução!

Desafio:
  - Construir um algoritmo que simule uma comparação entre duas mãos de poker.
  - As características da sequência de cartas são:
    - Um espaço é usado como separador das cartas
    * Cada carta consiste em dois caracteres
    * O primeiro caractere é o valor da carta, os caracteres válidos são:
        2, 3, 4, 5, 6, 7, 8, 9, T (dez), J (jack), Q (queen), K (king), A (ace)
    * O segundo caractere representa o naipe, os caracteres válidos são:
        S (Spades), H (Hearts), D (Diamonds), C (Clubs)
 - O resultado deve ter dois valores possíveis que representarão os seguintes estados: WIN ou LOSS.
# Resumo do programa
O algoritmo resolve o problema proposto para qualquer teste que envolva as regras de poker , com a entrada 
de duas mãos de poker para serem comparadas o programa retorna 'WIN' , 'LOSS' e tambem pode retornar 'DRAW'
dependendo da jogada ,seguindo as regras do jogo e levando como premissa o uso de somente um baralho e de que
os naipes não tem valor.O algoritmo foi criado com uma arquitetura onde as funções que comparam as entradas das mão de poker 
são analisadas através de funções de valor decrescente de acordo com a regra do jogo ,ou seja ,o processo começa
na maior jogada e vai decaindo de jogada até a de menor valor.



 

## Ambiente 


 - python 3.7

##  Testando a aplicação
```
 $ python principal.py 
```

   Aqui a aplicação mostrará todos os resultados das comparações entre as mãos em ordem de entrada de vetores.
```
 $ python test.py 
 ```

   - Aqui a aplicação realizará os testes unitários e os resultados serão mostrados em ordem de processamento de
    acordo com a arquitetura do projeto.

Referência
----
- Regras : https://www.pokerstars.com/br/poker/games/rules/?no_redirect=1


