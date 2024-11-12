<!DOCTYPE html>
<html>
<head>
    <title>Jogo de Tabelas Verdade de Lógica Proposicional</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0 15%;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .badge {
            display: inline-block;
            padding: 5px 10px;
            background-color: #4B8BBE;
            color: white;
            border-radius: 3px;
            text-decoration: none;
            font-size: 14px;
        }
        code {
            background-color: #ecf0f1;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul, ol {
            margin-left: 20px;
        }
        a {
            color: #2980b9;
            text-decoration: none;
        }
        hr {
            border: none;
            border-top: 1px solid #bdc3c7;
            margin: 40px 0;
        }
    </style>
</head>
<body>

<h1>Jogo de Tabelas Verdade de Lógica Proposicional</h1>

<a href="#" class="badge">Python</a>

<p>Este é um jogo educativo desenvolvido em Python que testa e aprimora seus conhecimentos em lógica proposicional, especificamente na construção e classificação de tabelas verdade.</p>

<h2>Descrição do Jogo</h2>

<p>O jogo permite a participação de um ou dois jogadores. Em cada rodada, os jogadores são apresentados a diferentes proposições lógicas e devem:</p>

<ol>
    <li><strong>Completar a Tabela Verdade</strong>: Fornecer os valores lógicos (<code>0</code> para falso e <code>1</code> para verdadeiro) para cada combinação das proposições atômicas.</li>
    <li><strong>Classificar a Proposição</strong>: Determinar se a proposição é uma <strong>Tautologia</strong>, <strong>Contradição</strong> ou <strong>Contingência</strong>.</li>
</ol>

<p>As proposições envolvem operações lógicas como conjunção (<code>e</code>), disjunção (<code>ou</code>) e negação (<code>não</code>). O jogo inclui proposições como:</p>

<ul>
    <li><code>p e q</code></li>
    <li><code>p ou r</code></li>
    <li><code>p ou não q</code></li>
    <li><code>p e não x</code></li>
</ul>

<h2>Como Jogar</h2>

<ol>
    <li><strong>Inicie o jogo</strong> executando o script Python:</li>
</ol>

<pre><code>python3 jogo_logica.py</code></pre>

<ol start="2">
    <li><strong>Escolha o modo de jogo</strong>:</li>
</ol>

<ul>
    <li>Digite <code>1</code> para <strong>Um Jogador</strong>.</li>
    <li>Digite <code>2</code> para <strong>Dois Jogadores</strong>.</li>
</ul>

<ol start="3">
    <li><strong>Rodada do Jogador</strong>:</li>
</ol>

<ul>
    <li>O jogador é apresentado a uma proposição lógica.</li>
    <li>Uma tabela verdade incompleta é exibida.</li>
    <li><strong>Completar a Tabela</strong>:</li>
    <ul>
        <li>Para cada combinação de valores das proposições atômicas, insira o resultado da proposição composta.</li>
        <li>Utilize <code>1</code> para <strong>Verdadeiro</strong> e <code>0</code> para <strong>Falso</strong>.</li>
    </ul>
    <li><strong>Classificar a Proposição</strong>:</li>
    <ul>
        <li>Após completar a tabela, classifique a proposição escolhendo:</li>
        <ul>
            <li><code>1</code> para <strong>Tautologia</strong></li>
            <li><code>2</code> para <strong>Contradição</strong></li>
            <li><code>3</code> para <strong>Contingência</strong></li>
        </ul>
    </ul>
</ul>

<ol start="4">
    <li><strong>Pontuação</strong>:</li>
</ol>

<ul>
    <li><strong>+1 ponto</strong> por completar corretamente a tabela verdade.</li>
    <li><strong>+1 ponto</strong> por classificar corretamente a proposição.</li>
</ul>

<ol start="5">
    <li><strong>Final do Jogo</strong>:</li>
</ol>

<ul>
    <li>A pontuação total de cada jogador é exibida.</li>
    <li>O jogador com mais pontos é declarado vencedor.</li>
    <li>Em caso de empate, o jogo termina empatado.</li>
</ul>

<h2>Objetivo Educacional</h2>

<p>O jogo tem como objetivo principal auxiliar no aprendizado e na prática de lógica proposicional, permitindo que os jogadores:</p>

<ul>
    <li>Pratiquem a construção de tabelas verdade.</li>
    <li>Aprendam a classificar proposições como tautologias, contradições ou contingências.</li>
    <li>Desenvolvam habilidades de raciocínio lógico e pensamento crítico.</li>
</ul>

<h2>Requisitos</h2>

<ul>
    <li>Python 3.x instalado no sistema.</li>
    <li>Sistema operacional com suporte a comandos de terminal (Windows, macOS, Linux).</li>
</ul>

<h2>Como Executar</h2>

<ol>
    <li><strong>Clone o repositório</strong> ou copie o código para um arquivo chamado <code>jogo_logica.py</code>.</li>
    <li><strong>Abra o terminal</strong> e navegue até o diretório onde o arquivo está salvo.</li>
    <li><strong>Execute o script</strong>:</li>
</ol>

<pre><code>python3 jogo_logica.py</code></pre>

<h2>Contribuições</h2>

<p>Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou novas funcionalidades.</p>

<hr>

<p><strong>Divirta-se jogando e aprimorando seus conhecimentos em lógica proposicional!</strong></p>

</body>
</html>
