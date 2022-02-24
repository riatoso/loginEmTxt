# MODULO VERIFICAR LOGIN TXT
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso  
# Created Date: Fev-2022
# version ='1.0'
# ---------------------------------------------------------------------------

def consulta(nome_aut):
    local = str("c:\login\login.txt")
    encontrados = 0
    with open(local, "r", encoding="utf-8") as verificado:
        for name in verificado.readlines():
            i = name.strip().split(",")
            name = (i[0])
            if name == nome_aut:
                encontrados = 1
                break
            else:
                continue
    return encontrados