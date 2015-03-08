#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

def printInicial():
    print(2*'   ',4*'♠♦♥♣',' BEM VINDO AO JOGO DE NAIPES ',4*'♠♦♥♣','\n')
    print('» Você começa inicialmente com 100 moedas.')
    print('» Nas apostas por cor você paga oito moedas.')
    print('» Nas apostas por naipe você paga quatro moedas.')
    print('» Se quiser ler mais sobre as regras digite REGRAS.')

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

def regrasJogo():
    print('\n- Cada carta do baralho possui uma cor e um naipe: ouro-vermelho, copas-vermelho, paus-preto e espada-preto.\n\n- Neste jogo, os valores das cartas e a quantidade de cartas de cada naipe presentes em um baralho não serão considerados com o objetivo de gerenciar probabilidades.\n\n- Você  inicia o jogo com um saldo de 100 MOEDAS e, a cada rodada, apostará em uma das modalidades disponíveis:\n\n* APOSTA POR NAIPE: Você  escolhe um dos naipes do baralho, e receberá o equivalente a 5 MOEDAS para cada carta daquele naipe sorteada.\nCaso todas as cartas sorteadas sejam do naipe escolhido, você receberá como prêmio 10 vezes o custo da aposta.\n\n* APOSTA POR COR: Você escolhe uma das cores de naipe, e receberá 3 MOEDAS para cada carta daquela cor escolhida que foi sorteada.\nCaso todas as cartas sorteadas sejam da cor escolhida, você receberá como prêmio 5 vezes o custo da aposta.\n\n- O jogo acaba quando você não tiver mais moedas, ou quando você digitar SAIR.\n\n-O premio será pago desconsiderando o valor que você pagou no tipo de aposta escolhida:\n\nEX: você tem 100 moedas e aposta no tipo de aposta COR que custa 8 MOEDAS; acerta 3 vezes a cor escolhida, ganha 9 MOEDAS e seu saldo atual será 101 MOEDAS.\nEX: você tem 100 MOEDAS e aposta no tipo de aposta NAIPE que custa 4 MOEDAS; acerta 2 vezes o naipe escolhido, ganha 10 MOEDAS e seu saldo atual será 106 MOEDAS.')

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+

def printApostaInvalida():
    print(20*'_-_-')
    print('\n»»» Digite uma forma de aposta válida!!!')
    
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

def saidaSaldoInsuficiente():
    print('»»» Seu saldo de moedas é insuficiente para novas apostas.\n')
    print(11*'  ',2* '♠ ♦ ♥ ♣ ♠ ')
    print(11*'  ','♣ OBRIGADO POR JOGAR, VOLTE SEMPRE ♣')
    print(20*'  ',2* '♠ ♦ ♥ ♣ ♠ ')

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
def saidaDoJogo():
    print(11*'  ',2* '♠ ♦ ♥ ♣ ♠ ')
    print(11*'  ','♣ Obrigado por jogar e volte sempre ♣')
    print(20*'  ',2* '♠ ♦ ♥ ♣ ♠ ')

#==========================================================================
def SorteioCor():
    import random
    Nparciais=[]
    cores=['preto','vermelho','vermelho','preto']
    cartas=['♠','♦','♥','♣']
    sorteio5=random.randint(0,3)#Aqui será
    sorteio6=random.randint(0,3)#sorteado os números
    sorteio7=random.randint(0,3)#para relaciona-los 
    sorteio8=random.randint(0,3)#aos elementos das listas.
    print('\n» As cores sorteadas foram:')#Nesse print abaixo irá mostar os elementos relacionados aos números sorteados.
    print('\n»',cores[sorteio5],cartas[sorteio5],',',cores[sorteio6],cartas[sorteio6],',',cores[sorteio7],cartas[sorteio7],',',cores[sorteio8],cartas[sorteio8])
    Nparciais.append(cores[sorteio5])  #As cores relacionadas
    Nparciais.append(cores[sorteio6])  #aos números sorteados
    Nparciais.append(cores[sorteio7])  #serão adicionadas
    Nparciais.append(cores[sorteio8])  #a lista Nparciais.
    return Nparciais
#===========================================================================
def SorteioNaipe():
    import random
    cartass=['espada','ouro','copas','paus']
    Nparcial=[]           #Nessa lista NúmeroParcial, será adicionado os elementos das listas "cartass" relacionado ao número sorteado para que seja contado quantos naipes foi sorteados.
    cartas=['♠','♦','♥','♣']
    sorteio1=random.randint(0,3)
    sorteio2=random.randint(0,3)
    sorteio3=random.randint(0,3)
    sorteio4=random.randint(0,3)
    print(20*'_-_-')
    print('\n» Os naipes sorteados foram:')#nesse print abaixo, vai exibir os elements da lista cartass relacionado ao núm. sorteado nos sorteios 1,2,3 e 4 acima.
    print('\n»',cartass[sorteio1],cartas[sorteio1],',',cartass[sorteio2],cartas[sorteio2],',',cartass[sorteio3],cartas[sorteio3],',',cartass[sorteio4],cartas[sorteio4])
    Nparcial.append(cartass[sorteio1])#adicionando os elementos
    Nparcial.append(cartass[sorteio2])#na lista NúmerosParciais
    Nparcial.append(cartass[sorteio3])#para que seja contado no FOR abaixo
    Nparcial.append(cartass[sorteio4])#quantos elementos o jogador acertou.
    return Nparcial
