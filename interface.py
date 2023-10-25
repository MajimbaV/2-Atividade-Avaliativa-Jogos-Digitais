import pygame as py
from pygame.locals import *
from botao import Botao
from sys import exit


py.init()

# Criando o display:

tela = py.display.set_mode((600,500))
py.display.set_caption('Menu inicial')


#Imagens dos botões em um dict:


dict_imagens_botoes  = {
    "imagens": ("assets/botao_Archer.png",
                "assets/botao_Mago.png",
                "assets/botao_Warrior.png",
                "assets/botao_Start.png", 
                "assets/botao_Back.png",
                "assets/botao_Exit.png",
                "assets/botao_Info.png"
), 
    
    "imagens_select": 
        (   "assets/botao_Archer_select.png",
            "assets/botao_Mago_select.png",
            "assets/botao_Warrior_select.png",
            "assets/botao_Start_select.png",
            "assets/botao_Exit_select.png",
            "assets/botao_Start_select.png",
            "assets/botao_Back_select.png"
)
}

#Criação dos objetos:

botao_start = Botao('Start','Inicia o jogo.', 
dict_imagens_botoes["imagens"][3],
dict_imagens_botoes["imagens_select"][5])

botao_exit = Botao("Exit","fecha o jogo", 
dict_imagens_botoes["imagens"][5], dict_imagens_botoes["imagens_select"][4])

botao_voltar = Botao("Voltar", "Volta para o menu inicial", 
dict_imagens_botoes["imagens"][4], dict_imagens_botoes["imagens_select"][6])

botao_guerreiro = Botao("Mago","Botão para usar a classe Guerreiro.", 
dict_imagens_botoes["imagens"][2], dict_imagens_botoes["imagens_select"][2])

botao_mago = Botao("Mago","Botão para usar a classe Mago.",
dict_imagens_botoes["imagens"][1],dict_imagens_botoes["imagens_select"][1])

botao_arqueiro = Botao("Arqueiro","Botão para usar a classe Arqueiro.",
dict_imagens_botoes["imagens"][0],dict_imagens_botoes["imagens_select"][0])

botao_info = Botao("Informação", "Resumo do jogo", dict_imagens_botoes["imagens"][6])

#Criando a imagem de fundo:


imagem_fundo = "assets/dirt.jpg"
fundo = py.transform.scale(py.image.load(imagem_fundo),(600,500))
imagem_info = "assets/story_game.png.png"
fundo_info = py.transform.scale(py.image.load(imagem_info).convert(),(600,500))       

#Variáveis de controle:

selecionar_arqueiro = False
selecionar_mago = False
selecionar_guerreiro = False
selecionar_voltar = False
selecionar_exit = False
selecionar_start = False
cond = 1


#posiçôes das superficies:

pos_start = (225,200)
pos_exit = (225,270)
pos_arqueiro = (80,75)
pos_mago = (80,180)
pos_guerreiro = (80,285)
pos_voltar = (80,390)
pos_info = (550,10)

#superfícies:
escala = (150,20)
escala_select = (212,40)
escala_info = (40,40)
surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
surface_mago = botao_mago.auto_carregar_imagem(escala)
surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
surface_voltar = botao_voltar.auto_carregar_imagem(escala)
surface_start = botao_start.auto_carregar_imagem(escala)
surface_exit = botao_exit.auto_carregar_imagem(escala)
surface_info = botao_info.auto_carregar_imagem(escala_info)



#Run principal:

while True:
    for evento in py.event.get():
        if evento.type == QUIT:
            py.quit()
            exit()
        elif evento.type == MOUSEBUTTONDOWN:
            pos_X,pos_Y = py.mouse.get_pos()
            if cond == 1:
                if selecionar_start:
                    if 195 <= pos_X <= 410 and 200 <= pos_Y <= 240:
                        cond = 3
                        selecionar_exit = False
                        selecionar_start = False
                        surface_start = botao_start.auto_carregar_imagem(escala)
                        surface_exit = botao_exit.auto_carregar_imagem(escala)
                        pos_start = (225,200)
                        pos_exit = (225,270)
                        
                    elif 225 <= pos_X <= 375 and 270 <= pos_Y <= 290:
                        py.quit()
                        exit()
                    
                    elif 50 <= pos_X <= 590 and 10 <= pos_Y <= 55:
                        cond = 2
                        selecionar_exit = False
                        selecionar_start = False
                        surface_start = botao_start.auto_carregar_imagem(escala)
                        surface_exit = botao_exit.auto_carregar_imagem(escala)
                        pos_start = (225,200)
                        pos_exit = (225,270)

                    else:
                        ...
                elif selecionar_exit:
                        if 195 <= pos_X <= 410 and 270 <= pos_Y <= 310:
                            py.quit()
                            exit()
                        elif 225 <= pos_X <= 375 and 200 <= pos_Y <= 220:
                            cond = 3
                            selecionar_exit = False
                            selecionar_start = False
                            surface_start = botao_start.auto_carregar_imagem(escala)
                            surface_exit = botao_exit.auto_carregar_imagem(escala)
                            pos_start = (225,200)
                            pos_exit = (225,270)    
                        elif 550 <= pos_X <= 590 and 10 <= pos_Y <= 50:
                            cond = 2
                            selecionar_exit = False
                            selecionar_start = False
                            surface_start = botao_start.auto_carregar_imagem(escala)
                            surface_exit = botao_exit.auto_carregar_imagem(escala)
                            pos_start = (225,200)
                            pos_exit = (225,270)                    
                        else:
                            ...        
                       
                else:
                    if 225 <= pos_X <= 375 and 200 <= pos_Y <= 220:
                        cond = 3
                        selecionar_exit = False
                        selecionar_start = False
                        surface_start = botao_start.auto_carregar_imagem(escala)
                        surface_exit = botao_exit.auto_carregar_imagem(escala)
                        pos_start = (225,200)
                        pos_exit = (225,270)                    
                    elif 225 <= pos_X <= 375 and 270 <= pos_Y <= 290:
                        py.quit()
                        exit()
        
                    elif 550 <= pos_X <= 590 and 10 <= pos_Y <= 55:
                        cond = 2
                    else:
                        ...
            
            elif cond == 2:
                    if  550 <= pos_X <= 590 and 10 <= pos_Y <= 50:
                        cond = 1
                    else:
                        ...             
            
            
            
            else:
                if selecionar_arqueiro:
                    if 50 <= pos_X <= 262 and  75 <= pos_Y <= 115:
                        print('Arqueiro ainda em cosntrução.')
                    elif 80 <= pos_X <= 230 and  180 <= pos_Y <= 200:
                        print('Mago ainda em construção')
                    elif 80 <= pos_X <= 230 and  285 <= pos_Y <= 305:
                        print('Guerreiro ainda em construção.')
                    elif 80 <= pos_X <= 230 and  390 <= pos_Y <= 410:
                        cond = 1
                        selecionar_arqueiro = False
                        selecionar_mago = False
                        selecionar_guerreiro = False
                        selecionar_voltar = False
                        surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
                        surface_mago = botao_mago.auto_carregar_imagem(escala)
                        surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
                        surface_voltar = botao_voltar.auto_carregar_imagem(escala)
                        pos_arqueiro = (80,75)
                        pos_mago = (80,180)
                        pos_guerreiro = (80,285)
                        pos_voltar = (80,390)
                    else:
                        ...
                elif selecionar_mago:
                    if 50 <= pos_X <= 262 and  180 <= pos_Y <= 220:
                        print('Mago ainda em construção.')
                    elif 80 <= pos_X <= 230 and  285 <= pos_Y <= 305:
                        print('Guerreiro ainda em construção')
                    elif 80 <= pos_X <= 230 and  390 <= pos_Y <= 410:
                        cond = 1
                        selecionar_arqueiro = False
                        selecionar_mago = False
                        selecionar_guerreiro = False
                        selecionar_voltar = False
                        surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
                        surface_mago = botao_mago.auto_carregar_imagem(escala)
                        surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
                        surface_voltar = botao_voltar.auto_carregar_imagem(escala)
                        pos_arqueiro = (80,75)
                        pos_mago = (80,180)
                        pos_guerreiro = (80,285)
                        pos_voltar = (80,390)
                    elif 80 <= pos_X <= 230 and  75 <= pos_Y <= 95:
                        print('Arqueiro ainda em construção.')
                    else:
                        ...
                elif selecionar_guerreiro:
                    if  50 <= pos_X <= 262 and  285 <= pos_Y <= 305:
                        print('Guerreiro ainda em construção.')
                    elif 80 <= pos_X <= 230 and  75 <= pos_Y <= 95:
                        print('Arqueiro ainda em construção.')
                    elif 80 <= pos_X <= 230 and  180 <= pos_Y <= 200:
                        print('Mago ainda em construção.')
                    elif 80 <= pos_X <= 230 and  390 <= pos_Y <= 410:
                        cond = 1
                        selecionar_arqueiro = False
                        selecionar_mago = False
                        selecionar_guerreiro = False
                        selecionar_voltar = False
                        surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
                        surface_mago = botao_mago.auto_carregar_imagem(escala)
                        surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
                        surface_voltar = botao_voltar.auto_carregar_imagem(escala)
                        pos_arqueiro = (80,75)
                        pos_mago = (80,180)
                        pos_guerreiro = (80,285)
                        pos_voltar = (80,390)
                    else:
                        ...
                elif selecionar_voltar:
                    if 50 <= pos_X <= 262 and  390 <= pos_Y <= 430:
                        cond = 1
                        selecionar_arqueiro = False
                        selecionar_mago = False
                        selecionar_guerreiro = False
                        selecionar_voltar = False
                        surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
                        surface_mago = botao_mago.auto_carregar_imagem(escala)
                        surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
                        surface_voltar = botao_voltar.auto_carregar_imagem(escala)
                        pos_arqueiro = (80,75)
                        pos_mago = (80,180)
                        pos_guerreiro = (80,285)
                        pos_voltar = (80,390)
                    elif 80 <= pos_X <= 230 and  75 <= pos_Y <= 95:
                        print('Arqueiro ainda em construção.')
                    elif 80 <= pos_X <= 230 and  180 <= pos_Y <= 200:
                        print('Mago ainda em construção.')
                    elif 80 <= pos_X <= 230 and  285 <= pos_Y <= 305:
                        print('Guerreiro ainda em construção.')
                    else:
                        ...
                else:
                    if 80 <= pos_X <= 230 and  75 <= pos_Y <= 95:
                        print('Arqueiro ainda em construção.')
                    elif 80 <= pos_X <= 230 and  180 <= pos_Y <= 200:
                        print('Mago ainda em construção.')
                    elif 80 <= pos_X <= 230 and  285 <= pos_Y <= 305:
                        print('Guerreiro ainda em construção.')
                    elif 80 <= pos_X <= 230 and  390 <= pos_Y <= 410:
                        cond = 1
                        selecionar_arqueiro = False
                        selecionar_mago = False
                        selecionar_guerreiro = False
                        selecionar_voltar = False
                        surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
                        surface_mago = botao_mago.auto_carregar_imagem(escala)
                        surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
                        surface_voltar = botao_voltar.auto_carregar_imagem(escala)
                        pos_arqueiro = (80,75)
                        pos_mago = (80,180)
                        pos_guerreiro = (80,285)
                        pos_voltar = (80,390)
                    else:
                        ...

        elif evento.type == KEYDOWN:
            
            if cond == 3:    
                if evento.key == K_UP:
                    if selecionar_arqueiro:
                        selecionar_arqueiro = False
                        selecionar_voltar = True
                        surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
                        surface_voltar = botao_voltar.auto_selecionar(escala_select)
                        pos_arqueiro = (80,75)
                        pos_voltar = (50,390)
                    elif selecionar_mago:
                        selecionar_mago = False
                        selecionar_arqueiro = True
                        surface_mago = botao_mago.auto_carregar_imagem(escala)
                        surface_arqueiro = botao_arqueiro.auto_selecionar(escala_select)
                        pos_mago = (80,180)
                        pos_arqueiro = (50,75)
                    elif selecionar_guerreiro:
                        selecionar_guerreiro = False
                        selecionar_mago = True
                        surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
                        surface_mago = botao_mago.auto_selecionar(escala_select)
                        pos_guerreiro = (80,285)
                        pos_mago = (50,180)
                    elif selecionar_voltar:
                        selecionar_voltar = False
                        selecionar_guerreiro = True
                        surface_voltar = botao_voltar.auto_carregar_imagem(escala)
                        surface_guerreiro = botao_guerreiro.auto_selecionar(escala_select)
                        pos_voltar = (80,390)
                        pos_guerreiro = (50,290)
                    else:
                        selecionar_voltar = True
                        surface_voltar = botao_voltar.auto_selecionar(escala_select)
                        pos_voltar = (50,390)
                         
                elif evento.key == K_DOWN:  
                    if selecionar_arqueiro:
                        selecionar_arqueiro = False
                        selecionar_mago = True
                        surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
                        surface_mago = botao_mago.auto_selecionar(escala_select)
                        pos_arqueiro = (80,75)
                        pos_mago = (50,180)
                    elif selecionar_mago:
                        selecionar_mago = False
                        selecionar_guerreiro = True
                        surface_mago = botao_mago.auto_carregar_imagem(escala)
                        surface_guerreiro = botao_guerreiro.auto_selecionar(escala_select)
                        pos_mago = (80,180)
                        pos_guerreiro = (50,295)
                    elif selecionar_guerreiro:
                        selecionar_guerreiro = False
                        selecionar_voltar = True
                        surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
                        surface_voltar = botao_voltar.auto_selecionar(escala_select)
                        pos_guerreiro = (80,285)
                        pos_voltar = (50,390)
                    elif selecionar_voltar:
                        selecionar_voltar = False
                        selecionar_arqueiro = True
                        surface_voltar = botao_voltar.auto_carregar_imagem(escala)
                        surface_arqueiro = botao_arqueiro.auto_selecionar(escala_select)
                        pos_voltar = (80,390)
                        pos_arqueiro = (50,75)
                    else:
                        selecionar_arqueiro = True
                        surface_arqueiro = botao_arqueiro.auto_selecionar(escala_select)
                        pos_arqueiro = (50,75)
                    
                elif evento.key == 13:
                    if selecionar_arqueiro:
                        print('Arqueiro ainda em construção...') 
                    elif selecionar_mago:
                        print('Mago ainda em construção...')
                    elif selecionar_guerreiro:
                        print('Guerreiro ainda em construção...')
                    elif selecionar_voltar:
                        cond = 1
                        selecionar_arqueiro = False
                        selecionar_mago = False
                        selecionar_guerreiro = False
                        selecionar_voltar = False
                        surface_arqueiro = botao_arqueiro.auto_carregar_imagem(escala)
                        surface_mago = botao_mago.auto_carregar_imagem(escala)
                        surface_guerreiro = botao_guerreiro.auto_carregar_imagem(escala)
                        surface_voltar = botao_voltar.auto_carregar_imagem(escala)
                        pos_arqueiro = (80,75)
                        pos_mago = (80,180)
                        pos_guerreiro = (80,285)
                        pos_voltar = (80,390) 
                    else:
                        ...
                else:
                    ...
                    
                        
            elif cond == 1:
                if evento.key == K_UP or evento.key == K_DOWN:
                    if selecionar_start:
                        selecionar_start = False
                        selecionar_exit = True
                        surface_start = botao_start.auto_carregar_imagem(escala) 
                        surface_exit = botao_exit.auto_selecionar(escala_select)
                        pos_start = (225,200)
                        pos_exit = (195,270)
                    elif selecionar_exit:
                        selecionar_exit = False
                        selecionar_start = True
                        surface_exit = botao_exit.auto_carregar_imagem(escala) 
                        surface_start = botao_start.auto_selecionar(escala_select)
                        pos_exit = (225,270)
                        pos_start = (195,200)
                    elif not selecionar_exit and not selecionar_start:
                            if evento.key == K_UP:
                                selecionar_exit = True 
                                surface_exit = botao_exit.auto_selecionar(escala_select)
                                pos_exit = (195,270)
                            else:
                                selecionar_start = True 
                                surface_start = botao_start.auto_selecionar(escala_select)
                                pos_start = (195,200)
                    else:
                        ...
                elif evento.key == 13:
                                                      
                    if selecionar_start:
                        cond = 3
                        selecionar_exit = False
                        selecionar_start = False
                        surface_start = botao_start.auto_carregar_imagem(escala)
                        surface_exit = botao_exit.auto_carregar_imagem(escala)
                        pos_start = (225,200)
                        pos_exit = (225,270)
                    elif selecionar_exit:
                        py.quit()
                        exit()     
                    else:
                        ...
                else:
                    ...
            else:
                ...
        else:
            ...
    if cond ==  1:
        
        
            tela.blit(fundo, (0,0))
            tela.blit(surface_start,pos_start)
            tela.blit(surface_exit, pos_exit)
            tela.blit(surface_info,pos_info)
    
    elif cond == 2:
        
        tela.blit(fundo_info,(0,0))
        tela.blit(surface_info,pos_info)
    
    
    else:
        
        tela.blit(fundo,(0,0))
        tela.blit(surface_arqueiro,pos_arqueiro)
        tela.blit(surface_mago,pos_mago)
        tela.blit(surface_guerreiro,pos_guerreiro)
        tela.blit(surface_voltar,pos_voltar)

        

    py.display.update()
    