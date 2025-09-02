import json
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Banco:
  def __init__(self):
    pass

  def cadastro(self, id_conta, senha, nome, saldo=0):
    try:
      with open('dados.json', 'r', encoding='utf-8') as arq:
        cadastro = json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
      cadastro = {}
    cadastro[id_conta] = {"senha": senha, "saldo": saldo, "nome": nome}
    with open('dados.json', 'w', encoding='utf-8') as arq:
      json.dump(cadastro, arq, ensure_ascii=False)

  def login(self, id_conta, senha):
    with open('dados.json', 'r', encoding='utf-8') as arq:
      cadastro = json.load(arq)
    if id_conta in cadastro and cadastro[id_conta]["senha"] == senha:
      print("Login realizado com sucesso!")
      return True 
    else:
      print("\nUsuario nao encontrado.")
  
  def get_saldo(self, id_conta):
    try:
      with open('dados.json', 'r', encoding='utf-8') as arq:
        cadastro = json.load(arq)
        print (f"\nO saldo da conta é de: {cadastro[id_conta]["saldo"]} R$.")
      return cadastro[id_conta]["saldo"]
    except:
      return None
    
  def realizar_deposito(self, id_conta, valor_deposito):
    with open('dados.json', 'r', encoding='utf-8') as arq:
      cadastro = json.load(arq)            
    if valor_deposito > 0:
      cadastro[id_conta]["saldo"] += valor_deposito
      with open('dados.json', 'w', encoding='utf-8') as arq:
        json.dump(cadastro, arq, ensure_ascii=False)
      print(f"Deposito no valor de {valor_deposito} R$ realizado com sucesso.")
      print(f"Saldo atualizado para {cadastro[id_conta]["saldo"]} R$")
    else:
      print("Valor de deposito invalido, tente novamente.")

  def realizar_saque(self, id_conta, valor_saque):
    with open('dados.json', 'r', encoding='utf-8') as arq:
      cadastro = json.load(arq)            
    if valor_saque > 0 and valor_saque < cadastro[id_conta]["saldo"]:
      cadastro[id_conta]["saldo"] -= valor_saque
      with open('dados.json', 'w', encoding='utf-8') as arq:
        json.dump(cadastro, arq, ensure_ascii=False)
      print(f"Saque no valor de {valor_saque} R$ realizado com sucesso.")
      print(f"Saldo atualizado para {cadastro[id_conta]["saldo"]} R$")
    else:
      print("Valor de saque invalido, tente novamente.")



while True:
  print("\nCaixa eletronico on-line:")
  print("1. Cadastro")
  print("2. Log-in")
  print("3. Sair")

  escolha = input("Digite sua escolha: ")

  if escolha == "1":
    usuario = input("Crie um ID para acessar sua conta. (3 numeros.):\n")
    senha = input("Crie uma senha para acessar sua conta. (6 numeros):\n")
    nome = input ("Digite seu nome completo: ")
    banco = Banco()
    banco.cadastro(usuario, senha, nome)
  elif escolha == "2":
    id_usuario = input("\nDigite o ID de sua conta: \n")
    senha = input("\nDigite sua senha: \n")
    banco = Banco()
    if banco.login(id_usuario, senha):
      limpar_tela()
      while True:
        with open('dados.json', 'r', encoding='utf-8') as arq:
          cadastro = json.load(arq)
        print(f"\nBem-vindo, {cadastro[id_usuario]["nome"]}!")
        print("1. Ver saldo")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Limpar tela")
        print("5. Voltar ao menu de Log-in/Cadastro")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
          banco = Banco()
          banco.get_saldo(id_usuario)
        elif escolha == "2":
          valor = int(input("Digite o valor a ser depositado: "))
          banco = Banco()
          banco.realizar_deposito(id_usuario, valor)
        elif escolha == "3":
          valor = int(input("Digite o valor do saque: "))
          banco = Banco()
          banco.realizar_saque(id_usuario, valor)
        elif escolha == "4":
          limpar_tela()
        elif escolha == "5":
          print ("Voltando para o menu principal.")
          break
  elif escolha == "3":
    print ("Programa finalizado.")
    break