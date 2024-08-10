Analisador Preditivo para Análise Sintática
Este projeto implementa um analisador preditivo para análise sintática de cadeias de entrada com base em uma tabela de análise preditiva. O analisador utiliza a técnica de análise preditiva para verificar se uma cadeia de entrada é aceita por uma gramática livre de contexto definida por uma tabela de análise.

• Funcionalidades:

 1. Carregamento da Tabela de Análise: Importa e processa uma tabela de análise preditiva a partir de um arquivo CSV.
 2. Análise Sintática: Realiza a análise preditiva da cadeia de entrada com base na tabela de análise, verificando se a cadeia é aceita pela gramática definida.
 3. Tratamento de Erros: Detecta e relata erros de análise, como mismatches de símbolos e produções não encontradas.
    
• Estrutura do Projeto:

 1. TabelaDeAnalise.py: Contém a classe TabelaDeAnalise, responsável pelo carregamento e processamento da tabela de análise a partir de um arquivo CSV.
 2. AnalisadorPreditivo.py.py: Contém a classe AnalisadorPreditivo, que utiliza a tabela de análise para realizar a análise preditiva de cadeias de entrada.
 3. Main.py: Script principal para executar o analisador preditivo, configurando a tabela de análise e a cadeia de entrada para análise.
