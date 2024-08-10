import csv

class TabelaDeAnalise:

    def __init__(self, csv_caminho):
        
        self.tabela = {}
        self.carrega_csv(csv_caminho)

    def carrega_csv(self, csv_caminho):
        
        with open(csv_caminho, "r", encoding='utf-8') as arq_csv:
            
            linhas = csv.reader(arq_csv, delimiter=",")
            cabecalho = next(linhas)
            cabecalho = [x.strip() for x in cabecalho]  # Remove espaços em branco e quebras de linha

            for linha_unica in linhas:
                
                lin_format = [x.strip() for x in linha_unica]
                nao_terminal = lin_format[0]

                if nao_terminal not in self.tabela:
                    
                    self.tabela[nao_terminal] = {}

                for j in range(1, len(lin_format)):
                    
                    if lin_format[j]:  # Se lin_format[j] não for vazio, faça:
                        
                        self.tabela[nao_terminal][cabecalho[j]] = lin_format[j]  # Mapeia a variável com o terminal em questão

    def obtem_producao(self, nao_terminal, terminal):
        
        producao = self.tabela.get(nao_terminal, {}).get(terminal)  # Obtém a regra de produção

        if producao and '->' in producao:

            return producao.split('->')[1].strip()
        
        return producao

    def eh_terminal(self, simbolo):
        
        return simbolo not in self.tabela  # Verifica se o símbolo é terminal
    
    # def __str__(self):
    #    # Retorna uma string representando a tabela
    #    resultado = []
    #    for nao_terminal, producoes in self.tabela.items():
    #       linha = [nao_terminal] + [producoes.get(coluna, '') for coluna in sorted(self.tabela[next(iter(self.tabela))].keys())]
    #        resultado.append(", ".join(linha))
    #    return "\n".join(resultado)
