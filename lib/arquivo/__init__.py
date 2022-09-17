from VISA.lib.interface import *
from VISA.ListaFunc import ListaFunc
from VISA.funcionarios import Funcionario
funcionario = ListaFunc()


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def cadsfuc(valores):
    with open('VisaFuncionario.txt', 'w') as arquivo:
        for v in valores:
            arquivo.write(str(v) + '-')


def salvar_func(arq):
    lista = funcionario.get_lista()
    temp = []
    for x in range(len(lista)):
        if lista[x] != None:
            temp.append(lista[x])

    with open(arq, 'w', encoding="UTF-8") as f:
        for valor in temp:
            f.write(str(valor))
            f.write('\n')