# Resumo do trabalho
A análise de séries temporais é crucial para compreender e prever padrões em dados temporais, como preços de ações e índices de mercado. Este trabalho teve como objetivo comparar os modelos de previsão SARIMA, Prophet e LSTM na previsão da série temporal do Índice Ibovespa em diferentes cenários de complexidade. Os dados foram extraídos do site da B3 e os modelos foram treinados no Jupyter Notebook utilizando a linguagem Python e bibliotecas específicas. Os resultados mostraram que o melhor modelo a ser utilizado depende da complexidade da série temporal que está sendo utilizada para a previsão. O modelo LSTM mostrou-se ser muito bom para utilizar em uma série temporal mais complexa como a do Ibovespa, obtendo previsões bem precisas, porém com a necessidade de uma configuração mais trabalhosa e mais tempo de processamento. O Prophet por outro lado se mostrou bem simples de configurar e utilizar, com um tempo mediano para processar os dados e treinar o modelo, porém com um resultado ruim nas previsões desta série temporal, funcionando melhor para séries mais simples com menos ruído ou com uma frequência menor de dados. O SARIMA demonstrou um resultado intermediário com relação à precisão das previsões, com uma complexidade de configuração média e tempo de processamento mais rápido e capacidade de previsão mais confiável se comparado ao modelo Prophet.

# Referências

Defacio, F.S.; Bronzati, V.R. 2019. Mercado de ações: Estudo da previsibilidade utilizando séries temporais aplicadas em machine learning. Dissertação de conclusão de curso. Universidade Presbiteriana Mackenzie, São Paulo, SP, Brasil.

Edisciplinas. 2023. Bloco LSTM Aula 12. Disponível em: https://edisciplinas.usp.br/pluginfile.php/7775634/mod_resource/content/1/Aula12_AM_2023.pdf/. Acesso em: 27 out. 2023.

Facebook. 2023. Prophet: Forecasting at scale. Disponível em: https://facebook.github.io/prophet/. Acesso em: 08 out. 2023.

Fama, E. 1970. Efficient Capital Markets: A Review of Theory and Empirical Work. The Journal of Finance 25: 383–417.

Iglesias, E.; Garrido, A.; Gómez-Ramos, A. 2003. Evaluation of drought management in irrigated areas. Agricultural Economics 29: 211-229.

Medium. 2020. Séries temporais: Parte 2. Disponível em: https://medium.com/@gisely.alves/séries-temporais-parte-2-7162d24c5429. Acesso em: 12 out. 2023.

Nielsen, A. 2020. Practical Time Series Analysis: Prediction with Statistics & Machine Learning. 1ed. O’Reilly Media, Inc., Sebastopol, CA, USA.

Patel, J.; Shah, S.; Thakkar, P.; Kotecha, K. 2015. Predicting stock and stock price index movement using trend deterministic data preparation and machine learning techniques. Expert Systems with Applications 42: 259-268.

Shumway, R.H.; Stoffer, D.S. 2011. Time Series Analysis and Its Applications: With R Examples. 3ed. Springer Science+Business Media, LLC, 233 Spring Street, New York, NY, USA.

Souza, R.L.R. 2011. Previsão do índice Bovespa por meio de redes neurais artificiais: Uma análise comparada aos métodos tradicionais de séries de tempo. Dissertação de Mestrado. Universidade Federal do Rio Grande do Norte, Natal, RN, Brasil.

Souto-Maior, C.D.; Borba, J.A.; da Costa Jr., N.C.A. 2011. S&P 500 Index Direction Forecasting from 1976 to 2010: A Fuzzy System Approach. The International Journal of Digital Accounting Research 11: 111-134.


# Arquivos

1. **[SARIMA.ipynb](https://github.com/AllexRocha/tcc_usp_esalq/blob/master/previsao_SARIMA.ipynb)**
   - **Descrição**: Notebook Jupyter contendo a implementação e análise do modelo SARIMA. Inclui a configuração dos hiperparâmetros, treinamento do modelo, e avaliação de desempenho com os dados do Índice Ibovespa.

2. **[Prophet.ipynb](https://github.com/AllexRocha/tcc_usp_esalq/blob/master/previsao_Prophet.ipynb)**
   - **Descrição**: Notebook Jupyter com a implementação do modelo Prophet. Abrange a configuração dos parâmetros, treinamento do modelo e avaliação das previsões geradas para o Índice Ibovespa.

3. **[LSTM.ipynb](https://github.com/AllexRocha/tcc_usp_esalq/blob/master/Previsao_LSTM.ipynb)**
   - **Descrição**: Notebook Jupyter que detalha a aplicação do modelo LSTM. Inclui o ajuste dos hiperparâmetros, treinamento da rede neural e análise das previsões realizadas para o Índice Ibovespa.

4. **[treino.csv](https://github.com/AllexRocha/tcc_usp_esalq/blob/master/dados_tratados/treino.csv)**
   - **Descrição**: Arquivo CSV contendo os dados de treinamento utilizados para ajustar os modelos de previsão. Inclui informações históricas do Índice Ibovespa para o período de 01 jan. 2010  até 03 maio 2021.

5. **[teste.csv](https://github.com/AllexRocha/tcc_usp_esalq/blob/master/dados_tratados/teste.csv)**
   - **Descrição**: Arquivo CSV com os dados de validação usados para avaliar a performance dos modelos de previsão. Inclui informações históricas do Índice Ibovespa para o período de 03 maio 2021 até 31 dez. 2023.

6. **[previsao.csv](https://github.com/AllexRocha/tcc_usp_esalq/blob/master/dados_tratados/previsao.csv)**
   - **Descrição**: Arquivo CSV contendo as previsões geradas pelos modelos para o Índice Ibovespa. Inclui informações históricas do Índice Ibovespa para o período de 31 dez. 2023 à 31 maio 2024.


Para executar os arquivos e simular as previsões deve ser usado algum programa capaz de executar arquivos ipynb como jupyter notebook ou vscode.
As bibliotecas necessárias estão no arquivo requirements.txt

O arquivo de dados_tratados possui os dados diários do índice ibovespa de 2010 até 2024
