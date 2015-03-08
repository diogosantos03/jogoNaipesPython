                         #MINI-PROJETO JOGO DE NAIPES.

#Uso de recursos: (laços de repetição, estruturas de decisão, funções e listas)
                                #DIOGO SANTOS

import BBprojeto
Moedas=100
PrintRegras=BBprojeto.printInicial()
tipodeaposta=str.lower(input('\n\n» Vai apostar na COR ou NAIPE?\n\n» Qual tipo de aposta: '))#Entrada para a escolha do tipo de aposta.
if(tipodeaposta=='regras'):
    Regras=BBprojeto.regrasJogo()
while(tipodeaposta!='sair')and(Moedas>=4):          
    ValorApostaNaipes=4            #Valor das apostas nos naipes.
    ValorApostaCor=8               #Valor das apostas nas cores.
    PremioCor=3                    #Valor do premio para cada cor escolhida que tenha sido sorteada.
    PremioNaipes=5                 #Valor do premio para cada naipe escolhido que tenha sido sortedo.
    QuantCoresSorteadas=0#Contador de quantas vezes a cor escolhida foi sorteada.
    QuantNaipesSorteados=0#Contador de quandas vezes o naipe escolhido foi sorteado.
    if(tipodeaposta=='cor'):
        if(Moedas<ValorApostaCor):
            print(20*'----')
            print('»»» Saldo insuficiente, mas você ainda pode apostar no NAIPE.')
        else:
            cor=str.lower(input('\n» VERMELHO de {Ouro♦ e Copas♥} ou PRETO de {Espada♠ e Paus♣}\n\n» Qual cor você quer apostar nos naipes?\n\n» Digite a cor: '))#entrada para escolha da cor a ser apostada.
            if(cor!='vermelho')and(cor!='preto')and(cor!='regras'):
                PrintApostaInvalida=BBprojeto.printApostaInvalida()#Chama a função com os print's de apostas inválidas.
            elif(cor=='regras'):
                Regras=BBprojeto.regrasJogo()#Chama a função com todas as regras do jogo.
            else:
                print(20*'_-_-')
                Moedas-=ValorApostaCor#Aqui é debitado as moedas relacionado a aposta por cor.
                SortCor=BBprojeto.SorteioCor()
                #Chama a função com os sorteios das Cores.
                for D in range(0,4,1):           #|=>Aqui irá comparar
                    if(cor==SortCor[D]):         #|=>os elementos que estão na lista
                        QuantCoresSorteadas+=1   #|=>e contar os que são iguais ao apostado pelo usuário.
                if(QuantCoresSorteadas>0)and(QuantCoresSorteadas<4):
                    Pnaipes=QuantCoresSorteadas*PremioCor#Calcula a quantidade de cor escolhida que foi sorteada pelo valor do premio.
                    Moedas=Moedas+Pnaipes#Soma os valores anteriormente calculados as moedas existentes.
                    print('\n»»» Você acertou',QuantCoresSorteadas,'vezes a cor',cor,'.')
                    print('\n»»» Você ganhou',Pnaipes,'moedas.')
                elif(QuantCoresSorteadas==4):#Se sorteou quatro das cores das apostada pelo usuário
                    Pnaipes=ValorApostaCor*5 #irá ganhar cinco vezes o valor da aposta.
                    Moedas=Moedas+Pnaipes
                    print('\n»»» Você acertou',QuantCoresSorteadas,'vezes a cor',cor,'.')
                    print('\n»»» Você ganhou',Pnaipes,'moedas.')
                else:
                    print('\n»»» Infelismente você não acertou nenhum naipe da cor',cor,'.')
    elif(tipodeaposta=='naipe'):
        if(Moedas<ValorApostaNaipes):
            print(20*'----')
            print('»»» Saldo insuficiente')
        else:
            naipes=str.lower(input('\nEspada♠, ouro♦, copas♥ ou paus♣:\n\n» Vai apostar em qual naipe?\n\n» Digite o naipe: '))
            if(naipes!='espada')and(naipes!='ouro')and(naipes!='copas')and(naipes!='paus')and(naipes!='regras'):
                PrintApostaInvalida=BBprojeto.printApostaInvalida()#Chama a função com os print's de apostas inválidas.
            elif(naipes=='regras'):
                Regras=BBprojeto.regrasJogo()#Chama a função com todas as regras do jogo.
            else:
                Moedas-=ValorApostaNaipes
                SortNaipe=BBprojeto.SorteioNaipe()#Chama a função com os sorteios dos naipes.
                for i in range(0,4,1):
                    if(naipes==SortNaipe[i]):
                        QuantNaipesSorteados+=1
                if(QuantNaipesSorteados>0)and(QuantNaipesSorteados<4):
                    Pnaipes=QuantNaipesSorteados*PremioNaipes
                    Moedas=Moedas+Pnaipes
                    print('\n»»» Você acertou',QuantNaipesSorteados,'naipes de',naipes,'.')
                    print('\n»»» Você ganhou',Pnaipes,'moedas.')
                elif(QuantNaipesSorteados==4):
                    Pnaipes=ValorApostaNaipes*10#Se acertou todos os 4, ganhará 10X o valor da aposta.
                    Moedas=Moedas+Pnaipes
                    print('\n»»» Parabéns, você acertou todos os naipes e ganhou',Pnaipes,'.')
                else:
                    print('\n»»» Infelismente você não acertou nenhum naipe de',naipes,'.')
    else:
        if(tipodeaposta=='regras'):
            print('\n»»» Já leu as regras, agora vamos lá!!!')
        else:
            PrintApostaInvalida=BBprojeto.printApostaInvalida()
    print('\n»»» Seu saldo é:',Moedas,'moedas.\n')
    if(Moedas<4):
        SairDoJogo=BBprojeto.saidaSaldoInsuficiente()#Chama a função com os prints de saida de jogo.
    else:
        print(20*'----')
        tipodeaposta=str.lower(input('» Se quiser, pode digitar SAIR para sair do jogo.\n» Lembrando, se quiser ler as regras digite REGRAS.\n\n» Vai apostar na COR ou NAIPE?\n\n» Qual tipo de aposta: '))
        if(tipodeaposta=='regras'):
            regras=BBprojeto.regrasJogo()
if(tipodeaposta=='sair'):
    print('\n» Você entrou no jogo com 100 moedas e vai saindo com',Moedas,'moedas.\n\n')
    SairJogo=BBprojeto.saidaDoJogo()#Chama a função com os prints de saida de jogo.
                        
