# MODULO DE MAIN LOGIN TXT
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso  
# Created Date: Fev-2022
# version ='1.0'
# ---------------------------------------------------------------------------
from cadastrar.cadastra import inserir_cadastro
from verifica.verificar import consulta
from logar.login import autenticar

if __name__ == "__main__":
    # GLOBAIS
    print(30*"#")
    print("Digite -> 1 - Cadastrar login.")
    print("Digite -> 2 - Fazer login.")
    print(30*"#")
    escolha = input("Digite sua opção: ")
    if escolha == "1":
        while True: # VERIFICA A DUPLICIDADE DO USUARIO
            nome = input("Digite um usuario para login: ").upper()
            testa = consulta(nome)
            if testa == 1:
                print("Usuario ja cadastrado.\nInsira outro!")
                continue
            else:
                break
        while True: #VERIFICA TAMANHO DA SENHA
            senha = input("Digite sua senha de no maximo 8 caracteres: ")
            if len(senha)<= 8 and len(senha) > 0:
                break
            else:
                print("Senha tem que ter entre 1 e oito caracteres.")
                continue
        print(inserir_cadastro(nome,senha))
    elif escolha == "2":
        while True:
            nome = input("Digite o usuario: ").upper()
            senha = input("Digite sua senha: ")
            print(30*"#")
            print(f"Voce digitou usuario: {nome} e senha: {senha}.")
            vf = input("Tem certeza que deseja continuar: (S/N): ").upper()
            if vf[0] == "S":
                print(autenticar(nome,senha))
                break
            else:
                print("Login cancelado.")
                continue
    else:
        print("Voce não digitou uma opçao valida...")
