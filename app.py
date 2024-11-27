from time import sleep
import platform
import os
import pandas as pd

# Variáveis Globais

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
tabela_preco = { # Tipos de Combustivel | Preço/Litro
    'gasolina': 6.60,
    'gasolina aditivada': 6.77,
    'oleo': 6.59
}
combustivel_venda = {}


def calc_combustivel(tipo, qntd):
    preco_comb = tabela_preco[tipo]
    preco_total = qntd * preco_comb
    
    return round(preco_total, 2)

# Retorna a diferença de combustíveis de manhã pra noite
def negative(Num1, Num2):
    if Num1 < Num2:
        a = float(f"{Num2 - Num1}")
    else:
        a = float(f'{Num1 - Num2}')
    return a

# Retorna o valor trocando a vírgula por ponto
def ponto(a):
    b = ',' in a
    if b:
        c = a.replace(",", ".")
    else:
        return float(a)
    return float(c)

# Faz a diferença de combustíveis enviado
def diff(combustivel: str):
    print(combustivel.title())
    
    nume1 = ponto(input("Qntd. de combustível (manhã): "))
    nume2 = ponto(input("Qntd. de combustível (noite): "))
    litros = round(negative(nume1, nume2), 3)
    return litros

def mostrar_info(infos: dict):
    print(f"Litros: ", RED + f"{infos['Litros-Totais']}" + RESET, "| Reais: ", GREEN + f"{infos['Valor-Total']}" + RESET)
    print("=" * 46)

def salvar_info(nome_combustivel:str, tipo:str):

    # Nome, Total de Litros, Valor Total, Tipo
    nome = nome_combustivel.title()
    total_litros = diff(nome)
    valor_total = calc_combustivel(tipo, total_litros)
    comb_tipo = tipo


    info = {"Nome": nome, "Litros-Totais": total_litros, "Valor-Total": valor_total, "Tipo-Tabela": comb_tipo}

    combustivel_venda[nome] = info

    return combustivel_venda[nome]

def resto():
    for combustivel in combustivel_venda.values():
        combustivel["Resto"] = ponto(input(f"Sobra de {combustivel['Nome'].lower()} do dia anterior: "))


def mostrar_relatorio():
    resto()
    tabela = [["Nome", "Resto", "Litros Totais (Do dia)", "Resto - Litros Totais"]]
    litros_total = 0
    valor_total = 0
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


    print("=" * 46)
    print(f'{"Bombas de Combustível":>35}')
    print("")
    for combustivel in combustivel_venda.values():
        litros_total += combustivel['Litros-Totais']
        valor_total += combustivel['Valor-Total']

        print(f"{combustivel['Nome']}:", RED + f"{combustivel['Litros-Totais']:<5}" + RESET, "->", GREEN + f"{combustivel['Valor-Total']}" + RESET)
    valor_total = round(valor_total, 3)
    litros_total = round(litros_total, 3)
    print("")
    print(f"Total Reais :", GREEN + f"{valor_total}" + RESET)
    print(f"Diversos :", GREEN + f"{diversos}" + RESET)
    print(f"Total Reais + Diversos :", GREEN + f"{round(valor_total + diversos, 2)}" + RESET)
    print("")
    print("=" * 46)

    if platform.system() == "Windows":
        os.system("pause")
        os.system("cls")
    else:
        os.system("/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
        os.system("clear")
    print("Calculando...")
    sleep(5)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print("=" * 46)
    print("")    
    print(f'{"Combustível usado":>35}')
    for combustivel in combustivel_venda.values():
        tabela.append([
            combustivel["Nome"],
            combustivel["Resto"],
            combustivel["Litros-Totais"],
            combustivel["Litros-Totais"] - combustivel["Resto"],
        ])

    tabela = pd.DataFrame(tabela)
    print(tabela)
###############################################################################

print("=" * 46)
print(f'{"CAIXA":>25}')
print("=" * 46)
print("")



mostrar_info(salvar_info("Gasolina", 'gasolina'))
mostrar_info(salvar_info("Gasolina2", 'gasolina'))
mostrar_info(salvar_info("Gasolina3", 'gasolina'))
mostrar_info(salvar_info("Gasolina Aditivada", 'gasolina aditivada'))
mostrar_info(salvar_info("Óleo Comum & S-10", 'oleo'))
mostrar_info(salvar_info("S-10", 'oleo'))
mostrar_info(salvar_info("S-500", 'oleo'))

diversos = ponto(input("Valores à parte: "))

print("=" * 46)

mostrar_relatorio()

while True:
    comando = input("Digite 'sair' para encerrar o programa: ")
    if comando.lower() == 'sair':
        break