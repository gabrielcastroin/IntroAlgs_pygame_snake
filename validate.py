#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Validação - Verifica se tudo está funcionando
Execute: python validate.py
"""

import sys
import subprocess
import os


def print_header(titulo):
    """Imprime cabeçalho formatado."""
    print("\n" + "="*60)
    print(f"  {titulo}")
    print("="*60)


def print_success(mensagem):
    """Imprime mensagem de sucesso."""
    print(f"✅ {mensagem}")


def print_error(mensagem):
    """Imprime mensagem de erro."""
    print(f"❌ {mensagem}")


def print_warning(mensagem):
    """Imprime mensagem de aviso."""
    print(f"⚠️  {mensagem}")


def print_info(mensagem):
    """Imprime mensagem de informação."""
    print(f"ℹ️  {mensagem}")


def validar_python():
    """Valida versão do Python."""
    print_header("1. Validando Python")
    
    version = sys.version_info
    print_info(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print_success("Versão Python compatível")
        return True
    else:
        print_error("Python 3.8+ é necessário")
        return False


def validar_modulos():
    """Valida importação de módulos."""
    print_header("2. Validando Módulos")
    
    modulos = [
        ("pygame", "Pygame"),
        ("pytest", "Pytest"),
    ]
    
    todos_ok = True
    for modulo, nome in modulos:
        try:
            __import__(modulo)
            print_success(f"{nome} importado com sucesso")
        except ImportError:
            print_error(f"{nome} não encontrado. Execute: pip install {modulo}")
            todos_ok = False
    
    return todos_ok


def validar_arquivos():
    """Valida existência de arquivos criados."""
    print_header("3. Validando Arquivos Criados")
    
    arquivos_novos = [
        "src/cobra.py",
        "src/utils.py",
        "src/pontuacao.py",
        "src/menu.py",
    ]
    
    todos_ok = True
    for arquivo in arquivos_novos:
        if os.path.exists(arquivo):
            size = os.path.getsize(arquivo)
            print_success(f"{arquivo} ({size} bytes)")
        else:
            print_error(f"{arquivo} não encontrado")
            todos_ok = False
    
    return todos_ok


def validar_testes():
    """Executa testes unitários."""
    print_header("4. Executando Testes")
    
    try:
        resultado = subprocess.run(
            ["python", "-m", "pytest", "tests/test_logica.py", "-v", "--tb=short"],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Conta quantos testes passaram
        linhas = resultado.stdout.split('\n')
        for linha in linhas:
            if "passed" in linha:
                print_success(linha.strip())
                return True
        
        if resultado.returncode != 0:
            print_error("Testes falharam!")
            print(resultado.stdout[-500:])  # Últimas linhas
            return False
        
        return True
    
    except subprocess.TimeoutExpired:
        print_error("Testes demoraram muito (timeout)")
        return False
    except Exception as e:
        print_error(f"Erro ao executar testes: {e}")
        return False


def validar_sintatico():
    """Valida erros de sintaxe."""
    print_header("5. Validando Sintaxe")
    
    arquivos_py = [
        "main.py",
        "run_game.py",
        "src/config.py",
        "src/cobra.py",
        "src/utils.py",
        "src/pontuacao.py",
        "src/menu.py",
        "src/jogo.py",
    ]
    
    todos_ok = True
    for arquivo in arquivos_py:
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                compile(f.read(), arquivo, 'exec')
            print_success(f"{arquivo} - Sintaxe OK")
        except SyntaxError as e:
            print_error(f"{arquivo} - Erro de sintaxe: {e}")
            todos_ok = False
        except FileNotFoundError:
            print_warning(f"{arquivo} - Não encontrado")
    
    return todos_ok


def validar_estrutura():
    """Valida estrutura de diretórios."""
    print_header("6. Validando Estrutura")
    
    diretorios = ["src", "tests", "data", "assets"]
    
    todos_ok = True
    for diretorio in diretorios:
        if os.path.isdir(diretorio):
            print_success(f"Diretório '{diretorio}/' existe")
        else:
            print_warning(f"Diretório '{diretorio}/' não encontrado")
    
    return todos_ok


def resumo_final(resultados):
    """Imprime resumo final."""
    print_header("RESUMO FINAL")
    
    total = len(resultados)
    sucesso = sum(1 for r in resultados if r)
    
    print_info(f"Verificações passadas: {sucesso}/{total}")
    
    if sucesso == total:
        print_success("Todas as validações passaram!")
        print_success("O jogo está pronto para jogar!")
        print_info("\nPara jogar, execute:")
        print_info("  python main.py")
        print()
        return True
    else:
        print_error("Algumas validações falharam.")
        print_warning("Corrija os problemas acima antes de jogar.")
        print()
        return False


def main():
    """Função principal."""
    print("\n" + "🐍 " * 20)
    print("VALIDAÇÃO DO JOGO DA COBRA".center(60))
    print("🐍 " * 20)
    
    resultados = [
        validar_python(),
        validar_modulos(),
        validar_arquivos(),
        validar_sintatico(),
        validar_estrutura(),
        validar_testes(),
    ]
    
    sucesso = resumo_final(resultados)
    
    return 0 if sucesso else 1


if __name__ == "__main__":
    sys.exit(main())
