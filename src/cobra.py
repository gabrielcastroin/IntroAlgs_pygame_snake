# -*- coding: utf-8 -*-
"""
Módulo da Cobra - Comportamento e lógica de movimento
"""


class Cobra:
    """Representa a cobra no jogo."""
    
    def __init__(self, inicio_x, inicio_y):
        """
        Inicializa a cobra.
        
        Args:
            inicio_x: Posição inicial X (em células)
            inicio_y: Posição inicial Y (em células)
        """
        self.corpo = [
            {"x": inicio_x, "y": inicio_y},      # Cabeça
            {"x": inicio_x - 1, "y": inicio_y},  # Corpo
            {"x": inicio_x - 2, "y": inicio_y},  # Cauda
        ]
        self.direcao = "RIGHT"
        self.proxima_direcao = "RIGHT"
    
    def mover(self):
        """Move a cobra na direção atual."""
        self.direcao = self.proxima_direcao
        
        cabeca = self.corpo[0].copy()
        
        if self.direcao == "UP":
            cabeca["y"] -= 1
        elif self.direcao == "DOWN":
            cabeca["y"] += 1
        elif self.direcao == "LEFT":
            cabeca["x"] -= 1
        elif self.direcao == "RIGHT":
            cabeca["x"] += 1
        
        self.corpo.insert(0, cabeca)
    
    def atravessar_borda(self, largura_tela, altura_tela, tamanho_celula):
        """Faz a cobra reaparecer no lado oposto ao bater na borda."""
        cabeca = self.corpo[0]
        max_x = largura_tela // tamanho_celula
        max_y = altura_tela // tamanho_celula
        
        if cabeca["x"] < 0:
            cabeca["x"] = max_x - 1
        elif cabeca["x"] >= max_x:
            cabeca["x"] = 0
            
        if cabeca["y"] < 0:
            cabeca["y"] = max_y - 1
        elif cabeca["y"] >= max_y:
            cabeca["y"] = 0

    def comer(self):
        """A cobra come, não remove cauda (cresce)."""
        pass  # Crescimento é implícito ao não remover a cauda
    
    def remover_cauda(self):
        """Remove o último segmento (movimento normal)."""
        if len(self.corpo) > 1:
            self.corpo.pop()
    
    def definir_direcao(self, direcao):
        """Define a próxima direção, evitando inversão de 180 graus."""
        opostas = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        
        if direcao != opostas[self.direcao]:
            self.proxima_direcao = direcao
    
    def colidiu_com_borda(self, largura_tela, altura_tela, tamanho_celula):
        """Verifica colisão com as bordas."""
        cabeca = self.corpo[0]
        max_x = largura_tela // tamanho_celula
        max_y = altura_tela // tamanho_celula
        
        return (cabeca["x"] < 0 or cabeca["x"] >= max_x or
                cabeca["y"] < 0 or cabeca["y"] >= max_y)
    
    def colidiu_consigo_mesma(self):
        """Verifica auto-colisão (cabeça bate no corpo)."""
        cabeca = self.corpo[0]
        # Verifica se a cabeça colide com qualquer segmento do corpo (exceto a cabeça)
        for segmento in self.corpo[1:]:
            if cabeca["x"] == segmento["x"] and cabeca["y"] == segmento["y"]:
                return True
        return False
    
    def comeu_comida(self, comida):
        """Verifica se comeu a comida."""
        cabeca = self.corpo[0]
        return cabeca["x"] == comida["x"] and cabeca["y"] == comida["y"]
    
    def obter_cabeca(self):
        """Retorna a posição da cabeça."""
        return self.corpo[0].copy()
    
    def obter_tamanho(self):
        """Retorna o tamanho (número de segmentos)."""
        return len(self.corpo)
    
    def reiniciar(self, inicio_x, inicio_y):
        """Reinicia a cobra para posição inicial."""
        self.corpo = [
            {"x": inicio_x, "y": inicio_y},
            {"x": inicio_x - 1, "y": inicio_y},
            {"x": inicio_x - 2, "y": inicio_y},
        ]
        self.direcao = "RIGHT"
        self.proxima_direcao = "RIGHT"
