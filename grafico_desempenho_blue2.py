# EXPERIMENTO ATLAS - Reconstrução de sinal - Best Linear Unbiased Estimator (BLUE 2) - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 24 de junho de 2024.

# Objetivo do código: gráfico do desempenho (MSE, MAE ou SNR) ao longo das ocupações de acordo com o janelamento ideal para o método Best Linear Unbiased Estimator (BLUE 2) para a estimação da amplitude.

""" 
Organização do Código:

Leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.

Funções presentes:

1) Função para a leitura dos dados do desempenho do método BLUE 2 de todas as ocupações para o janelamento ideal.
Entrada: parâmetro estimado, número do janelamento ideal, opção de avaliação do desempenho.
Saída: matriz com os dados de entrada organizados de acordo com a coluna (número da ocupação, média, variância e desvio padrão do desempenho do método BLUE 2).

2) Instrução para o plote do gráfico do desempenho do método BLUE 2 ao longo das ocupações para o janelamento ideal.
Entrada: matriz dos dados de desempenho do método BLUE 2.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import os
from termcolor import colored

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Plote do gráfico do desempenho (MSE, MAE ou SNR) ao longo das ocupações de acordo com o janelamento ideal para o método Best Linear Unbiased Estimator (BLUE 2):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------------------- 1) FUNÇÃO PARA A LEITURA DOS DADOS ESTATÍSTICOS DO DESEMPENHO DO MÉTODO BLUE 2 ----------------------------------- ###

# Definição da função para a leitura dos dados estatísticos do desempenho do método BLUE 2.
def leitura_dados_estatisticos_desempenho_BLUE2(parametro, n_janelamento_ideal, opcao_avaliacao_desempenho):

    # Nome da pasta em que se encontra o arquivo de entrada dos dados estatísticos do desempenho de acordo com o janelamento ideal.
    pasta_dados_estatisticos_desempenho = f"K_Fold_{parametro}_{opcao_avaliacao_desempenho}_Desempenho_BLUE2_OC"

    # Nome do arquivo de entrada dos dados estatísticos do desempenho de acordo com o janelamento ideal.
    arquivo_dados_estatisticos_desempenho = f"k_fold_{parametro}_{opcao_avaliacao_desempenho}_desempenho_blue2_J_{n_janelamento_ideal}.txt"

    # O caminho para esse arquivo de entrada.
    caminho_arquivo_dados_estatisticos_desempenho = os.path.join(pasta_dados_estatisticos_desempenho, arquivo_dados_estatisticos_desempenho)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_estatisticos_desempenho):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_estatisticos_desempenho, "r") as arquivo_entrada_dados_estatisticos_desempenho:
        
            # Armazena os dados na variável Matriz_Dados_Desempenho.
            Matriz_Dados_Desempenho = np.array(np.loadtxt(arquivo_entrada_dados_estatisticos_desempenho, skiprows = 1, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_estatisticos_desempenho} não existe na pasta {pasta_dados_estatisticos_desempenho}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar em uma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_Desempenho.
    return Matriz_Dados_Desempenho

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------- 2) FUNÇÃO PARA O PLOTE DOS GRÁFICO DO DADO ESTATÍSTICO DO DESEMPENHO AO LONGO DAS OCUPAÇÕES PARA O JANELAMENTO IDEAL ------------ ###

# Definição da função para o plote do gráfico do dado estatístico do desempenho ao longo das ocupações para o janelamento ideal.
def grafico_dado_estatistico_desempenho_BLUE2(opcao_avaliacao_desempenho, Matriz_Dados_Desempenho):
    
    # Definição da variável indice_coluna_ocupações que armazena o valor do índice da coluna das ocupações.
    indice_coluna_ocupacoes = 0
    
    # Definição da variável indice_coluna_media que armazena o valor do índice da coluna das médias.
    indice_coluna_media = 1
    
    # Definição da variável indice_coluna_var que armazena o valor do índice da coluna das variâncias.
    indice_coluna_var = 2
    
    # Definição da variável indice_coluna_DP que armazena o valor do índice da coluna dos desvios padrão.
    indice_coluna_DP = 3
    
    # Definição do eixo das abscissas.
    vetor_ocupacoes = Matriz_Dados_Desempenho[: , indice_coluna_ocupacoes]
    
    # Definição do eixo das ordenadas.
    vetor_dados = Matriz_Dados_Desempenho[:, indice_coluna_media]
    
    # Definição da lista com os valores das barras de erro.
    vetor_barras_erro = Matriz_Dados_Desempenho[:, indice_coluna_DP]
    
    # Comando para o nome do eixo das abscissas.
    plt.xlabel("Ocupação (OC.)", fontsize = 18)
    plt.xticks(fontsize = 16)
    
    # Caso a variável opcao_avalicao_desempenho seja 1.
    if opcao_avaliacao_desempenho == 1:
              
        # Comando para o nome do eixo das ordenadas de acordo com o erro médio quadrático.
        plt.ylabel(r"Média do erro médio quadrático (ADC Count)^2", fontsize = 18)
              
    # Caso a variável opcao_avalicao_desempenho seja 2.
    elif opcao_avaliacao_desempenho == 2:
            
        # Comando para o nome do eixo das ordenadas de acordo com o erro médio absoluto.
        plt.ylabel(r"Média do erro médio absoluto (ADC Count)", fontsize = 18)
        
    # Caso a variável dado_estatistico seja 3 (desvio padrão).
    elif opcao_avaliacao_desempenho == 3:
        
        # Comando para o nome do eixo das ordenadas de acordo com a relação Sinal-Ruído (Signal-to-Noise Ratio - SNR).
        plt.ylabel(r"Média da relação Sinal-Ruído", fontsize = 18)
        
    # Comando que define o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Comando para o plote do gráfico.
    plt.errorbar(vetor_ocupacoes, vetor_dados, vetor_barras_erro, color = 'blue', linestyle = '--', marker = 'o')
    
    # Comando para o grid.
    plt.grid()
    
    # Comando para o plote.
    plt.show()
        
### -------------------------------------------------------------------------------------------------------------------------------------------- ###        
        
### ---------------------------------------------------- 3) FUNÇÃO PRINCIPAL DO CÓDIGO (MAIN) -------------------------------------------------- ###

# Definição da função principal (main) para esse código.
def principal_grafico_dado_estatistico_desempenho_BLUE2():
    
    # Impressão de mensagem no terminal.
    print("Opções de análise:\nErro Médio Quadrático (Mean Squared Error - MSE): 1\nErro Médio Absoluto (Mean Absolute Error - MAE): 2\nRelação Sinal-Ruído (Signal-to-Noise Ratio - SNR): 3\n")

    # A variável opcao_avalicao_desempenho armazena o número do tipo inteiro digitado pelo usuário via terminal.
    opcao_avaliacao_desempenho = int(input("Digite o número da opção desejada: "))

    # A variável valores_dados é uma lista com os valores aceitáveis para opcao_avalicao_desempenho.
    valores_avaliacoes_desempenho = list(range(1,4,1))
    
    # Caso a variável opcao_avaliacao_desempenho seja igual a 1.
    if opcao_avaliacao_desempenho == 1:
            
        # A variável mecanismo_desempenho recebe a string "MSE".
        mecanismo_desempenho = "MSE"
            
    # Caso a variável opcao_avaliacao_desempenho seja igual a 2.
    elif opcao_avaliacao_desempenho == 2:
          
        # A variável mecanismo_desempenho recebe a string "MAE".  
        mecanismo_desempenho = "MAE"    
            
    # Caso a variável opcao_avaliacao_desempenho seja igual a 3.
    elif opcao_avaliacao_desempenho == 3:
           
        # A variável mecanismo_desempenho recebe a string "SNR".
        mecanismo_desempenho = "SNR"  

    # Caso o valor digitado armazenado na variável pcao_avaliacao_desempenho não estiver presente na lista valores_avaliacoes_desempenho.
    if opcao_avaliacao_desempenho not in valores_avaliacoes_desempenho:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
          
    # A variável parametro recebe a string "amplitude".
    parametro = "amplitude"
    
    # A variável n_janelamento_ideal recebe o valor do janelamento ideal do método BLUE 2.
    # Obs.: essa análise deve ser realizada previamento pela interpretação dos gráficos gerados pelo K-Fold (grafico_k_fold_blue2).
    n_janelamento_ideal = 15
        
    # Chamada das funções.
    
    Matriz_Dados_Desempenho = leitura_dados_estatisticos_desempenho_BLUE2(parametro, n_janelamento_ideal, mecanismo_desempenho)
    grafico_dado_estatistico_desempenho_BLUE2(opcao_avaliacao_desempenho, Matriz_Dados_Desempenho)
    
# Chamada da função principal do código.
principal_grafico_dado_estatistico_desempenho_BLUE2()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")
    
    
            
    
    
    
    