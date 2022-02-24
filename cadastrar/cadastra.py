# MODULO DE CADASTRO LOGIN TXT
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso  
# Created Date: Fev-2022
# version ='1.0'
# ---------------------------------------------------------------------------


def inserir_cadastro(usuario,senha):
    import os
    fileName = str('c:\login\login.txt')
    dirName = str('c:\login')
    dirVerifica = os.path.isdir(dirName)
    fileVerifica = os.path.exists(fileName)
    # print(dirVerifica,fileVerifica) <- Debug do if
    while True:
        if os.path.isdir(dirName) and os.path.exists(fileName):
            #print("O diretório existe, e arquivo ok.")
            break
        elif os.path.isdir(dirName) and os.path.exists(fileName) == False:
            with open(fileName,"w"):
                print("Arquivo criado.")
                break
        else:
            print("O diretório não existe!")
            os.mkdir("C:\login")
            with open(fileName,'w'):
                print("Diretorio criado e arquivo criados")
                break
    with open(fileName, "a", encoding="utf-8") as cadastro:
        try:
            cadastro.writelines(f"{usuario},{senha}\n")
            return ("Login cadastrado.\nCaminho c:\login\login.txt")
        except:
            return ("Erro ao cadastrar")


