# EXPERIMENTO ATLAS - Reconstrução de sinal - Melhor Estimador Linear Não Enviesado - Best Linear Unbiased Estimator (BLUE2) - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 02 de setembro de 2024.

# Objetivo do código: aplicação do método Best Linear Unbiased Estimator (BLUE2) para a estimação da amplitude.

"""
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento desejado.
Os dados de entrada das ocupações no formato de arquivo texto (txt) contém informações sobre os pulsos de sinais (ADC Count), a amplitude de referência (ADC Count), a fase de referência (ns) e o ruído eletrônico (ADC Count).
O valor de referência considerado para o pedestal foi de 30 ADC Count.

Funções presentes:

1) Função para a definição do vetor pulso de referência.
Entrada: número de janelamento.
Saída: vetor pulso de referência para cada instante de tempo de acordo com o janelamento.

2) Função para o método BLUE2.
Entrada: matriz com os pulsos de sinais da etapa de treino, matriz com os pulsos de sinais da etapa de teste, vetor com a amplitude de referência e o número de janelamento.
Saída: lista com o erro de estimação pelo método BLUE 2 para a amplitude.
"""

# Importação das bibliotecas.
import numpy as np

# Importação dos arquivos.
from leitura_dados_ocupacao_BLUE2 import *
from leitura_dados_ruidos_BLUE2 import *

### ------------------------------------------------- 1) FUNÇÃO PARA O PULSO DE REFERÊNCIA ----------------------------------------------------- ###

# Definição da função para o vetor pulso de referência de acordo com o janelamento.
def pulso_referencia(n_janelamento):
    
    # Criação das variáveis que armazenam os valores dos pulsos de referência para cada cada instante de tempo.
    h_tm225 = 0.0 # t = -225,0 ns
    h_tm200 = 0.0 # t = -220,0 ns
    h_tm175 = 0.0 # t = -175,0 ns
    h_tm150 = 0.0 # t = -150,0 ns
    h_tm125 = 0.0 # t = -125,0 ns
    h_tm100 = 0.0 # t = -100,0 ns
    h_tm75 = 2.304e-05 # t = -75,0 ns
    h_tm50 = 0.0172264 # t = -50,0 ns
    h_tm25 = 0.452445 # t = -25,0 ns
    h_t0 = 1.0 # t = 0,0 ns
    h_tM25 = 0.563307 # t = 25,0 ns
    h_tM50 = 0.149335 # t = 50,0 ns
    h_tM75 = 0.0423598 # t = 75,0 ns
    h_tM100 = 0.00480767 # t = 100,0 ns
    h_tM125 = 0.0 # t = 125,0 ns
    h_tM150 = 0.0 # t = 150,0 ns
    h_tM175 = 0.0 # t = 175,0 ns
    h_tM200 = 0.0 # t = 200,0 ns
    h_tM225 = 0.0 # t = 225,0 ns
       
    # Caso o janelamento seja igual a 7.
    if n_janelamento == 7:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 7 no intervalo de tempo de -75,0 a 75,0 ns.
        vetor_pulso_referencia = np.array([h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75])
        
    # Caso o janelamento seja igual a 9.
    elif n_janelamento == 9:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 9 no intervalo de tempo de -100,0 a 100,0 ns.
        vetor_pulso_referencia = np.array([h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100])
        
    # Caso o janelamento seja igual a 11.
    elif n_janelamento == 11:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 11 no intervalo de tempo de -125,0 a 125,0 ns.
        vetor_pulso_referencia = np.array([h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125])
        
    # Caso o janelamento seja igual a 13.
    elif n_janelamento == 13:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 13 no intervalo de tempo de -150,0 a 150,0 ns.
        vetor_pulso_referencia = np.array([h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150])
        
    # Caso o janelamento seja igual a 15.
    elif n_janelamento == 15:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 15 no intervalo de tempo de -175,0 a 175,0 ns.
        vetor_pulso_referencia = np.array([h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175])   

    # Caso o janelamento seja igual a 17.
    elif n_janelamento == 17:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 17 no intervalo de tempo de -200,0 a 200,0 ns.
        vetor_pulso_referencia = np.array([h_tm200, h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175, h_tM200]) 
        
    # Caso o janelamento seja igual a 19.
    elif n_janelamento == 19:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 19 no intervalo de tempo de -225,0 a 225,0 ns.
        vetor_pulso_referencia = np.array([h_tm225, h_tm200, h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175, h_tM200, h_tM225])     

    # A função retorna o vetor pulso de referência.
    return vetor_pulso_referencia

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------------------------------- 2) FUNÇÃO PARA O MÉTODO BLUE2 ------------------------------------------------------------- ###

# Definição da função para o método BLUE2.
def metodo_BLUE2(n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_teste_janelado):

    # Criação da lista vazia para armazenar os erros calculados para a amplitude. 
    lista_erro_estimacao_amplitude = []
    
    # A variável Matriz_Covariancia recebe o valor de retorno da função matriz_covariancia.
    Matriz_Covariancia = matriz_covariancia(Matriz_Pulsos_Sinais_Treino_Janelado)
    
    # A variável vetor_h recebe o retorno da função pulso_referencia.
    vetor_h = pulso_referencia(n_janelamento)
         
    # Tenta calcular a inversa da matriz Matriz_Covariancia.
    try:
    # Cálcula a inversa da matriz Matriz_Covariancia usando numpy.linalg.inv.
        Inversa_Matriz_Covariancia = np.linalg.inv(Matriz_Covariancia)
          
    # Caso a matriz Matriz_Covariancia seja singular ou não invertível.  
    except np.linalg.LinAlgError:
    # Impressão de mensagem de erro
        print("A matriz matriz de covariancia não é invertível.")
        
    # Cálculo da transposta da do vetor h.
    transposta_h = np.transpose(vetor_h)
    
    # Cálculo do vetor g1.
    vetor_g1 = (np.dot(Inversa_Matriz_Covariancia, vetor_h))/(np.dot(np.dot(transposta_h, Inversa_Matriz_Covariancia), vetor_h))
    
    # Cálculo da transposta do vetor g1.
    transposta_vetor_g1 = np.transpose(vetor_g1)
    
    # Para o índice de zero até o número de linhas da matriz Matriz_Pulsos_Sinais_Teste_Janelado.
    for indice_linha in range(len(Matriz_Pulsos_Sinais_Teste_Janelado)):
        
        # O vetor vetor_pulsos_sinais corresponde a linha de índice indice_linha da matriz Matriz_Pulsos_Sinais_Teste_Janelado.    
        vetor_pulsos_sinais_teste = Matriz_Pulsos_Sinais_Teste_Janelado[indice_linha]
    
        # A amplitude de referência é o elemento de índice indice_linha do vetor vetor_amplitude_referencia_teste_janelado.
        valor_amplitude_referencia_teste = vetor_amplitude_referencia_teste_janelado[indice_linha]
        
        # Cálculo do valor da amplitude estimada pelo método BLUE2.
        valor_amplitude_estimada = np.dot(transposta_vetor_g1 , vetor_pulsos_sinais_teste)
        
        # Cálculo do erro de estimação da amplitude.
        erro_estimacao_amplitude = valor_amplitude_referencia_teste-valor_amplitude_estimada
    
        # O elemento erro_estimacao_amplitude é adicionado na lista correspondente.    
        lista_erro_estimacao_amplitude.append(erro_estimacao_amplitude)

    # A função retorna a lista lista_erro_estimacao_amplitude.
    return lista_erro_estimacao_amplitude
 
### -------------------------------------------------------------------------------------------------------------------------------------------- ###