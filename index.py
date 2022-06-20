
import os


usuario = input("Digite seu usuario --> ")

re = 0

classe = ""
tipo = ""
funcionalidade = ""
preco = ""

#verifica se a conta existe 

with open("contas.txt", "r") as arquivo:

    txt = [data[0:len(data) - 1] for data in arquivo.readlines()]

    contas = {}

    for e in txt:

        dat = e.split("//")
        contas[dat[0]] = dat[1:][0]


for e in contas.keys():

    #existe 

    if usuario == e:

        re = 1

    #nao existe 

    else:

        re = 2


#se existir 

if re == 1:

    print("\nJa existe uma conta com esse usuario\n")

    while True:

        senha = input("Digite sua senha --> ")

        if senha == contas[usuario]:

            print("\nSenha correta\n")

            break

        else:

            print("\nSenha incorreta\n")

            continue
        

    while True:

        res = int(input("Voce quer abrir o ultimo save (digite 1) ou criar um novo (digite 2)? "))

        if res == 1 or res == 2:

            break

        else:

            continue


    if res == 2:

        with open(f"./saves/{usuario}.txt", "w") as arquivo:

            arquivo.write("")



#se nao

else:

    print("\nAinda nao existe uma conta com esse usuario\n")

    senha = input("Crie uma senha --> ")

    with open("contas.txt", "a") as arquivo:

        arquivo.write(f"{usuario}//{senha}\n")


    with open(f"./saves/{usuario}.txt", "w") as arquivo:

        print("Save criado!")



print("\nSave carregado!\n")

os.system("clear")

#criacao das funcoes para a mochila

def adicionar():

    global classe
    global tipo
    global funcionalidade
    global preco

    classe = input("\nDigite o classe do item (Ataque, Cura ou Itens gerais)--> ")
    tipo = input("Digite a tipo do item --> ")
    funcionalidade = input("Digite a funcionalidade do item --> ")
    preco = input("Digite o preco do item --> ")

    with open(f"./saves/{usuario}.txt", "a") as arquivo:

        arquivo.write(f"{classe}//{tipo}//{funcionalidade}//{preco}\n")


    with open(f"./saves/{usuario}.txt", "r") as arquivo:

        txt1 = [data[0:(len(data)-1)] for data in arquivo.readlines()]

        itensArray = []

        for e in txt1:

            dt = e.split("//")
            itensArray.append(list(dt[0:]))


    print("\nItem adicionado!\n")
    print("-="*30)


def editar():

    classeP = input("\nDigite a classe do item que quer editar --> ")
    tipoP = input("Digite o tipo do item que quer editar --> ")

    r = 0

    with open(f"./saves/{usuario}.txt", "r") as arquivo:

        txt2 = [data[0:(len(data)-1)] for data in arquivo.readlines()]
        array = []

        for e in txt2:

            dt = e.split("//")
            array.append(list(dt[0:]))

        for i,e in enumerate(array):

            if array[i][0] == classeP.lower() and array[i][1] == tipoP:

                print(f"\nClasse atual do item: {array[i][0]}\nTipo atual do item: {array[i][1]}\nFuncionalidade atual do item: {array[i][2]}\nPreco atual do item: $ {array[i][3]}")

                novaC = input("\nDigite a nova classe desse item --> ")
                novoT = input("Digite o novo tipo desse item --> ")
                novaF = input("Digite a nova funcionalidade desse item --> ")
                novoP = input("Digite o novo preco desse item --> ")

                array[i][0] = novaC
                array[i][1] = novoT
                array[i][2] = novaF
                array[i][3] = novoP

                with open(f"./saves/{usuario}.txt", "w") as arquivo:

                    for i,e in enumerate(array):

                        arquivo.write(f"{array[i][0]}//{array[i][1]}//{array[i][2]}//{array[i][3]}\n")

                print("\nItem editado!\n")

                break
            
            else:

                r = 2
        
        if r == 2:

            print("\nItem nao existe")


    print("-="*30)


def exluir():

    classeP = input("\nDigite a classe do item que quer excluir --> ")
    tipoP = input("Digite o tipo do item que quer excluir --> ")

    re = 0

    with open(f"./saves/{usuario}.txt", "r") as arquivo:

        txt2 = [data[0:(len(data)-1)] for data in arquivo.readlines()]
        array = []

        for e in txt2:

            dt = e.split("//")
            array.append(list(dt[0:]))

        for i,e in enumerate(array):

            if array[i][0] == classeP.lower() and array[i][1] == tipoP:

                array.pop(i)

                print("\nItem exluido!\n")

                break

            else:

                re = 2

        if re == 2:

             print("\nO item pesquisado nao existe")


        with open(f"./saves/{usuario}.txt", "w") as arquivo:

            for i,e in enumerate(array):

                arquivo.write(f"{array[i][0]}//{array[i][1]}//{array[i][2]}//{array[i][3]}\n")      

    print("-="*30)  


def visualizar():

    with open(f"./saves/{usuario}.txt", "r") as arquivo:

        txt2 = [data[0:(len(data)-1)] for data in arquivo.readlines()]
        array = []

        for e in txt2:

            dt = e.split("//")
            array.append(list(dt[0:]))

        print("\nSua mochila: ")

        for i,e in enumerate(array):

            print(f"\nClasse do item: {array[i][0]}\nTipo do item: {array[i][1]}\nFuncionalidade do item: {array[i][2]}\nPreco do item: $ {array[i][3]}")

            print("-"*15)

    print("-="*30)


def pesquisar():

    classeP = input("\nDigite a classe do item que quer pesquisar --> ")
    tipoP = input("Digite o tipo do item que quer pesquisar --> ")

    re = 0

    with open(f"./saves/{usuario}.txt", "r") as arquivo:

        txt2 = [data[0:(len(data)-1)] for data in arquivo.readlines()]
        array = []

        for e in txt2:

            dt = e.split("//")
            array.append(list(dt[0:]))

        for i,e in enumerate(array):

            if array[i][0] == classeP.lower() and array[i][1] == tipoP:

                print(f"\nClasse do item: {array[i][0]}\nTipo do item: {array[i][1]}\nFuncionalidade do item: {array[i][2]}\nPreco do item: $ {array[i][3]}")
                
                break

            else:

                re = 2

        if re == 2:

            print("\nO item pesquisado nao existe")

    print("-="*30)

while True:

    resp = int(input("\nO que deseja fazer na sua mochila?\n\n Adicionar itens (digite 1)\n Editar itens (Digite 2)\n Excluir itens (Digite 3)\n Visualizar (Digite 4)\n Pesquisar (Digite 5)\n ou sair (Digite 6)\n --> "))

    if resp == 1:

        adicionar()

        continue

    elif resp == 2:

        editar()

        continue

    elif resp == 3:

        exluir()

        continue

    elif resp == 4:

        visualizar()

        continue

    elif resp == 5:

        pesquisar()

        continue

    elif resp == 6:

        break

    else:

        print("\nEscolha um numero valido\n")

        continue