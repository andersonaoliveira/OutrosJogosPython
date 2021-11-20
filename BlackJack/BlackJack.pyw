from graphics import *
import random

def principal():

    #DEFINIÇÃO DOS ITENS DA TELA
    win = GraphWin("BlackJack", 800,550)
    win.setBackground("green")
    linhabranca1 = Rectangle(Point(120, 35), Point(680, 165))
    linhabranca2 = Rectangle(Point(120, 335), Point(680, 465))
    linhabranca1.setOutline("white")
    linhabranca1.setFill("white")
    linhabranca2.setOutline("white")
    linhabranca2.setFill("white")
    linhabranca1.draw(win)
    linhabranca2.draw(win)
    cartavirada = Image(Point(45,65),"carta virada.gif")
    cartavirada.draw(win)
    manter = Rectangle(Point(50, 500), Point(100, 525))
    comprar = Rectangle(Point(175, 500), Point(225, 525))
    inicio = Rectangle(Point(2, 2), Point(85,130))
    linha = Line(Point(0,200),Point(800,200))
    linha.setOutline("yellow")
    manter.setFill("white")
    comprar.setFill("black")
    sortear = Text(Point(44,25), "Sortear")
    sortear.setStyle("bold")
    sortear.setTextColor("white")
    sortear.draw(win)
    textomanter=Text(Point(75,485),"Manter")
    textomanter.draw(win)
    textopegar=Text(Point(200,485),"Comprar")
    textopegar.draw(win)
    manter.draw(win)
    comprar.draw(win)
    inicio.draw(win)
    linha.draw(win)

    #VARIÁVEIS INICIADAS E VALORES DAS CARTAS
    jogo = 1
    sorteio = 1
    saida = 0
    pontocartanova = 350
    
    vale1 = "c1 e1 o1 p1"
    vale2 = "c2 e2 o2 p2"
    vale3 = "c3 e3 o3 p3"
    vale4 = "c4 e4 o4 p4"
    vale5 = "c5 e5 o5 p5"
    vale6 = "c6 e6 o6 p6"
    vale7 = "c7 e7 o7 p7"
    vale8 = "c8 e8 o8 p8"
    vale9 = "c9 e9 o9 p9"
    vale10 = "c10 e10 o10 p10 c11 e11 o11 p11 c12 e12 o12 p12 c13 e13 o13 p13"
    listavalores = " ",vale1,vale2,vale3,vale4,vale5,vale6,vale7,vale8,vale9,vale10
    #SORTEAR AS CARTAS
    cartas = "c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13 e1 e2 e3 e4 e5 e6 e7 e8 e9 e10 e11 e12 e13 o1 o2 o3 o4 o5 o6 o7 o8 o9 o10 o11 o12 o13 p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13".split()
    random.shuffle(cartas)
    contdecartas = 0


    #Pontuação
    computador = 0
    jogador = 0
    cartaAS = 0
    cartaASPC = 0
    pontosjogador = 0
    pontoscomputador = 0

    
    #CLICAR NA AREA ADEQUADA PARA INICIAR O JOGO
    while jogo == 1:
        p = win.getMouse()
        x = p.x
        y = p.y
        if x>2 and x<85 and y>2 and y<130 and sorteio == 1:
            cartadefinida = "{}.gif".format(cartas[contdecartas])
            carta0 = Image(Point(170,100),(cartadefinida))
            carta0.draw(win)
            contdecartas = contdecartas + 1
            cartadefinida = "{}.gif".format(cartas[contdecartas])
            carta1 = Image(Point(260,100),(cartadefinida))
            carta1.draw(win)
            contdecartas = contdecartas + 1
            cartadefinida = "{}.gif".format(cartas[contdecartas])
            carta2 = Image(Point(170,400),(cartadefinida))
            carta2.draw(win)
            contdecartas = contdecartas + 1
            cartadefinida = "{}.gif".format(cartas[contdecartas])
            carta3 = Image(Point(260,400),(cartadefinida))
            carta3.draw(win)
            contdecartas = contdecartas + 1
            for i in range (1,11):
                if cartas[0] in listavalores[i]:
                    computador += i
                    if i == 1:
                        cartaASPC +=1
                        computador -= 10
            for i in range (1,11):
                if cartas[1] in listavalores[i]:
                    computador += i
                    if i == 1:
                        cartaASPC +=1
                        computador -= 10
            for i in range (1,11):
                if cartas[2] in listavalores[i]:
                    jogador += i
                    if i == 1:
                        cartaAS +=1
                        jogador -= 10
            for i in range (1,11):
                if cartas[3] in listavalores[i]:
                    jogador += i
                    if i == 1:
                        cartaAS +=1
                        jogador -= 10

            sorteio = 0 #SORTEIO
        if x>50 and x<100 and y>500 and y<525 and sorteio == 0 and jogador <= 21:
            if cartaAS != 0 and jogador <= 11:
                pontosjogador = jogador + 10
            else:
                pontosjogador = jogador
            if cartaASPC != 0 and computador <= 11:
                pontoscomputador = computador + 10
            else:
                pontoscomputador = computador
            scorecomputador = 21-pontoscomputador
            scorejogador = 21-pontosjogador
            if scorecomputador < scorejogador:
                cxperdeu = Rectangle(Point(60, 80), Point(740, 380))
                cxperdeu.setOutline("white")
                cxperdeu.setFill("white")
                cxperdeu.draw(win)
                txtperdeu = Text(Point(400,180), "QUE PENA, VOCÊ PERDEU!")
                txtperdeu.setTextColor("red")
                txtperdeu.setStyle("bold")
                txtperdeu.setSize(20)
                txtperdeu.draw(win)

                win.getMouse()
                
                cxfimdejogo = Rectangle(Point(60, 80), Point(740, 380))
                cxfimdejogo.setOutline("black")
                cxfimdejogo.setFill("black")
                cxfimdejogo.draw(win)
                cxreiniciar = Rectangle(Point(80, 260), Point(280, 360))
                cxreiniciar.setOutline("green")
                cxreiniciar.setFill("green")
                cxreiniciar.draw(win)
                cxterminar = Rectangle(Point(520, 260), Point(720, 360))
                cxterminar.setOutline("red")
                cxterminar.setFill("red")
                cxterminar.draw(win)
                txtperguntasair = Text(Point(400,180), "O QUE VOCÊ DESEJA FAZER?")
                txtreiniciar = Text(Point(180,310), "REINICIAR")
                txtterminar = Text(Point(620,310), "SAIR")
                txtperguntasair.setTextColor("white")
                txtreiniciar.setTextColor("white")
                txtterminar.setTextColor("white")
                txtperguntasair.setStyle("bold")
                txtperguntasair.setSize(20)
                txtreiniciar.draw(win)
                txtterminar.draw(win)
                txtperguntasair.draw(win)

                while saida == 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>520 and x<720 and y>260 and y<360:
                        saida = 1
                        #fechar o jogo
                        win.close()
                    if x>80 and x<280 and y>260 and y<360:
                        saida = 1
                        #continuar
                        win.close()
                        principal() #VOCÊ PERDEU

            if scorecomputador == scorejogador:
                cxperdeu = Rectangle(Point(60, 80), Point(740, 380))
                cxperdeu.setOutline("white")
                cxperdeu.setFill("white")
                cxperdeu.draw(win)
                txtempatou = Text(Point(400,180), "A PARTIDA TERMINOU EMPATADA!")
                txtempatou.setTextColor("black")
                txtempatou.setStyle("bold")
                txtempatou.setSize(20)
                txtempatou.draw(win)

                win.getMouse()
                
                cxfimdejogo = Rectangle(Point(60, 80), Point(740, 380))
                cxfimdejogo.setOutline("black")
                cxfimdejogo.setFill("black")
                cxfimdejogo.draw(win)
                cxreiniciar = Rectangle(Point(80, 260), Point(280, 360))
                cxreiniciar.setOutline("green")
                cxreiniciar.setFill("green")
                cxreiniciar.draw(win)
                cxterminar = Rectangle(Point(520, 260), Point(720, 360))
                cxterminar.setOutline("red")
                cxterminar.setFill("red")
                cxterminar.draw(win)
                txtperguntasair = Text(Point(400,180), "O QUE VOCÊ DESEJA FAZER?")
                txtreiniciar = Text(Point(180,310), "REINICIAR")
                txtterminar = Text(Point(620,310), "SAIR")
                txtperguntasair.setTextColor("white")
                txtreiniciar.setTextColor("white")
                txtterminar.setTextColor("white")
                txtperguntasair.setStyle("bold")
                txtperguntasair.setSize(20)
                txtreiniciar.draw(win)
                txtterminar.draw(win)
                txtperguntasair.draw(win)

                while saida == 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>520 and x<720 and y>260 and y<360:
                        saida = 1
                        #fechar o jogo
                        win.close()
                    if x>80 and x<280 and y>260 and y<360:
                        saida = 1
                        #continuar
                        win.close()
                        principal() #EMPATOU

            if scorecomputador > scorejogador:
                cxperdeu = Rectangle(Point(60, 80), Point(740, 380))
                cxperdeu.setOutline("white")
                cxperdeu.setFill("white")
                cxperdeu.draw(win)
                txtempatou = Text(Point(400,180), "QUEM DIRIA, VOCÊ VENCEU!")
                txtempatou.setTextColor("blue")
                txtempatou.setStyle("bold")
                txtempatou.setSize(20)
                txtempatou.draw(win)

                win.getMouse()
                
                cxfimdejogo = Rectangle(Point(60, 80), Point(740, 380))
                cxfimdejogo.setOutline("black")
                cxfimdejogo.setFill("black")
                cxfimdejogo.draw(win)
                cxreiniciar = Rectangle(Point(80, 260), Point(280, 360))
                cxreiniciar.setOutline("green")
                cxreiniciar.setFill("green")
                cxreiniciar.draw(win)
                cxterminar = Rectangle(Point(520, 260), Point(720, 360))
                cxterminar.setOutline("red")
                cxterminar.setFill("red")
                cxterminar.draw(win)
                txtperguntasair = Text(Point(400,180), "O QUE VOCÊ DESEJA FAZER?")
                txtreiniciar = Text(Point(180,310), "REINICIAR")
                txtterminar = Text(Point(620,310), "SAIR")
                txtperguntasair.setTextColor("white")
                txtreiniciar.setTextColor("white")
                txtterminar.setTextColor("white")
                txtperguntasair.setStyle("bold")
                txtperguntasair.setSize(20)
                txtreiniciar.draw(win)
                txtterminar.draw(win)
                txtperguntasair.draw(win)

                while saida == 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>520 and x<720 and y>260 and y<360:
                        saida = 1
                        #fechar o jogo
                        win.close()
                    if x>80 and x<280 and y>260 and y<360:
                        saida = 1
                        #continuar
                        win.close()
                        principal() #VOCÊ VENCEU
        if x>175 and x<225 and y>500 and y<525 and sorteio == 0 and jogador < 21:
            cartadefinida = "{}.gif".format(cartas[contdecartas])
            carta0 = Image(Point(pontocartanova,400),(cartadefinida))
            carta0.draw(win)
            for i in range (1,11):
                if cartas[contdecartas] in listavalores[i]:
                    jogador += i
                    if i == 1:
                        cartaAS +=1
                        jogador -= 10
            contdecartas = contdecartas + 1
            pontocartanova += 90 #COMPRAR
            if jogador > 21 and sorteio == 0:
                cxperdeu = Rectangle(Point(60, 80), Point(740, 380))
                cxperdeu.setOutline("white")
                cxperdeu.setFill("white")
                cxperdeu.draw(win)
                txtperdeu = Text(Point(400,180), "PASSOU DE 21, VOCÊ PERDEU!")
                txtperdeu.setTextColor("red")
                txtperdeu.setStyle("bold")
                txtperdeu.setSize(20)
                txtperdeu.draw(win)

                win.getMouse()

                cxfimdejogo = Rectangle(Point(60, 80), Point(740, 380))
                cxfimdejogo.setOutline("black")
                cxfimdejogo.setFill("black")
                cxfimdejogo.draw(win)
                cxreiniciar = Rectangle(Point(80, 260), Point(280, 360))
                cxreiniciar.setOutline("green")
                cxreiniciar.setFill("green")
                cxreiniciar.draw(win)
                cxterminar = Rectangle(Point(520, 260), Point(720, 360))
                cxterminar.setOutline("red")
                cxterminar.setFill("red")
                cxterminar.draw(win)
                txtperguntasair = Text(Point(400,180), "O QUE VOCÊ DESEJA FAZER?")
                txtreiniciar = Text(Point(180,310), "REINICIAR")
                txtterminar = Text(Point(620,310), "SAIR")
                txtperguntasair.setTextColor("white")
                txtreiniciar.setTextColor("white")
                txtterminar.setTextColor("white")
                txtperguntasair.setStyle("bold")
                txtperguntasair.setSize(20)
                txtreiniciar.draw(win)
                txtterminar.draw(win)
                txtperguntasair.draw(win)

                while saida == 0:
                    p = win.getMouse()
                    x = p.x
                    y = p.y
                    if x>520 and x<720 and y>260 and y<360:
                        saida = 1
                        #fechar o jogo
                        win.close()
                    if x>80 and x<280 and y>260 and y<360:
                        saida = 1
                        #continuar
                        win.close()
                        principal() #FIM DE JOGO

                    
principal()






    
        

