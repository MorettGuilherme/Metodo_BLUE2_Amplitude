A segunda versão do método Melhor Estimador Linear Não Enviesado (Best Linear Unbiased Estimador - BLUE 2) visa a estimaçaõ da amplitude central. Diferentemente de sua primeira versão, o método fornece o valor da amplitude central estimada e não mais um vetor de parâmetros.
Os resultados foram melhores que o da primeira versão. Pela análise estatística da validação cruzada K-Fold, o janelamento 15 pode ser adotado como sendo o ideal.

As pastas e os arquivos presentes nesse repositório são:

1. Dados_Estatisticos_BLUE2_amplitude_OC
   * Pasta com os arquivos dos dados estatísticos (média, variância e desvio padrão) do erro de estimação da amplitude de acordo com a ocupação para cada um dos janelamentos.
  
2. Dados_Ocupacoes_Free_Running
  * Pasta com os arquivos dos dados dos pulsos de sinais (ADC Count), amplitude de referência (ADC Count), fase de referência (ns) e erro da eletrônica (ADC Count) em cada instante de colisão (ns) para cada uma das ocupações.

3. K_Fold_amplitude_DP_Dados_Estatisticos_BLUE2_OC
  * Pasta com os arquivos dos dados estatísticos (média, variância e desvio padrão) do desvio padrão calculados pela técnica de validação cruzada K-Fold ao decorrer da quantidade de janelamento para cada ocupação.

4. K_Fold_amplitude_media_Dados_Estatisticos_BLUE2_OC
  * Pasta com os arquivos dos dados estatísticos (média, variância e desvio padrão) da média calculados pela técnica de validação cruzada K-Fold ao decorrer da quantidade de janelamento para cada ocupação.

5. K_Fold_amplitude_var_Dados_Estatisticos_BLUE2_OC
  * Pasta com os arquivos dos dados estatísticos (média, variância e desvio padrão) da variância calculados pela técnica de validação cruzada K-Fold ao decorrer da quantidade de janelamento para cada ocupação.

6. Resultados_BLUE2_Amplitude.
  * Essa pasta contém outras pastas com os resultados em formato de gráficos e histogramas obtidos pelo método BLUE 2 para a análise do erro de estimação da amplitude.

7. arquivo_saida_dados_estatisticos_blue2.py
   * Função para o cálculo dos dados estatísticos do erro de estimação pelo método Best Linear Unbiased Estimator (BLUE 2).
   * Instrução para salvar os dados estatísticos do erro de estimação da amplitude para determinada ocupação em um arquivo de saída.
   * Instrução principal do código.

8. grafico_dado_estatistico_janelamento_blue2.py
   * Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.
   * Instrução principal do código.
  
9. grafico_k_fold_blue2.py
   * Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
   * Instrução principal (main) do código.
  
10. histograma_erro_parametro_blue2.py
   * Função para o cálculo da estatística do erro de estimação da amplitude.
   * Função para o plote do histograma do erro de estimação da amplitude.
   * Função principal.

11. k_fold_blue2.py
   * Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
   * Instrução da validação cruzada K-Fold.
   * Instrução principal do código.

12. leitura_dados_ocupacao_blue2.py
   * Função para a leitura dos dados de ocupação.
   * Função para a retirada do pedestal dos pulsos de sinais.
   * Função para a construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.
   * Função para separação em dados de treino e teste.

13. leitura_dados_ruidos_blue2.py
   * Função para a leitura dos dados de ruídos de acordo com a ocupação.
   * Função para a organização dos dados de ruídos de acordo com o janelamento.
   * Função para separação em dados de treino e teste.
   * Função para a construção da matriz de covariância.
   * Função para a construção da matriz de covariância como identidade.

14. metodo_blue2.py
   * Função para a definição do vetor pulso de referência.
   * Função para o método BLUE 1.

IMPORTANTE: os dados das ocupações foram simulados computacionalmente. As características das distribuições são:

* Distribuição amplitude: exponencial com média 100 ADC Count.
* Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ns.
* Pedestal: 30 ADC Count.
* Nível de deformação: 0,01 ADC Count.
* Número de eventos: 2000000.
* Fold: 100.
* Os dados de ruídos para a construção da matriz de covariância foram os mesmo que para os pulsos de sinais.
