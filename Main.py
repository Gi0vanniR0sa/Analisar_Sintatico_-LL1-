from TabelaDeAnalise import TabelaDeAnalise
from AnalisadorPreditivo import AnalisadorPreditivo

def main():
    # Caminho para o arquivo CSV que contém a tabela de análise
    csv_caminho = input("Por favor, forneça o caminho da tabela de analise: ")
    
    # Criação da instância da TabelaDeAnalise com o arquivo CSV
    tabela_analise = TabelaDeAnalise(csv_caminho)
    
    # Criação da instância do AnalisadorPreditivo com a tabela de análise
    analisador = AnalisadorPreditivo(tabela_analise)
    
    # Solicita ao usuário a entrada para análise
    entrada = input("Digite a entrada: ")
    
    # Análise da entrada e exibição do resultado
   
    aceito = analisador.analisar(entrada)

    if aceito:
        print("A cadeia de entrada foi aceita.")
    else:
        print("A cadeia de entrada não foi aceita.")

if __name__ == "__main__":
    main()
