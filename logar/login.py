# MODULO DE AUTENTICACAO LOGIN TXT
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso  
# Created Date: Fev-2022
# version ='1.0'
# ---------------------------------------------------------------------------

def autenticar(nome,senha):
    local = str("c:\login\login.txt")
    lista_login = []
    autenticado = "EERO DE LOGIN"
    with open(local, "r", encoding="utf-8") as recorte_linhas:
        for linha in recorte_linhas:
            lista = (linha.strip().split(","))
            lista_login.append(lista)
        for nova_linha in lista_login:
            if nova_linha[0] == nome and nova_linha[1] == senha:
                autenticado = "AUTENTICADO COM SUCESSO"
            else:
                continue
    return autenticado