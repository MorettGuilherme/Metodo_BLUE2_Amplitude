# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE2) - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 14 de novembro de 2024.

# Objetivo do código: geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação da amplitude pelo método BLUE2.

""" 
Organização do Código:

Importação de arquivos.
Método BLUE2 para a estimação da amplitude: metodo_BLUE2.py

Funções presentes:

1) Função para o cálculo dos dados estatísticos do erro de estimação da amplitude pelo método Best Linear Unbiased Estimator (BLUE2).
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
from metodo_BLUE2 import * 

# Impressão de uma linha que representa o início do programa.
print("\n----------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação da amplitude pelo método Best Linear Unbiased Estimator (BLUE2):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE PELO MÉTODO BLUE2 --------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude pelo método BLUE2.
def dados_estatisticos_erro_estimacao_amplitude_BLUE2(lista_erro_amplitude):
    
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
    
### --------------------------------------------------------------------------------------------------------------------------------- ###

### --------- 2) INSTRUÇÃO PARA A IMPRESSÃO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE PELO MÉTODO BLUE2 -------------- ###

# Definição da instrução para a impressão em um arquivo de saída, os dados estatísticos do erro de estimação da amplitude pelo método BLUE2.
def arquivo_saida_dados_estatisticos_erro_estimacao_amplitude_BLUE2(parametro, n_ocupacao, n_janelamento, media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = "Oc,media_erro,var_erro,desvio_padrao_erro\n"

    # Definição da pasta que contém o arquivo de saída.
    pasta_saida = f"Dados_Estatisticos_BLUE2_{parametro}_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"dados_estatisticos_BLUE2_janelamento_{n_janelamento}.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        
        # Abre o arquivo presente no endereço caminho_arquivo_saida como a variável arquivo_saida_dados_estatisticos no modo leitura.
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            
            # A variável primeiro_caractere recebe o primeiro elemento presente no arquivo_saida_dados_estatisticos.
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            
            # Caso não haja nada na variável primeiro_caractere.
            if not primeiro_caractere:
                
                # Abre o arquivo presente no endereço caminho_arquivo_saida como file no modo acrescentar.
                with open(caminho_arquivo_saida, 'a') as file:
                    
                    # Escreve o título no arquivo file.
                    file.write(titulo_arquivo_saida)
    
    # Excessão de erro ao encontrar o arquivo no caminho fornecido.                
    except FileNotFoundError:
        
        # Abre o arquivo presente no endereço caminho_arquivo_saida como file no modo escrita.
        with open(caminho_arquivo_saida, 'w') as file:
            
            # Escreve o título no arquivo file.
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        
        # Abre o arquivo presente no endereço caminho_arquivo_saida como arquivo_saida_dados_estatisticos no modo acrescentar.
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            
            # Escrita dos dados de interesse no arquivo_saida_dados_estatisticos.
            arquivo_saida_dados_estatisticos.write(f"{n_ocupacao},{media_erro_estimacao_amplitude},{var_erro_estimacao_amplitude},{desvio_padrao_erro_estimacao_amplitude}\n")
        
    # Excessão.
    except Exception as e:
        
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### --------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------------------------ 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO ----------------------------------------------------- ###

# Definição da instrução principal para esse código.
def principal_arquivo_saida_dados_estatisticos_BLUE2():
    
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
            
            Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
            
            Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_treino_janelado, vetor_amplitude_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado)
    
            lista_erro_estimacao_amplitude = metodo_BLUE2(n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_teste_janelado)
            
            media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude = dados_estatisticos_erro_estimacao_amplitude_BLUE2(lista_erro_estimacao_amplitude)
    
            arquivo_saida_dados_estatisticos_erro_estimacao_amplitude_BLUE2(parametro, n_ocupacao, n_janelamento, media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude)
            
### --------------------------------------------------------------------------------------------------------------------------------- ###

# Chamada da instrução principal do código.
principal_arquivo_saida_dados_estatisticos_BLUE2()

### --------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.
print("\n----------------------------------------------------------------------------------------------------------------------------\n")