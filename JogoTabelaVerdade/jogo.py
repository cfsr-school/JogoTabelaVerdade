import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_tabela_verdade(proposicao, resultado_esperado):
    if proposicao == "p ou r":
        variaveis = ["p", "r"]  # Usar 'p' e 'r' para a proposição que envolve 'p ou r'
        combinacoes = [(0, 1), (0, 1), (1, 0), (1, 1)]
    elif proposicao == "p e não x":
        variaveis = ["p", "x"]  # Usar 'p' e 'x' para a proposição que envolve 'p e não x'
        combinacoes = [(0, 1), (0, 1), (1, 1), (1, 1)]
    else:
        variaveis = ["p", "q"]
        combinacoes = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    print("Tabela Verdade:")
    print(" ".join(variaveis) + " | " + proposicao)
    
    for combinacao in combinacoes:
        print(" ".join(map(str, combinacao)) + " | ?")

    return combinacoes, resultado_esperado

def mostrar_tabela_completa(proposicao, combinacoes, resultado_esperado):
    if proposicao == "p ou r":
        variaveis = ["p", "r"]
    elif proposicao == "p e não x":
        variaveis = ["p", "x"]
    else:
        variaveis = ["p", "q"]
    
    print("Tabela Verdade Completa:")
    print(" ".join(variaveis) + " | " + proposicao)
    for i, combinacao in enumerate(combinacoes):
        print(" ".join(map(str, combinacao)) + " | " + str(resultado_esperado[i]))

def selecionar_proposicoes():
    return [
        ("p e q", [0, 0, 0, 1], 3),               # Contingência: p e q
        ("p ou r", [1, 1, 1, 1], 1),              # Tautologia: p ou r
        ("p ou não q", [1, 0, 1, 1], 3),          # Contingência: p ou não q
        ("p e não x", [0, 0, 0, 0], 2)            # Contradição: p e não x
    ]

def obter_entrada_valida(prompt, opcoes_validas):
    while True:
        entrada = input(prompt)
        if entrada.isdigit() and int(entrada) in opcoes_validas:
            return int(entrada)
        print("Entrada incorreta. Digite um valor válido.")

def rodada_jogador(jogador, proposicoes):
    pontuacao = 0
    for proposicao, resultado_esperado, classificacao_esperada in proposicoes:
        limpar_tela()
        print(f"\nJogador {jogador}, sua vez!")
        print(f"Proposição: {proposicao}")
        combinacoes, resultado_esperado = gerar_tabela_verdade(proposicao, resultado_esperado)
        
        # Coleta as respostas do jogador para a tabela
        respostas = []
        print("\nComplete a tabela (use 1 para verdadeiro e 0 para falso):")
        for combinacao in combinacoes:
            resposta = obter_entrada_valida(f"Para a combinação {combinacao}, insira o resultado: ", {0, 1})
            respostas.append(resposta)
        
        # Verificar acerto na tabela
        if respostas == resultado_esperado:
            pontuacao += 1
            print("Tabela correta! + 1 ponto.")
        else:
            print("Tabela incorreta.")
        
        time.sleep(2)
        limpar_tela()
        
        # Mostrar tabela completa e perguntar sobre a classificação
        mostrar_tabela_completa(proposicao, combinacoes, resultado_esperado)
        print("\nClassifique a proposição:")
        print("1 - Tautologia")
        print("2 - Contradição")
        print("3 - Contingência")
        tipo = obter_entrada_valida("Escolha o número: ", {1, 2, 3})
        
        # Verificar acerto na classificação
        if tipo == classificacao_esperada:
            pontuacao += 1
            print("Classificação correta! + 1 ponto")
        else:
            print("Classificação errada.")
        
        time.sleep(2)
        limpar_tela()
    
    return pontuacao

def jogar():
    limpar_tela()
    modo_jogo = obter_entrada_valida("Escolha o modo de jogo:\n1 - Um jogador\n2 - Dois jogadores\nDigite o número: ", {1, 2})
    
    proposicoes = selecionar_proposicoes()
    
    # Jogador 1 responde todas as proposições
    pontuacao_jogador1 = rodada_jogador(1, proposicoes)
    
    # Jogador 2 responde todas as proposições se o modo for para dois jogadores
    pontuacao_jogador2 = 0
    if modo_jogo == 2:
        pontuacao_jogador2 = rodada_jogador(2, proposicoes)
    
    # Mostrar pontuação final
    print("Resultado Final:")
    print(f"Pontuação Jogador 1: {pontuacao_jogador1} pontos")
    if modo_jogo == 2:
        print(f"Pontuação Jogador 2: {pontuacao_jogador2} pontos")
        if pontuacao_jogador1 > pontuacao_jogador2:
            print("Jogador 1 wins!")
            print("Fim do jogo")
        elif pontuacao_jogador2 > pontuacao_jogador1:
            print("Jogador 2 wins!")
            print("Fim do jogo")
        else:
            print("Empate!")
            print("Fim do jogo")
    else:
        print("Fim do jogo")

jogar()
