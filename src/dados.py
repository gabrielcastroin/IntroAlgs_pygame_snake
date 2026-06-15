def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0


# ===== SISTEMA DE RANKING =====

def salvar_ranking(caminho_arquivo, jogador_nome, pontos, tempo_jogo):
    """
    Salva uma entrada de ranking em JSON.
    Mantém um ranking top 10.
    
    Args:
        caminho_arquivo: Caminho do arquivo de ranking
        jogador_nome: Nome do jogador
        pontos: Pontuação alcançada
        tempo_jogo: Tempo de jogo em segundos
    """
    import json
    from datetime import datetime
    
    ranking = carregar_ranking(caminho_arquivo)
    
    # Cria nova entrada
    nova_entrada = {
        "nome": jogador_nome[:20],  # Limita nome a 20 caracteres
        "pontos": pontos,
        "tempo": tempo_jogo,
        "data": datetime.now().isoformat()
    }
    
    # Adiciona e ordena
    ranking.append(nova_entrada)
    ranking.sort(key=lambda x: x["pontos"], reverse=True)
    
    # Mantém apenas top 10
    ranking = ranking[:10]
    
    # Salva
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(ranking, arquivo, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar ranking: {e}")


def carregar_ranking(caminho_arquivo):
    """
    Carrega o ranking do arquivo JSON.
    
    Returns:
        Lista de entradas de ranking, ordenadas por pontos (decrescente)
    """
    import json
    
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo == "":
                return []
            return json.loads(conteudo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def formatar_ranking(ranking):
    """
    Formata o ranking para exibição.
    
    Args:
        ranking: Lista de entradas de ranking
        
    Returns:
        String formatada com o ranking
    """
    if not ranking:
        return "Nenhuma entrada no ranking ainda."
    
    linhas = ["=== TOP 10 RANKING ==="]
    for i, entrada in enumerate(ranking, 1):
        nome = entrada.get("nome", "Desconhecido")
        pontos = entrada.get("pontos", 0)
        tempo = entrada.get("tempo", 0)
        data = entrada.get("data", "").split("T")[0]  # Pega apenas a data
        
        linha = f"{i:2d}. {nome:15s} - {pontos:5d} pts ({tempo:3d}s) [{data}]"
        linhas.append(linha)
    
    return "\n".join(linhas)


def obter_melhor_ranking(ranking):
    """
    Obtém a melhor pontuação do ranking.
    
    Args:
        ranking: Lista de entradas de ranking
        
    Returns:
        Melhor pontuação ou 0 se ranking vazio
    """
    if ranking:
        return ranking[0].get("pontos", 0)
    return 0