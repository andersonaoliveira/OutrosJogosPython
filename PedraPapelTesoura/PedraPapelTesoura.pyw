from graphics import *
import random
import time

def abertura():
    win = GraphWin("Pedra, Papel ou Tesoura", 800, 600)
    win.setBackground(color_rgb (250,250,250))
    
    #Apresentação do jogo
    jogar = Text(Point(400,50), '''Bora jogar, mas antes leia as REGRAS:  
1 - A pedra vence a tesoura, tesoura vence papel e papel vence pedra!
2 - Escolha uma das opções abaixo para o jogo começar!!''')
    jogar.setTextColor(color_rgb(0,0,0))
    jogar.setStyle("bold")
    jogar.setSize(12)
    jogar.draw(win)

    pedra=Image(Point(200,300), "imagens/pedra1.png")
    pedra.draw(win)

    papel=Image(Point(400,300), "imagens/papel1.png")
    papel.draw(win)
    
    tesoura=Image(Point(600,300), "imagens/tesoura1.png")
    tesoura.draw(win)

    escolha = 0
    loop = 1

    while loop != 0:
        m = win.getMouse()
        x = m.x
        y = m.y
        if x>112 and x<289 and y>205 and y<393:
            escolha = 1
            x = 0
            y = 0
        if x>304 and x<488 and y>193 and y<403:
            escolha = 2
            x = 0
            y = 0
        if x>536 and x<662 and y>199 and y<406:
            escolha = 3
            x - 0
            y = 0
        
        if escolha != 0:
            jogar.undraw()
            time.sleep(0.5)
            pedra.undraw()
            time.sleep(1)
            papel.undraw()
            time.sleep(2)
            tesoura.undraw()
            time.sleep(2)
            if escolha == 1:
                pedra=Image(Point(400,200), "imagens/pedra1.png")
                pedra.draw(win)
            if escolha == 2:
                papel=Image(Point(400,200), "imagens/papel1.png")
                papel.draw(win)
            if escolha == 3:
                tesoura=Image(Point(400,200), "imagens/tesoura1.png")
                tesoura.draw(win)
            loop = 0

    jogar = Text(Point(400,50), "Ótimo, agora que você já sabe como funciona\nVamos AO JOGO!!\nClique na sua mão para iniciar a partida.")
    jogar.setTextColor(color_rgb(0,0,0))
    jogar.setStyle("bold")
    jogar.setSize(12)
    jogar.draw(win)
    loop2 = 1
    while loop2 != 0:
        n = win.getMouse()
        x = n.x
        y = n.y
        if x>305 and x<493 and y>93 and y<309:
            loop2 = 0
            time.sleep(1)
            win.close()
            principal()


def principal():
    win = GraphWin("Pedra, Papel ou Tesoura", 800, 600)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(1)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.8)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.6)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.6)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.5)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.5)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.5)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.4)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.4)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.4)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.4)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.2)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.2)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.2)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.1)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.1)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.1)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.1)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.05)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.05)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.05)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.05)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.01)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.01)
    win.setBackground(color_rgb (250,250,250))
    explosao=Image(Point(400,300), "imagens/explosao.png")
    explosao.draw(win)
    time.sleep(0.01)
    win.setBackground(color_rgb (0,0,0))
    explosao.undraw()
    time.sleep(0.01)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.01)
    win.setBackground(color_rgb (0,0,0))
    explosao=Image(Point(400,300), "imagens/explosao.png")
    explosao.draw(win)
    time.sleep(0.01)
    win.setBackground(color_rgb (250,250,250))
    explosao.undraw()
    time.sleep(0.01)
    win.setBackground(color_rgb (0,0,0))
    time.sleep(0.01)
    win.setBackground(color_rgb (250,250,250))
    time.sleep(0.01)
    win.setBackground(color_rgb (0,0,0))
    explosao=Image(Point(400,300), "imagens/explosao.png")
    explosao.draw(win)
    time.sleep(0.01)
    explosao.undraw()
    time.sleep(0.1)
    win.setBackground(color_rgb (255,127,0))
    linha1 = Line(Point(0,50),Point(800,50))
    linha1.setOutline("black")
    linha1.setWidth(3)

    caixatitulo = Rectangle(Point(0,0),Point(800,50))
    caixatitulo.setFill("black")
    caixatitulo.setOutline("black")
    caixatitulo.draw(win)
    vidavoce = Rectangle(Point(10,80),Point(310,120))
    vidavoce.setOutline("white")
    vidavoce.draw(win)
    vidapc = Rectangle(Point(490,80),Point(790,120))
    vidapc.setOutline("white")
    vidapc.draw(win)
    titulo = Text(Point(400,25), "PEDRA - PAPEL - TESOURA")
    titulo.setTextColor("white")
    titulo.setStyle("bold")
    titulo.setSize(24)
    titulo.draw(win)
    txtvoce = Text(Point(40,65), "VOCÊ")
    txtvoce.setTextColor("black")
    txtvoce.setStyle("bold")
    txtvoce.setSize(12)
    txtvoce.draw(win)
    txtcomputador = Text(Point(720,65), "COMPUTADOR")
    txtcomputador.setTextColor("black")
    txtcomputador.setStyle("bold")
    txtcomputador.setSize(12)
    txtcomputador.draw(win)
    time.sleep(0.4)
    vidavoce20 = Rectangle(Point(11,81),Point(69,119))
    vidavoce20.setFill("red")
    vidavoce20.draw(win)    
    vidapc20 = Rectangle(Point(729,81),Point(789,119))
    vidapc20.setFill("red")
    vidapc20.draw(win)
    time.sleep(0.4)
    vidavoce40 = Rectangle(Point(11,81),Point(129,119))
    vidavoce40.setFill("orange")
    vidavoce40.draw(win)    
    vidapc40 = Rectangle(Point(669,81),Point(789,119))
    vidapc40.setFill("orange")
    vidapc40.draw(win)
    time.sleep(0.4)
    vidavoce60 = Rectangle(Point(11,81),Point(189,119))
    vidavoce60.setFill("green")
    vidavoce60.draw(win)
    vidapc60 = Rectangle(Point(609,81),Point(789,119))
    vidapc60.setFill("green")
    vidapc60.draw(win)
    time.sleep(0.4)
    vidavoce80 = Rectangle(Point(11,81),Point(249,119))
    vidavoce80.setFill("green")
    vidavoce80.draw(win)
    vidapc80 = Rectangle(Point(549,81),Point(789,119))
    vidapc80.setFill("green")
    vidapc80.draw(win)
    time.sleep(0.4)
    vidavoce100 = Rectangle(Point(11,81),Point(309,119))
    vidavoce100.setFill("green")
    vidavoce100.draw(win)
    vidapc100 = Rectangle(Point(489,81),Point(789,119))
    vidapc100.setFill("green")
    vidapc100.draw(win)    
    time.sleep(0.4)
    vidavoce = Rectangle(Point(10,80),Point(310,120))
    vidavoce.setOutline("black")
    vidavoce.setWidth(3)
    vidavoce.draw(win)
    vidapc = Rectangle(Point(490,80),Point(790,120))
    vidapc.setOutline("black")
    vidapc.setWidth(3)
    vidapc.draw(win)

    pedra=Image(Point(70,500), "imagens/pedra.png")
    pedra.draw(win)
    papel=Image(Point(200,500), "imagens/papel.png")
    papel.draw(win)    
    tesoura=Image(Point(330,500), "imagens/tesoura.png")
    tesoura.draw(win)
    pedrapc=Image(Point(470,500), "imagens/pedrapc.png")
    pedrapc.draw(win)
    papelpc=Image(Point(600,500), "imagens/papelpc.png")
    papelpc.draw(win)    
    tesourapc=Image(Point(730,500), "imagens/tesourapc.png")
    tesourapc.draw(win)

    time.sleep(0.4)

    aviso = Text(Point(400,250), "ASSIM QUE APARECER A MENSAGEM\n' J O G A R '\nESCOLHA PEDRA, PAPEL OU TESOURA")
    aviso.setTextColor("black")
    aviso.setStyle("bold")
    aviso.setSize(24)
    aviso.draw(win)

    time.sleep(5)

    aviso.undraw()
    linha2 = Line(Point(400,50),Point(400,600))
    linha2.setOutline("black")
    linha1.draw(win)
    linha2.draw(win)

    suavida = 0
    vidadele = 0

    vidajogador = 100
    vidacomputador = 100

    loopdojogo = 1
    while loopdojogo == 1:
        numero3 = Text(Point(200,250), "3")
        numero3.setTextColor("black")
        numero3.setStyle("bold")
        numero3.setSize(24)
        numero3.draw(win)
        time.sleep(0.5)
        
        numero3.undraw()
        numero2 = Text(Point(200,250), "2")
        numero2.setTextColor("black")
        numero2.setStyle("bold")
        numero2.setSize(24)
        numero2.draw(win)
        time.sleep(0.5)
        
        numero2.undraw()
        numero1 = Text(Point(200,250), "1")
        numero1.setTextColor("black")
        numero1.setStyle("bold")
        numero1.setSize(24)
        numero1.draw(win)
        time.sleep(0.5)

        
        jokenpo=Image(Point(600,300), "imagens/jokenpo.png")
        jokenpo.draw(win)

        numero1.undraw()
        jogar = Text(Point(200,250), "JOGAR")
        jogar.setTextColor("black")
        jogar.setStyle("bold")
        jogar.setSize(24)
        jogar.draw(win)

        computadorescolheu = 10
        voceescolheu = 10

        loopdarodada = 1
        while loopdarodada == 1:
            loopescolher = 1
            while loopescolher == 1:
                n = win.getMouse()
                x = n.x
                y = n.y
                if x>18 and x<118 and y>445 and y<558:
                    jogar.undraw()
                    jokenpo.undraw()
                    papel.undraw()
                    tesoura.undraw()
                    voceescolheu = 0
                    computadorescolheu = random.randrange(3)
                    loopescolher = 0

                if x>150 and x<248 and y>440 and y<560:
                    jogar.undraw()
                    jokenpo.undraw()
                    pedra.undraw()
                    tesoura.undraw()
                    voceescolheu = 1
                    computadorescolheu = random.randrange(3)
                    loopescolher = 0

                if x>272 and x<381 and y>421 and y<574:
                    jogar.undraw()
                    jokenpo.undraw()
                    pedra.undraw()
                    papel.undraw()
                    voceescolheu = 2
                    computadorescolheu = random.randrange(3)
                    loopescolher = 0
            
            pedrapc.undraw()
            papelpc.undraw()
            tesourapc.undraw()

            if computadorescolheu == 0:
                pedrapc=Image(Point(470,500), "imagens/pedrapc.png")
                pedrapc.draw(win)
            if computadorescolheu == 1:
                papelpc=Image(Point(600,500), "imagens/papelpc.png")
                papelpc.draw(win)   
            if computadorescolheu == 2:
                tesourapc=Image(Point(730,500), "imagens/tesourapc.png")
                tesourapc.draw(win)

            suavida = 0
            vidadele = 0

            time.sleep(1)
            if computadorescolheu == voceescolheu:
                mensagemrodada = Text(Point(200,250), "NÃO VALE\nFOI EMPATE")
                mensagemrodada.setTextColor("black")
                mensagemrodada.setStyle("bold")
                mensagemrodada.setSize(20)
                mensagemrodada.draw(win)
            if computadorescolheu == 0 and voceescolheu == 1:
                mensagemrodada = Text(Point(200,250), "SEU PAPEL\nEMBRULHOU A PEDRA")
                mensagemrodada.setTextColor("black")
                mensagemrodada.setStyle("bold")
                mensagemrodada.setSize(20)
                mensagemrodada.draw(win)
                vidadele = 20
            if computadorescolheu == 1 and voceescolheu == 2:
                mensagemrodada = Text(Point(200,250), "SUA TESOURA\nRASGOU TUDO")
                mensagemrodada.setTextColor("black")
                mensagemrodada.setStyle("bold")
                mensagemrodada.setSize(20)
                mensagemrodada.draw(win)
                tesouravspapel=Image(Point(600,300), "imagens/tesouravspapel.png")
                tesouravspapel.draw(win)
                vidadele = 20
                time.sleep(2)
                tesouravspapel.undraw()
            if computadorescolheu == 2 and voceescolheu == 0:
                mensagemrodada = Text(Point(200,250), "SUA PEDRA\nACABOU COM A TESOURA")
                mensagemrodada.setTextColor("black")
                mensagemrodada.setStyle("bold")
                mensagemrodada.setSize(20)
                mensagemrodada.draw(win)
                vidadele = 20
            if computadorescolheu == 0 and voceescolheu == 2:
                mensagemrodada = Text(Point(200,250), "A PEDRA DELE\nACABOU COM SUA TESOURA")
                mensagemrodada.setTextColor("black")
                mensagemrodada.setStyle("bold")
                mensagemrodada.setSize(20)
                mensagemrodada.draw(win)
                pedravstesoura=Image(Point(600,300), "imagens/pedravstesoura.png")
                pedravstesoura.draw(win)
                suavida = 20
                time.sleep(2)
                pedravstesoura.undraw()
            if computadorescolheu == 1 and voceescolheu == 0:
                mensagemrodada = Text(Point(200,250), "O PAPEL DO INIMIGO\nÉ EMBRULHAR VOCÊ")
                mensagemrodada.setTextColor("black")
                mensagemrodada.setStyle("bold")
                mensagemrodada.setSize(20)
                mensagemrodada.draw(win)
                suavida = 20
            if computadorescolheu == 2 and voceescolheu == 1:
                mensagemrodada = Text(Point(200,250), "SEU PAPEL\nFOI TESOURADO")
                mensagemrodada.setTextColor("black")
                mensagemrodada.setStyle("bold")
                mensagemrodada.setSize(20)
                mensagemrodada.draw(win)
                suavida = 20

            if suavida == 20:
                vidajogador = vidajogador - 20
                if vidajogador == 80:
                    vidavoce100.undraw()
                if vidajogador == 60:
                    vidavoce80.undraw()
                if vidajogador == 40:
                    vidavoce60.undraw()
                if vidajogador == 20:
                    vidavoce40.undraw()
                if vidajogador == 0:
                    vidavoce20.undraw()
            
            if vidadele == 20:
                vidacomputador = vidacomputador - 20
                if vidacomputador == 80:
                    vidapc100.undraw()
                if vidacomputador == 60:
                    vidapc80.undraw()
                if vidacomputador == 40:
                    vidapc60.undraw()
                if vidacomputador == 20:
                    vidapc40.undraw()
                if vidacomputador == 0:
                    vidapc20.undraw()
            
            time.sleep(4)

            pedra.undraw()
            papel.undraw()
            tesoura.undraw()
            pedrapc.undraw()
            papelpc.undraw()
            tesourapc.undraw()
            mensagemrodada.undraw()

            time.sleep(0.5)

            pedra=Image(Point(70,500), "imagens/pedra.png")
            pedra.draw(win)
            papel=Image(Point(200,500), "imagens/papel.png")
            papel.draw(win)    
            tesoura=Image(Point(330,500), "imagens/tesoura.png")
            tesoura.draw(win)
            pedrapc=Image(Point(470,500), "imagens/pedrapc.png")
            pedrapc.draw(win)
            papelpc=Image(Point(600,500), "imagens/papelpc.png")
            papelpc.draw(win)    
            tesourapc=Image(Point(730,500), "imagens/tesourapc.png")
            tesourapc.draw(win)


            fimdejogo = 0
            if vidajogador == 0:
                caixafimdejogo = Rectangle(Point(100,100),Point(700,500))
                caixafimdejogo.setFill("black")
                caixafimdejogo.setOutline("black")
                caixafimdejogo.setWidth(3)
                caixafimdejogo.draw(win)
                caixaverde = Rectangle(Point(200,400),Point(350,450))
                caixaverde.setFill("green")
                caixaverde.setOutline("white")
                caixaverde.setWidth(3)
                caixaverde.draw(win)
                caixavermelha = Rectangle(Point(450,400),Point(600,450))
                caixavermelha.setFill("red")
                caixavermelha.setOutline("white")
                caixavermelha.setWidth(3)
                caixavermelha.draw(win)
                txtfimdejogo = Text(Point(400,250), "QUE PENA, VOCÊ PERDEU!\n\nDESEJA JOGAR NOVAMENTE?")
                txtfimdejogo.setTextColor("white")
                txtfimdejogo.setSize(24)
                txtfimdejogo.draw(win)
                txtverde = Text(Point(275,425), "CONTINUAR")
                txtverde.setTextColor("white")
                txtverde.setSize(20)
                txtverde.draw(win)
                txtvermelho = Text(Point(525,425), "SAIR")
                txtvermelho.setTextColor("white")
                txtvermelho.setSize(20)
                txtvermelho.draw(win)
                while fimdejogo == 0:
                    n = win.getMouse()
                    x = n.x
                    y = n.y
                    if x>200 and x<350 and y>400 and y<450:
                        win.close()
                        abertura()
                    if x>450 and x<600 and y>400 and y<450:
                        win.close()                                    
                    
            if vidacomputador == 0:
                caixafimdejogo = Rectangle(Point(100,100),Point(700,500))
                caixafimdejogo.setFill("black")
                caixafimdejogo.setOutline("black")
                caixafimdejogo.setWidth(3)
                caixafimdejogo.draw(win)
                caixaverde = Rectangle(Point(200,400),Point(350,450))
                caixaverde.setFill("green")
                caixaverde.setOutline("white")
                caixaverde.setWidth(3)
                caixaverde.draw(win)
                caixavermelha = Rectangle(Point(450,400),Point(600,450))
                caixavermelha.setFill("red")
                caixavermelha.setOutline("white")
                caixavermelha.setWidth(3)
                caixavermelha.draw(win)
                txtfimdejogo = Text(Point(400,250), "EBAAAA, VOCÊ VENCEU!\n\nDESEJA JOGAR NOVAMENTE?")
                txtfimdejogo.setTextColor("white")
                txtfimdejogo.setSize(24)
                txtfimdejogo.draw(win)
                txtverde = Text(Point(275,425), "CONTINUAR")
                txtverde.setTextColor("white")
                txtverde.setSize(20)
                txtverde.draw(win)
                txtvermelho = Text(Point(525,425), "SAIR")
                txtvermelho.setTextColor("white")
                txtvermelho.setSize(20)
                txtvermelho.draw(win)
                while fimdejogo == 0:
                    n = win.getMouse()
                    x = n.x
                    y = n.y
                    if x>200 and x<350 and y>400 and y<450:
                        win.close()
                        abertura()
                    if x>450 and x<600 and y>400 and y<450:
                        win.close()  
            loopdarodada = 0
                    
            
    win.getMouse()
    win.getMouse()



abertura()
