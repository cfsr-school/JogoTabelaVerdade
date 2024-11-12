# Jogo de Tabelas Verdade de Lógica Proposicional

![Linguagem: Python](https://img.shields.io/badge/Linguagem-Python-blue.svg)

Este é um jogo educativo desenvolvido em **Python** que testa e aprimora seus conhecimentos em lógica proposicional, especificamente na construção e classificação de tabelas verdade.

## Sumário

- [Descrição do Jogo](#descrição-do-jogo)
- [Como Jogar](#como-jogar)
- [Objetivo Educacional](#objetivo-educacional)
- [Requisitos](#requisitos)
- [Como Executar](#como-executar)
- [Contribuições](#contribuições)
- [Licença](#licença)
- [Capturas de Tela](#capturas-de-tela)
- [Contato](#contato)

## Descrição do Jogo

O jogo permite a participação de **um ou dois jogadores**. Em cada rodada, os jogadores são apresentados a diferentes proposições lógicas e devem:

1. **Completar a Tabela Verdade**: Fornecer os valores lógicos (`0` para falso e `1` para verdadeiro) para cada combinação das proposições atômicas.

2. **Classificar a Proposição**: Determinar se a proposição é uma **Tautologia**, **Contradição** ou **Contingência**.

As proposições envolvem operações lógicas como conjunção (`e`), disjunção (`ou`) e negação (`não`).

## Como Jogar

1. **Inicie o jogo** executando o script Python:

   ```bash
   python3 jogo_logica.py

    Escolha o modo de jogo:
        Digite 1 para Um Jogador.
        Digite 2 para Dois Jogadores.

    Rodada do Jogador:

        O jogador é apresentado a uma proposição lógica.

        Uma tabela verdade incompleta é exibida.

        Completar a Tabela:
            Para cada combinação de valores das proposições, insira o resultado da proposição composta.
            Utilize 1 para Verdadeiro e 0 para Falso.

        Classificar a Proposição:

            Após completar a tabela, classifique a proposição escolhendo:
                1 para Tautologia
                2 para Contradição
                3 para Contingência

    Pontuação:
        +1 ponto por completar corretamente a tabela verdade.
        +1 ponto por classificar corretamente a proposição.

    Final do Jogo:
        A pontuação total de cada jogador é exibida.
        O jogador com mais pontos é declarado vencedor.
        Em caso de empate, o jogo termina empatado.

Objetivo Educacional

O jogo tem como objetivo principal auxiliar no aprendizado e na prática de lógica proposicional, permitindo que os jogadores:

    Pratiquem a construção de tabelas verdade.
    Aprendam a classificar proposições como tautologias, contradições ou contingências.
    Desenvolvam habilidades de raciocínio lógico.

Requisitos

    Python 3.x instalado no sistema.
    Sistema operacional com suporte a comandos de terminal (Windows, macOS, Linux).

Como Executar

    Clone o repositório ou baixe o zip pelo github.

    Abra o terminal e navegue até o diretório onde o arquivo está salvo.

    Execute o script:

    python3 jogo_logica.py

