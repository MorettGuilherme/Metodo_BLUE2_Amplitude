# EXPERIMENTO ATLAS - Reconstrução de sinal - Best Linear Unbiased Estimator (BLUE 2) - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 10 de junho 2024.

# Objetivo do código: geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação da amplitude pelo método Best Linear Unbiased Estimator (BLUE 2).

""" 
Organização do Código:

Importação de arquivos.
Leitura dos dados de ocupação: leitura_dados_ocupacao.py
Leitura dos dados de ruídos: leitura_dados_ruidos_blue2.py
Método: metodo_blue2.py

Funções presentes:

1) Função para o cálculo dos dados estatísticos do erro de estimação pelo método Best Linear Unbiased Estimator (BLUE 2).
Entrada: lista com o erro de estimação da amplitude.
Saída: a média, a variância e o desvio padrão do erro de estimação da amplitude.

2) Instrução para salvar os dados estatísticos do erro de estimação da amplitude para determinada ocupação em um arquivo de saída.
Entrada: a média, a variância e o desvio padrão do erro de estimação da amplitude.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from termcolor import colored
import time
from tqdm import tqdm

# Importação dos arquivos.
from leitura_dados_ocupacao_blue2 import *
from leitura_dados_ruidos_blue2 import *
from metodo_blue2 import * 

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação da amplitude pelo método Best Linear Unbiased Estimator (BLUE 2):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------------------ 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE --------------------------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude.
def dados_estatisticos_erro_amplitude(lista_erro_amplitude):
    
    # A lista do erro da amplitude é convertida para o tipo numpy array.
    vetor_erro_amplitude = np.array(lista_erro_amplitude)

    # Cálculo da média do erro de estimação da amplitude.
    media_erro_amplitude = np.mean(vetor_erro_amplitude)

    # Cálculo da variância do erro de estimação da amplitude.
    var_erro_amplitude = np.var(vetor_erro_amplitude)

    # Cálculo do desvio padrão do erro de estimação da amplitude.
    desvio_padrao_erro_amplitude = np.std(vetor_erro_amplitude)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação da amplitude.
    return media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------- 2) FUNÇÃO PARA A IMPRESSÃO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE -------------------------------- ###

# Definição da função para a impressão em um arquivo de saída, os dados estatísticos do erro da amplitude.
def arquivo_saida_dados_estatisticos_erro_amplitude(parametro, n_ocupacao, n_janelamento, media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = "Oc,media_erro,var_erro,desvio_padrao_erro\n"

    # Definição da pasta em que contém o arquivo de saída.
    pasta_saida = f"Dados_Estatisticos_BLUE2_{parametro}_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"dados_estatisticos_BLUE2_janelamento_{n_janelamento}.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Verifica se o arquivo existe e está vazio
    try:
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            if not primeiro_caractere:
                # Arquivo está vazio, escreva o título
                with open(caminho_arquivo_saida, 'a') as file:
                    file.write(titulo_arquivo_saida)
    except FileNotFoundError:
        # Se o arquivo não existe, cria e escreve o título
        with open(caminho_arquivo_saida, 'w') as file:
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        # Abre o arquivo de saída no modo de acrescentar (append).
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            # Escrita dos dados de interesse.
            arquivo_saida_dados_estatisticos.write(f"{n_ocupacao},{media_erro_amplitude},{var_erro_amplitude},{desvio_padrao_erro_amplitude}\n")
        
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------------------------------------- 3) FUNÇÃO PRINCIPAL DO CÓDIGO (MAIN) -------------------------------------------------------------- ###

# Definição da função principal (main) para esse código.
def principal_arquivo_saida_dados_estatisticos_blue2():
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 0.
    ocupacao_inicial = 0
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 100.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações.
    incremento_ocupacao = 10
    
    # A variável n_janelamento_inicial armazena o valor inicial do janelamento que é 7.
    n_janelamento_inicial = 7
    
    # A variável n_janelamento_final armazena o valor final do janelamento que é 19.
    n_janelamento_final = 19
    
    # A variável incremento_janelamento armazena o valor do incremento entre os janelamentos.
    incremento_janelamento = 2
    
    # A variável parametro recebe a string "amplitude".
    parametro = "amplitude"
    
    # Para o número de janelamento inicial de 7 até 19 com incremento de 2.
    for n_janelamento in tqdm(range(n_janelamento_inicial, n_janelamento_final+1, incremento_janelamento)):
    
        # Para o número de ocupação inicial de 0 até 100 com incremento de 10.
        for n_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
    
            # Chamada ordenada das funções.
    
            Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao)
    
            vetor_amostras_pulsos, vetor_amplitude_referencia, _ = amostras_pulsos_e_referencia(Matriz_Dados_OC)
            
            Matriz_dados_pulsos, vetor_amplitude_referencia = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
            
            Matriz_dados_pulsos_treino, Matriz_dados_pulsos_teste, vetor_amplitude_referencia_treino, vetor_amplitude_referencia_teste = dados_treino_teste_histograma(Matriz_dados_pulsos, vetor_amplitude_referencia)
            
            vetor_dados_ruidos = leitura_dados_ruidos(n_ocupacao)
            
            Matriz_dados_ruidos = amostras_ruidos_janelamento(vetor_dados_ruidos, n_janelamento) 
            
            Matriz_covariancia = matriz_covariancia(Matriz_dados_ruidos)
    
            lista_erro_amplitude = metodo_BLUE2(Matriz_dados_pulsos_teste, vetor_amplitude_referencia_teste, Matriz_covariancia, n_janelamento)
            
            media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude = dados_estatisticos_erro_amplitude(lista_erro_amplitude)
    
            arquivo_saida_dados_estatisticos_erro_amplitude(parametro, n_ocupacao, n_janelamento, media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude)
            
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Chamada da função principal do código.
principal_arquivo_saida_dados_estatisticos_blue2()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")