class ListaFunc:
    def __init__(self):
        self.tamanho = 30
        self.list_funcionarios = [None] * self.tamanho
        self.ultima_posicao = -1
        self.qtd = 0

    def get_lista(self):
        return self.list_funcionarios

    # O(n)
    def excluir(self, valor):
        posicao = valor
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.list_funcionarios[i] = self.list_funcionarios[i + 1]
            print('Funcionario foi removido com sucesso!')

            self.ultima_posicao -= 1

    # O(1) - O(2)
    def insere(self, valor):
        if self.ultima_posicao == self.tamanho - 1:
            self.aumentar_listas_funcionario()
        else:
            self.ultima_posicao += 1
            self.qtd += 1
            self.list_funcionarios[self.ultima_posicao] = valor

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(0, self.ultima_posicao + 1):
                print(i, ' - ', self.list_funcionarios[i])

    def aumentar_listas_funcionario(self):
        if self.qtd == self.tamanho:
            self.tamanho += 30
            self.list_funcionarios_aux = [None] * self.tamanho
            for i in range(0, self.tamanho - 30, 1):
                self.list_funcionarios_aux[i] = self.list_funcionarios[i]

            self.list_funcionarios = [None] * self.tamanho

            for i in range(0, self.tamanho - 1, 1):
                self.list_funcionarios[i] = self.list_funcionarios_aux[i]

    def arquivo_func(self):
        lista = self.list_funcionarios
        with open('VisaFuncionario.txt', 'w', encoding="UTF-8") as f:
            for x, valor in enumerate(lista):
                if lista[x] != None:
                    f.write(str(valor))
                    f.write('\n')
