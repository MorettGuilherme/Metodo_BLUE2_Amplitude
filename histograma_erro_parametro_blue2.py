# EXPERIMENTO ATLAS - Reconstrução de sinal - Best Linear Unbiased Estimator (BLUE 2) - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 10 de junho de 2024.

# Objetivo do código: análise do erro de estimação do parâmetro da amplitude pelo método Best Linear Unbiased Estimator (BLUE 2).

"""
Organização do Código:

Importação de arquivos.
Leitura dos dados de ocupação: leitura_dados_ocupacao_blue2.py
Leitura dos dados de ruídos: leitura_dados_ruidos_blue2.py
Método: metodo_blue2.py

Funções presentes:

1) Função para o cálculo da estatística do erro de estimação da amplitude.
Entrada: lista com os erros de estimação da amplitude.
Saída: a média, a variância e o desvio padrão do erro de estimação da amplitude.

2) Função para o plote do histograma do erro de estimação da amplitude.
Entrada: lista com os erros de estimação da amplitude e seus dados estatatísticos.
Saída: nada.

3) Função principal.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from termcolor import colored

# Importação dos arquivos.
from leitura_dados_ocupacao_blue2 import *
from leitura_dados_ruidos_blue2 import *
from metodo_blue2 import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Análise do erro de estimação da amplitude pelo método Best Linear Unbiased Estimator (BLUE 2):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### -------------------------- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE ------------------------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude.
def dados_estatisticos_erro_amplitude(lista_erro_amplitude):
    
    # A lista do erro de estimação da amplitude é convertida para o tipo numpy array.
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

### -------------------------------- 2) FUNÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO ERRO DE ESTIMAÇÃO DA AMPLITUDE ------------------------------- ###

# Definição de função para o plot do histograma do erro de estimação da amplitude.
def histograma_erro_amplitude(lista_erro_amplitude, media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude):
    
    # A lista do erro de estimação da amplitude é convertida para o tipo numpy array.
    vetor_erro_amplitude = np.array(lista_erro_amplitude)

    # Nomeação do eixo x de acordo com a amplitude.
    plt.xlabel('Erro de estimação da amplitude (ADC Count)', fontsize = 18)
        
    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)

    # A variável texto recebe uma string com as informações de interesse.
    texto = f"Média: {round(media_erro_amplitude, 6)} \n Variância: {round(var_erro_amplitude, 6)} \n Desvio padrão: {round(desvio_padrao_erro_amplitude, 6)}"

    # Definição do histograma a partir do vetor vetor_erro_amplitude.
    plt.hist(vetor_erro_amplitude, bins = 100, range = [-300, 300], edgecolor = 'black', linewidth = 1.2)
    
    # Posicionamento do texto no gráfico.
    plt.text(0.99, 0.98, texto, horizontalalignment = 'right',
    verticalalignment = 'top',
    transform = plt.gca().transAxes,
    bbox = dict(facecolor = 'white', alpha = 0.5),
    fontsize = 14)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ------------------------------------------------------------- ###

# Definição da função principal (main) do código.
def principal_histograma_erro_amplitude():
    
    # A variável numero_ocupacao armazena o valor digitado da ocupação desejada no terminal pelo usuário.
    n_ocupacao = float(input("Digite o valor da ocupação desejada: "))

    # A variável valores_ocupacao é uma lista com os valores aceitáveis de ocupação de 0 até 100.
    valores_ocupacao = list(range(0,101,10))

    # Caso o valor digitado armazenado na variável numero_ocupacao não estiver presente na lista valores_ocupacao.
    if n_ocupacao not in valores_ocupacao:
    
        # Exibição de uma mensagem de alerta de que a ocupação solicitada é inválida.
        print("\nNúmero de ocupação inválida!\n")
        # A execução do programa é interrompida.
        exit(1) 

    # O tipo da variável numero_ocupacao é convertida para inteiro.
    # Obs.: essa conversão possibilita que a leitura do arquivo possa ser feita corretamente.
    n_ocupacao = int(n_ocupacao)
    
    # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
    n_janelamento = int(input("Digite a quantidade de janelamento: "))

    # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de dois.
    valores_janelamento = list(range(7,20,2))

    # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
    if n_janelamento not in valores_janelamento:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)

    # Chamada ordenada das funções.
    
    Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao) 
    
    Matriz_Dados_OC_sem_pedestal = retirada_pedestal(Matriz_Dados_OC)
    
    vetor_amostras_pulsos, vetor_amplitude_referencia, _ = amostras_pulsos_e_referencia(Matriz_Dados_OC_sem_pedestal)
        
    Matriz_dados_pulsos, vetor_amplitude_referencia = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
              
    Matriz_dados_pulsos_treino, Matriz_dados_pulsos_teste, vetor_amplitude_referencia_treino, vetor_amplitude_referencia_teste = dados_treino_teste_histograma(Matriz_dados_pulsos, vetor_amplitude_referencia)
    
    vetor_dados_ruidos = leitura_dados_ruidos(n_ocupacao)
    
    Matriz_dados_ruidos = amostras_ruidos_janelamento(vetor_dados_ruidos, n_janelamento)
    
    Matriz_covariancia = matriz_covariancia(Matriz_dados_ruidos)
       
    lista_erro_amplitude = metodo_BLUE2(Matriz_dados_pulsos_teste, vetor_amplitude_referencia_teste, Matriz_covariancia, n_janelamento)
    
    media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude = dados_estatisticos_erro_amplitude(lista_erro_amplitude)
    
    histograma_erro_amplitude(lista_erro_amplitude, media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude)
    
# Chamada da função principal (main) do código.
principal_histograma_erro_amplitude()

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

