# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE2) - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 25 de julho de 2024.

# Objetivo do código: cálculo do desempenho do método Best Linear Unbiased Estimator (BLUE2) para a estimação da amplitude pela validação cruzada K-Fold.

""" 
Organização do código:

Importação de arquivos.
Método BLUE2 para a estimação da amplitude: metodo_BLUE2.py

Funções presentes:

1) Instrução para salvar em arquivos os dados estatísticos do desempenho do método BLUE2 para a estimação da amplitude.
Entrada: parâmetro, número de ocupação, número do janelamento ideal, média do desempenho, variância do desempenho, desvio padrão do desempenho e o mecanismo do desempenho.
Saída: nada.

2) Função para o cálculo do desempenho do método BLUE2 pelo Erro Médio de Estimação (EME).
Entrada: número de elementos presentes em cada bloco e lista dos erros de estimação para cada bloco do K-Fold.
Saída: média do EME, variância do EME e desvio padrão do EME.

3) Função para o cálculo do desempenho do método BLUE2 pelo Erro Médio Quadrático (Mean Squared Error - MSE).
Entrada: número de elementos presentes em cada bloco e lista dos erros de estimação para cada bloco do K-Fold.
Saída: média do MSE, variância do MSE e desvio padrão do MSE.

4) Função para o cálculo do desempenho do método BLUE2 pelo Erro Médio Absoluto (Mean Absolute Error - MAE).
Entrada: número de elementos presentes em cada bloco e lista dos erros de estimação para cada bloco do K-Fold.
Saída: média do MAE, variância do MAE e desvio padrão do MAE.

5) Função para o cálculo do desempenho do método BLUE2 pela Relação Sinal-Ruído (Signal-to-Noise Ratio - SNR).
Entrada: lista dos parâmetros de referência e lista dos erros de estimação para cada bloco do K-Fold.
Saída: média do SNR, variância do SNR e desvio padrão do SNR.

6) Função para o cálculo do desempenho do método BLUE2 pelo desvio padrão (DP).
Entrada: número de elementos presentes em cada bloco e lista dos erros de estimação para cada bloco do K-Fold.
Saída: valor do desvio padrão de cada bloco.

7) Instrução da validação cruzada K-Fold adaptada para o cálculo do desempenho do método BLUE 2 para a estimação da amplitude.
Entrada: parâmetro, número de ocupação, número do janelamento ideal, opção da avaliação do desempenho, matriz com os pulsos de sinais, vetor do parâmetro de referência e a matriz de covariância.
Saída: nada.

8) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação de bibliotecas.
import numpy as np
import os
from tqdm import tqdm
import time
from termcolor import colored

# Importação dos arquivos.
from metodo_BLUE2 import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída pela técnica de validação cruzada K-Fold para a estimação da amplitude pelo método Best Linear Unbiased Estimator (BLUE2):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------------ 1) INSTRUÇÃO PARA SALVAR OS DADOS ESTATÍSTICOS DO K-FOLD PARA A ESTIMAÇÃO DA AMPLITUDE PELO MÉTODO BLUE2 -------------------- ###

# Definição da instrução para salvar os dados estatísticos do desempenho do método BLUE2 para a estimação da amplitude em arquivo de saída.
def arquivo_saida_dados_desempenho_BLUE2(parametro, n_ocupacao, n_janelamento_ideal, media_dado_desempenho, var_dado_desempenho, DP_dado_desempenho, mecanismo_desempenho):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = f"n_ocupacao,media_{mecanismo_desempenho},var_{mecanismo_desempenho},DP_{mecanismo_desempenho}\n"

    # Definição da pasta que contém o arquivo de saída.
    pasta_saida = f"K_Fold_{parametro}_{mecanismo_desempenho}_Desempenho_BLUE2_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saída.
    arquivo_saida = f"k_fold_{parametro}_{mecanismo_desempenho}_desempenho_BLUE2_J_{n_janelamento_ideal}.txt"

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
            arquivo_saida_dados_estatisticos.write(f"{n_ocupacao},{media_dado_desempenho},{var_dado_desempenho},{DP_dado_desempenho}\n")
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------- 2) FUNÇÃO PARA O CÁLCULO DO ERRO MÉDIO DE ESTIMAÇÃO (MEAN SQUARED ERROR - EME) ---------------------------------- ###

# Definição da função para o cálculo do erro médio de estimação (EME).
def EME(numero_elementos_bloco, bloco_erro_estimacao):
    
    # Cálculo do EME.
    valor_EME = (1/numero_elementos_bloco)*(sum(bloco_erro_estimacao))
    
    # A função retorna o valor do EME.
    return valor_EME

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### --------------------------- 3) FUNÇÃO PARA O CÁLCULO DO ERRO MÉDIO QUADRÁTICO (MEAN SQUARED ERROR - MSE) ----------------------------------- ###

# Definição da função para o cálculo do erro médio quadrático (MSE).
def MSE(numero_elementos_bloco, bloco_erro_estimacao):
    
    # Eleva todos os elementos do bloco_erro_estimacao ao quadrado e salva o resultado na lista bloco_erro_estimacao_quadratico.
    bloco_erro_estimacao_quadratico = [elemento**2 for elemento in bloco_erro_estimacao]
    
    # Cálculo do MSE.
    valor_MSE = (1/numero_elementos_bloco)*(sum(bloco_erro_estimacao_quadratico))
    
    # A função retorna o valor do MSE.
    return valor_MSE

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### --------------------------- 4) FUNÇÃO PARA O CÁLCULO DO ERRO MÉDIO ABSOLUTO (MEAN ABSOLUTE ERROR - MAE) ------------------------------------ ###

# Definição da função para o cálculo do erro médio absoluto (MAE).
def MAE(numero_elementos_bloco, bloco_erro_estimacao):
    
    # Aplica o módulo em todos os elementos do bloco_erro_estimacao e salva o resultado na lista bloco_erro_estimacao_modulo.
    bloco_erro_estimacao_modulo = [np.abs(elemento) for elemento in bloco_erro_estimacao]
    
    # Cálculo do MAE.
    valor_MAE = (1/numero_elementos_bloco)*(sum(bloco_erro_estimacao_modulo))
    
    # A função retorna o valor do MAE.
    return valor_MAE

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### --------------------------- 5) FUNÇÃO PARA O CÁLCULO DA RELAÇÃO SINAL-RUÍDO (SIGNAL-TO-NOISE RATIO - SNR) ---------------------------------- ###

# Definição da função para o cálculo da relação sinal-ruído (Signal-to-Noise Ratio - SNR).
def SNR(bloco_parametro_referencia, bloco_erro_estimacao):
    
    # Eleva todos os elementos do bloco_parametro_referencia ao quadrado e salva o resultado na lista bloco_parametro_referencia_quadratico.
    bloco_parametro_referencia_quadratico = [elemento**2 for elemento in bloco_parametro_referencia]
    
    # Eleva todos os elementos do bloco_erro_estimacao ao quadrado e salva o resultado na lista bloco_erro_estimacao_quadratico.
    bloco_erro_estimacao_quadratico = [elemento**2 for elemento in bloco_erro_estimacao]
    
    # Cálculo do SNR.
    valor_SNR = 10*np.log10((sum(bloco_parametro_referencia_quadratico))/(sum(bloco_erro_estimacao_quadratico)))
    
    # A função retorna o valor do SNR.
    return valor_SNR

## --------------------------------------------------------------------------------------------------------------------------------------------- ###

### --------------------------------------------- 6) FUNÇÃO PARA O CÁLCULO DO DESVIO PADRÃO (DP) ----------------------------------------------- ###

# Definição da função para o cálculo do desvio padrão.
def DP(numero_elementos_bloco, bloco_erro_estimacao):
    
    # Eleva todos os elementos do bloco_erro_estimacao ao quadrado e salva o resultado na lista bloco_erro_estimacao_quadratico.
    bloco_erro_estimacao_quadratico = [elemento**2 for elemento in bloco_erro_estimacao]

    # Cálculo do desvio padrão.
    valor_DP = np.sqrt((np.sum(bloco_erro_estimacao_quadratico))/(numero_elementos_bloco))
    
    # A função retorna o valor valor_DP.
    return valor_DP

## --------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------- 7) INSTRUÇÃO PARA A VALIDAÇÃO CRUZADA K-FOLD ADAPTADA PARA O CÁLCULO DO DESEMPENHO DO MÉTODO BLUE 2 PARA A ESTIMAÇÃO DA AMPLITUDE PELO MÉTODO BLUE2 ------------- ###

# Definição da instrução da técnica de validação cruzada K-Fold para o cálculo do desempenho do método BLUE2 para a estimação da amplitude.
def K_fold_desempenho_BLUE2(parametro, n_ocupacao, n_janelamento_ideal, opcao_avaliacao_desempenho, Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado):

    # Caso a variável opcao_avaliacao_desempenho seja igual a 1.
    if opcao_avaliacao_desempenho == 1:
        
        # A variável mecanismo_desempenho recebe a string "EME".
        mecanismo_desempenho = "EME"
    
    # Caso a variável opcao_avaliacao_desempenho seja igual a 2.
    if opcao_avaliacao_desempenho == 2:
            
        # A variável mecanismo_desempenho recebe a string "MSE".
        mecanismo_desempenho = "MSE"
            
    # Caso a variável opcao_avaliacao_desempenho seja igual a 3.
    elif opcao_avaliacao_desempenho == 3:
          
        # A variável mecanismo_desempenho recebe a string "MAE".  
        mecanismo_desempenho = "MAE"    
            
    # Caso a variável opcao_avaliacao_desempenho seja igual a 4.
    elif opcao_avaliacao_desempenho == 4:
           
        # A variável mecanismo_desempenho recebe a string "SNR".
        mecanismo_desempenho = "SNR" 
        
    # Caso a variável opcao_avaliacao_desempenho seja igual a 5.
    elif opcao_avaliacao_desempenho == 5:
           
        # A variável mecanismo_desempenho recebe a string "DP".
        mecanismo_desempenho = "DP"   
    
    # Criação da lista vazia blocos_pulsos_sinais.
    blocos_pulsos_sinais = []

    # Criação da lista vazia blocos_amplitude_referencia.
    blocos_amplitude_referencia = []
    
    # Criação da variável quantidade_blocos que armazena a quantidade de blocos.
    quantidade_blocos = 100

    # Definição da quantidade de elementos de cada bloco.
    quantidade_elementos_bloco = len(Matriz_Pulsos_Sinais_Janelado) // quantidade_blocos
    
    # Para i de início em zero até a quantidade de elementos de amostras com incremento igual a quantidade_elementos_bloco.
    for i in range(0, len(Matriz_Pulsos_Sinais_Janelado), quantidade_elementos_bloco):
    
        # Definição do bloco de pulsos de sinais.
        bloco_pulsos_sinais = Matriz_Pulsos_Sinais_Janelado[i:i+quantidade_elementos_bloco]
        # O bloco dos pulsos de sinais é acrescentado a lista dos blocos dos pulsos de sinais.
        blocos_pulsos_sinais.append(bloco_pulsos_sinais)
    
        # Definição do bloco dos dados da amplitude de referência.
        bloco_amplitude_referencia = vetor_amplitude_referencia_janelado[i:i+quantidade_elementos_bloco]
        # O bloco da amplitude de referência é acrescentado a lista dos blocos da amplitude de referência.
        blocos_amplitude_referencia.append(bloco_amplitude_referencia)
    
    # Definição da lista vazia lista_blocos_valores_desempenho.
    lista_blocos_valores_desempenho = []
     
    # Para indice_teste de zero até o tamanho da matriz de dados de entrada com incremento igual a quantidade de elementos no bloco.
    for indice_teste in range(0, len(blocos_pulsos_sinais)):
        
        # Definição do bloco_teste_pulsos_sinais como sendo aquele de índice igual ao indice_teste.
        bloco_teste_pulsos_sinais = blocos_pulsos_sinais[indice_teste]
        
        # Definição do bloco_treino_pulsos_sinais como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_pulsos_sinais = blocos_pulsos_sinais[:indice_teste]+blocos_pulsos_sinais[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_pulsos_sinais em sequência, uma lista unidimensional.
        bloco_treino_pulsos_sinais = [elemento for sublista in bloco_treino_pulsos_sinais for elemento in sublista]
        
        # Definição do bloco_teste_amplitude_referencia como sendo aquele de índice igual ao indice_teste.
        bloco_teste_amplitude_referencia = blocos_amplitude_referencia[indice_teste]
        
        # Definição do bloco_treino_amplitude_referencia como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_amplitude_referencia = blocos_amplitude_referencia[:indice_teste]+blocos_amplitude_referencia[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_parametro_referencia em sequência, uma lista unidimensional.
        bloco_treino_amplitude_referencia = [elemento for sublista in bloco_treino_amplitude_referencia for elemento in sublista]
        
        # A variável bloco_lista_erro_parametro recebe o valor de retorno da função metodo_BLUE2.
        bloco_lista_erro_estimacao_parametro = metodo_BLUE2(bloco_treino_pulsos_sinais, bloco_teste_pulsos_sinais, bloco_teste_amplitude_referencia, n_janelamento_ideal)
        
        # Caso a variável opcao_avaliacao_desempenho seja igual a 1.
        if opcao_avaliacao_desempenho == 1:
            
            # A variável bloco_valor_EME recebe o valor de retorno da função EME.
            bloco_valor_EME = EME(quantidade_elementos_bloco, bloco_lista_erro_estimacao_parametro)
            # O valor de bloco_valor_EME é acrescentado a lista lista_blocos_valores_desempenho.
            lista_blocos_valores_desempenho.append(bloco_valor_EME)
        
        # Caso a variável opcao_avaliacao_desempenho seja igual a 2.
        elif opcao_avaliacao_desempenho == 2:
            
            # A variável bloco_valor_MSE recebe o valor de retorno da função MSE.
            bloco_valor_MSE = MSE(quantidade_elementos_bloco, bloco_lista_erro_estimacao_parametro)
            # O valor de bloco_valor_MSE é acrescentado a lista lista_blocos_valores_desempenho.
            lista_blocos_valores_desempenho.append(bloco_valor_MSE)
            
        # Caso a variável opcao_avaliacao_desempenho seja igual a 3.
        elif opcao_avaliacao_desempenho == 3:
            
            # A variável bloco_valor_MAE recebe o valor de retorno da função MAE.
            bloco_valor_MAE = MAE(quantidade_elementos_bloco, bloco_lista_erro_estimacao_parametro)
            # O valor de bloco_valor_MAE é acrescentado a lista lista_blocos_valores_desempenho.
            lista_blocos_valores_desempenho.append(bloco_valor_MAE)
            
        # Caso a variável opcao_avaliacao_desempenho seja igual a 4.
        elif opcao_avaliacao_desempenho == 4:
           
           # A variável bloco_valor_SNR recebe o valor de retorno da função SNR.
           bloco_valor_SNR = SNR( bloco_teste_amplitude_referencia, bloco_lista_erro_estimacao_parametro)
           # O valor de bloco_valor_SNR é acrescentado a lista lista_blocos_valores_desempenho.
           lista_blocos_valores_desempenho.append(bloco_valor_SNR)
           
        # Caso a variável opcao_avaliacao_desempenho seja igual a 5.
        elif opcao_avaliacao_desempenho == 5:
            
           # A variável bloco_valor_DP recebe o valor de retorno da função DP.
           bloco_valor_DP = DP(quantidade_elementos_bloco, bloco_lista_erro_estimacao_parametro)
           # O valor de bloco_valor_DP é acrescentado a lista lista_blocos_valores_desempenho.
           lista_blocos_valores_desempenho.append(bloco_valor_DP)
            
    # Cálculo dos dados estatísticos do desempenho.
    media_desempenho = np.mean(lista_blocos_valores_desempenho)
    var_desempenho = np.var(lista_blocos_valores_desempenho)
    DP_desempenho = np.std(lista_blocos_valores_desempenho)
     
    # Salva as informações dos dados estatísticos da análise do desempenho do método BLUE2.
    arquivo_saida_dados_desempenho_BLUE2(parametro, n_ocupacao, n_janelamento_ideal, media_desempenho, var_desempenho, DP_desempenho, mecanismo_desempenho)   
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ### 

### ---------------------------------------------- 8) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ----------------------------------------------------- ###
  
# Definição da instrução principal (main) do código.
def principal_desempenho_BLUE2():
    
    # A variável parametro recebe a string "amplitude".
    parametro = "amplitude"
    
    # Impressão de mensagem solicitando ao usuário digitar a opção desejada para a análise do desempenho.
    print("Opções de avaliações de desempenho do método:\nErro Médio Estimação (EME) - 1\nErro Médio Quadrático (Mean Squared Error - MSE) - 2\nErro Médio Absoluto (Mean Absolute Erro - MAE) - 3\nRelação Sinal-Ruído (Signal-to-Noise Ratio - SNR) - 4\nDesvio Padrão (DP) - 5")
    
    # A variável opcao_avaliacao_desempenho armazena o valor digitado pelo usuário no terminal.
    opcao_avaliacao_desempenho = int(input("Digite o número da opção desejada: "))
    
    # A variável lista_opcoes_avaliacoes_desempenho armazena os valores disponíveis para a análise do desempenho.
    lista_opcoes_avaliacoes_desempenho = list(range(1, 6, 1))
    
    # Caso o valor digitado pelo usuário não estiver na lista.
    if opcao_avaliacao_desempenho not in lista_opcoes_avaliacoes_desempenho:
        
        # Exibição de mensagem de alerta que a opção é inválida.
        print("Por favor digite uma opção válida!\n")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 0.
    ocupacao_inicial = 0
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 100.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações que é 10.
    incremento_ocupacao = 10
    
    # A variável n_janelamento_ideal recebe o valor do janelamento ideal do método BLUE 2.
    # Obs.: essa análise deve ser realizada previamento pela interpretação dos gráficos gerados pelo K-Fold (grafico_k_fold_BLUE2).
    n_janelamento_ideal = 15
    
    # Definição do tempo inicial.
    tempo_inicial = time.time()
    
    # Para o número de ocupações de 0 até 100 com incremento de 10. 
    for n_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
        
        # Chamada ordenada das funções.
    
        Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao)
            
        Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
            
        vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
        
        Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento_ideal)
            
        Matriz_Pulsos_Sinais_Janelado, vetor_fase_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento_ideal)
    
        K_fold_desempenho_BLUE2(parametro, n_ocupacao, n_janelamento_ideal, opcao_avaliacao_desempenho, Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado)
    
    # Definição do tempo final.
    tempo_final = time.time()
    
    # Cálculo do tempo de execução.
    tempo_execucao = tempo_final-tempo_inicial
    
    # Impressão do tempo de execução.
    print(f"Tempo de execução: {tempo_execucao}")
     
# Chamada da instrução principal do código.
principal_desempenho_BLUE2()       
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")