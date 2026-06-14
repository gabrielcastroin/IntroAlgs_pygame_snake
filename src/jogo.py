import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    PRETO,
    VERDE,
    VERMELHO,
    TAMANHO_CELULA,
    CAMINHO_RECORDE,
)

from src.funcoes import (
    calcular_pontos,
    mover_cobra,
    cobra_perde_segmento,
    cobra_colidiu_com_borda,
    cobra_colidiu_consigo_mesma,
    cobra_comeu_comida,
    gerar_comida_aleatoria,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def executar_jogo():
    """Executa o loop principal do Jogo da Cobra."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True
    game_over = False

    # Inicializa a cobra no meio da tela (coordenadas em células)
    largura_celulas = LARGURA_TELA // TAMANHO_CELULA
    altura_celulas = ALTURA_TELA // TAMANHO_CELULA

    cobra = [
        {"x": largura_celulas // 2, "y": altura_celulas // 2},
        {"x": largura_celulas // 2 - 1, "y": altura_celulas // 2},
        {"x": largura_celulas // 2 - 2, "y": altura_celulas // 2},
    ]

    # Direção inicial (para a direita)
    direcao = "RIGHT"
    proxima_direcao = "RIGHT"

    # Comida
    comida = gerar_comida_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA, cobra)

    # Pontuação
    pontos = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal do jogo
    while rodando:
        relogio.tick(FPS)

        # Captura eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                # Trata entrada do teclado para mudar direção
                # Evita que a cobra vire 180 graus para si mesma
                if evento.key == pygame.K_UP and direcao != "DOWN":
                    proxima_direcao = "UP"
                elif evento.key == pygame.K_DOWN and direcao != "UP":
                    proxima_direcao = "DOWN"
                elif evento.key == pygame.K_LEFT and direcao != "RIGHT":
                    proxima_direcao = "LEFT"
                elif evento.key == pygame.K_RIGHT and direcao != "LEFT":
                    proxima_direcao = "RIGHT"

        # Atualiza a direção se não tiver sido cancelada
        direcao = proxima_direcao

        # Move a cobra
        if not game_over:
            mover_cobra(cobra, direcao)

            # Verifica colisão com a comida
            if cobra_comeu_comida(cobra, comida):
                pontos = calcular_pontos(pontos, 10)
                comida = gerar_comida_aleatoria(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA, cobra)
            else:
                # Se não comeu, perde um segmento (movimento normal)
                cobra_perde_segmento(cobra)

            # Verifica fim de jogo
            if cobra_colidiu_com_borda(cobra, LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA):
                game_over = True
            elif cobra_colidiu_consigo_mesma(cobra):
                game_over = True

        # Atualiza recorde se necessário
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        # Atualiza o título da janela
        status = "GAME OVER" if game_over else "JOGANDO"
        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | {status}"
        )

        # Desenha a cena
        tela.fill(PRETO)

        # Desenha a cobra (verde)
        for segmento in cobra:
            x_pixel = segmento["x"] * TAMANHO_CELULA
            y_pixel = segmento["y"] * TAMANHO_CELULA
            pygame.draw.rect(
                tela,
                VERDE,
                (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA)
            )
            # Desenha borda para melhor visualização
            pygame.draw.rect(
                tela,
                (0, 100, 0),
                (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA),
                1
            )

        # Desenha a comida (vermelho)
        x_pixel = comida["x"] * TAMANHO_CELULA
        y_pixel = comida["y"] * TAMANHO_CELULA
        pygame.draw.rect(
            tela,
            VERMELHO,
            (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA)
        )
        pygame.draw.rect(
            tela,
            (200, 0, 0),
            (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA),
            1
        )

        # Se game over, exibe mensagem
        if game_over:
            fonte = pygame.font.Font(None, 36)
            texto = fonte.render("GAME OVER! Pressione ESC para sair", True, VERMELHO)
            rect_texto = texto.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
            tela.blit(texto, rect_texto)

            # Permite sair com ESC
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_ESCAPE]:
                rodando = False

        pygame.display.flip()

    pygame.quit()