# MODULO DE CADASTRO LOGIN TXT
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso  
# Created Date: Fev-2022
# version ='1.0'
# ---------------------------------------------------------------------------

def inserir_cadastro(usuario,senha):
    with open("login.txt", "w", encoding="utf-8") as cadastro:
        try:
            cadastro.writelines(f"{usuario},{senha}")
            return ("Login cadastrado.")
        except:
            return ("Erro ao cadastrar")