import pygame as py
class Botao:
    def __init__(self,nome: str,descricao: str,link_imagem: str, link_imagem_selecionada: str = None):
        self.nome_botao = nome
        self.descricao_botao = descricao
        self.link_imagem = link_imagem
        self.link_imagem_selecionada = link_imagem_selecionada
        
    def auto_carregar_imagem(self,escala: tuple):
        carregar = py.image.load(self.link_imagem)
        return py.transform.scale(carregar,escala)
        
    def auto_selecionar(self,escala: tuple):
        carregar = py.image.load(self.link_imagem_selecionada)
        return py.transform.scale(carregar,escala)
    