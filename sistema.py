from estabelecimentos import Estabelecimento
from ListaEstab import ListaEstab
from VISA.lib.arquivo import *
from time import sleep
from visita import Visita
from ListaVisita import ListaVisita
from datetime import datetime

print("\t  \033[32:40mSistema Gerenciador da Visa v1.0\33[m")

arqfuncionario = 'VisaFuncionario.txt'
arqestabelecimento = 'VisaEstabelecimento.txt'
arqvisita = 'VisaVisita.txt'
funcionario = ListaFunc()
estabelecimento = ListaEstab()
visita = ListaVisita()


if not arquivoExiste(arqfuncionario):
    criarArquivo(arqfuncionario)

if not arquivoExiste(arqestabelecimento):
    criarArquivo(arqestabelecimento)

if not arquivoExiste(arqvisita):
    criarArquivo(arqvisita)


def main_func():
    with open(arqfuncionario, 'r', encoding="UTF-8") as arquivo:
        for v in arquivo:
            funcionario.insere(v.replace('\n', ''))


def main_estb():
    with open(arqestabelecimento, 'r', encoding="UTF-8") as arquivo:
        for v in arquivo:
            estabelecimento.cadastrar_estabelecimento(v.replace('\n', ''))


def main_visita():
    with open(arqvisita, 'r', encoding="UTF-8") as arquivo:
        for v in arquivo:
            visita.cadastrar_visita(v.replace('\n', ''))


main_func()
main_estb()
main_visita()


def cadastra_visita():
    razão_social = input('NOME: ')
    cnpj = input('CPF: ')
    dia = input('DIA: ')
    mes = input('MÊS: ')
    ano = input('ANO: ')
    data = datetime(dia, mes, ano)

    nova_visita= Visita(razão_social, cnpj, data)
    visita.cadastrar_visita(nova_visita)


def cadastra_funcionario():
    nome = input('NOME: ')
    cpf = input('CPF: ')
    telefone = input('TELEFONE: ')
    funcao = input('FUNÇÃO: ')

    novo_funcionario = Funcionario(nome, cpf, telefone, funcao)
    funcionario.insere(novo_funcionario)


def cadastra_estabelecimentos():
    razao_social = input('RAZÃO SOCIAL: ')
    CNPJ = leiaInt('CNPJ: ')
    telefone = leiaInt('TELEFONE: ')
    atividade_economica = leiaFloat('CNAE: ')
    data_validade_alvara = leiaInt('DATA DE VALIDADE DO ALVARÁ SANTITÁRIO: ')
    print('SITUAÇÃO DO ESTABELECIMENTO: ')
    situacao = leiaInt('\t[1]: Aguarda cumprimento de ressalvas para Alvará Inicial\n'
                       '\t[2]: Interdição cautelar\n'
                       '\t[3]: Não protocolou situação de renovação de Alvará\n'
                       '\t[4]: Alvará vigente e dentro do prazo para solicitação de renovação \n'
                       '\t[5]: Alvará vencido e estabelecimento não cumpriu ressalvas apontadas no Relatório de '
                       'Inspeção\n '
                       '\t[6]: Atividade não sujeita a concessão de Alvará Sanitário\n'
                       '\t[7]: Alvará vencido, protocolou solicitação de renovação e aguarda inspeção\n'
                       'Escolha uma opção: ')

    novo_estabelecimento = Estabelecimento(razao_social, CNPJ, telefone, atividade_economica, data_validade_alvara,
                                           situacao)
    estabelecimento.cadastrar_estabelecimento(novo_estabelecimento)


while True:
    cabecalho('MENU PRINCIPAL')
    resposta = menu(['Estabelecimentos', 'Funcionario', 'Fechar o Programa'])
    if resposta == 1:
        while True:
            cabecalho('ESTABELECIMENTOS')
            resp1 = menu(['Cadastra novo estabelecimentos', 'Listar estabelecimentos',
                          'Remover Estabelecimento', 'Visita', 'Voltar ao menu anterior'])
            sleep(0.5)

            if resp1 == 1:
                cabecalho('NOVO CADASTRO')
                cadastra_estabelecimentos()

            elif resp1 == 2:
                cabecalho('LISTA DE ESTABELECIMENTOS')
                estabelecimento.listar_estabelecimento()

            elif resp1 == 3:
                estabelecimento.listar_estabelecimento()
                valor = int(input('\nQual estabelecimento você deseja remover? '))
                estabelecimento.excluir(valor)

            elif resp1 == 4:
                while True:
                    resp = menu(['Agendar Visita', 'Listar Visitas', 'Remover Visita', 'Voltar ao menu anterior'])
                    if resp == 1:
                        cadastra_visita()
                    elif resp == 2:
                        visita.listar_visita()
                    elif resp == 3:
                        visita.excluir()
                    elif resp == 4:
                        break
                    else:
                        print('\033[31mERR0! Digite uma opção válida!\033[m')

            elif resp1 == 5:
                break
            else:
                print('\033[31mERR0! Digite uma opção válida!\033[m')
        print()

    elif resposta == 2:
        while True:
            cabecalho('FUNCIONÁRIOS')
            resp2 = menu(['Cadastra novo funcionário', 'Listar funcionários', 'Remover Funcionários',
                          'Voltar ao menu anterior'])
            sleep(0.5)

            if resp2 == 1:
                cabecalho('NOVO CADASTRO')
                cadastra_funcionario()
                print('\033[33mNovo registro foi adicionado.\033[m')

            elif resp2 == 2:
                cabecalho('LISTA DE FUNCIONÁRIOS')
                print("----------NOME-----------CPF-----------TELEFONE-----FUNÇÃO")
                funcionario.imprime()

            elif resp2 == 3:
                funcionario.imprime()
                valor = int(input('\nQual funcionário você deseja remover? '))
                funcionario.excluir(valor)

            elif resp2 == 4:
                break
            else:
                print('\033[31mERR0! Digite uma opção válida!\033[m')
            print()

    elif resposta == 3:
        estabelecimento.arquivo_estab()
        funcionario.arquivo_func()
        visita.arquivo_visita()
        print('Saindo do sistema... Até logo! ')
        break
    else:
        print('\033[31mERR0! Digite uma opção válida!\033[m')
