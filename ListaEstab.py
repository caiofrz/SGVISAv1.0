
class ListaEstab:
    def __init__(self):
        self.tamanho = 30
        self.list_estabelecimentos = [None] * self.tamanho
        self.qtd = 0

    def cadastrar_estabelecimento(self, estabelecimento):
        self.list_estabelecimentos[self.qtd] = estabelecimento
        self.qtd += 1

        self.aumentar_listas_estabelecimento()

    def excluir(self, valor):
        posicao = valor
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.qtd):
                self.list_estabelecimentos[i] = self.list_estabelecimentos[i + 1]
            print('Estabelecimento foi removido com sucesso!')

            self.qtd -= 1

    def listar_estabelecimento(self):
        if self.qtd == 0:
            print('NÃO POSSUI NENHUM CADASTRO')
        else:
            for i in range(0, self.qtd, 1):
                print(i, "-", self.list_estabelecimentos[i])

    def aumentar_listas_estabelecimento(self):
        if self.qtd == self.tamanho:
            self.tamanho += 30
            self.list_estabelecimentos_aux = [None] * self.tamanho
            for i in range(0, self.tamanho - 30, 1):
                self.list_estabelecimentos_aux[i] = self.list_estabelecimentos[i]

            self.list_estabelecimentos = [None] * self.tamanho

            for i in range(0, self.tamanho - 1, 1):
                self.list_estabelecimentos[i] = self.list_estabelecimentos_aux[i]

    def arquivo_estab(self):
        lista = self.list_estabelecimentos
        with open('VisaFuncionario.txt', 'w', encoding="UTF-8") as f:
            for x, valor in enumerate(lista):
                if lista[x] != None:
                    f.write(str(valor))
                    f.write('\n')
