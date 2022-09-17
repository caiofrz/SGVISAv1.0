class ListaVisita:
    def __init__(self):
        self.tamanho = 30
        self.list_visitas = [None] * self.tamanho
        self.qtd = 0

    def cadastrar_visita(self, visita):
        self.list_visitas[self.qtd] = visita
        self.qtd += 1

        self.aumentar_listas_visita()

    def listar_visita(self):
        if self.qtd == 0:
            print('O vetor está vazio')
        else:
            for i in range(0, self.qtd + 1):
                print(i, ' - ', self.list_visitas[i])

    def excluir(self, valor):
        posicao = valor
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.qtd):
                self.list_visitas[i] = self.list_visitas[i + 1]
            print('Estabelecimento foi removido com sucesso!')

            self.qtd -= 1

    def aumentar_listas_visita(self):
        if self.qtd == self.tamanho:
            self.tamanho += 30
            self.list_visitas_aux = [None] * self.tamanho
            for i in range(0, self.tamanho - 30, 1):
                self.list_visitas_aux[i] = self.list_visitas[i]

            self.list_visitas = [None] * self.tamanho

            for i in range(0, self.tamanho - 1, 1):
                self.list_visitas[i] = self.list_visistas_aux[i]

    def arquivo_visita(self):
        lista = self.list_visitas
        with open('VisaVisita.txt', 'w', encoding="UTF-8") as f:
            for x, valor in enumerate(lista):
                if lista[x] != None:
                    f.write(str(valor))
                    f.write('\n')
