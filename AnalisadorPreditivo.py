from collections import deque
from typing import List

class AnalisadorPreditivo:

    def __init__(self, tabela_analise):
        self.tabela_analise = tabela_analise
        self.stack = deque()
        print(f"Pilha inicializada: {self.stack}")

    def analisar(self, entrada: str) -> bool:
        self.stack.clear()  # Limpa a pilha
        self.stack.append("$")  # Insere $ no fundo da pilha
        self.stack.append("S")  # Insere S acima do elemento no fundo da pilha

        tokens_entrada = entrada.split()
        tokens_entrada.append("$")  # Insere $ no final da fita para saber quando houve casamento

        cabeca_leitura = 0  # Armazena a posição da cabeça de leitura na fita

        while self.stack:  # O laço é percorrido enquanto houverem elementos na pilha
            topo = self.stack[-1]  # topo é a variável que se encontra no topo da pilha
            token_atual = tokens_entrada[cabeca_leitura]  # token_atual é o primeiro elemento da fita

            # Verifica se a pilha contém apenas o símbolo $ e se o símbolo atual é $
            if len(self.stack) == 1 and self.stack[0] == "$" and token_atual == "$":
                return True

            if self.tabela_analise.eh_terminal(topo):
                if topo == token_atual:
                    self.stack.pop()
                    cabeca_leitura += 1
                else:
                    print(f"Erro: Esperado '{topo}', mas encontrado '{token_atual}'")
                    return False
            else:
                producao = self.tabela_analise.obtem_producao(topo, token_atual)

                if producao is not None:
                    self.stack.pop()  # Desempilha o símbolo no topo da pilha
                    simbolos = producao.split()  # Divide o corpo da produção em símbolos
                    for simbolo in reversed(simbolos):
                        if simbolo != "ε":
                            self.stack.append(simbolo)  # Adiciona os símbolos na pilha
                else:
                    print(f"Erro: Nenhuma produção encontrada para '{topo}' com entrada '{token_atual}'")
                    return False

        # Se a pilha contém apenas o símbolo $ e a fita está no final, aceita a entrada
        if self.stack == deque(["$"]) and tokens_entrada[cabeca_leitura] == "$":
            return True
        else:
            print("Erro: Cadeia de entrada não aceita.")
            return False
