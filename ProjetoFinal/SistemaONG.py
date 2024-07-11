import time
from datetime import date 
from fuzzywuzzy import process

today = date.today()

hoje = today.strftime("%d/%m/%Y")

doadores = []
pets = []
contPets = 0
contDoador = 0


usuarios = [
    {'username': 'batatinha', 'password': '123'},
]

def login():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    
    for user in usuarios:
        if user['username'] == username and user['password'] == password:
            print("Login bem-sucedido!")
            print()
            return True
    print("Nome de usuário ou senha incorretos.")
    return False


def verListas():
    print(doadores)
    print()
    print(pets)
    print()


def excluirDoador():
    print("Se não souber o id do Doador digite 0 or 'N' ")
    idDoador = input("Digite o id do doador: ").upper()
    for doador in doadores:
        if doador['Id'] == int(idDoador):
            escolha = input("Você realmente deseja excluir este doador?(S/N): ").upper()
            if escolha == "S":
                doadores.remove(doador)
                print("Doador excluido com sucesso!")
                time.sleep(1)
                print(50 * "-")
                return
            elif escolha == "N":
                menu()
                time.sleep(1)
                print(50 * "-")

    print("Doador não encontrado.")
    time.sleep(1)
    print(50 * "-")
    if int(idDoador) == 0 or idDoador == "N":
        verId()



def excluirAnimal():
    print("Se não souber o id do animal digite 0 or 'N' ")
    idAnimal = input("Digite o id do animal: ").upper()
    for animal in pets:
        if animal['Id'] == int(idAnimal):
            escolha = input("Você realmente deseja excluir este animal?(S/N): ").upper()
            if escolha == "S":
                pets.remove(animal)
                print("Animal excluido com sucesso!")
                time.sleep(1)
                print(50 * "-")
                return
            elif escolha == "N":
                menu()
                time.sleep(1)
                print(50 * "-")

    print("Animal não encontrado.")
    time.sleep(1)
    print(50 * "-")
    if int(idAnimal) == 0 or idAnimal == "N":
        verIdAnimal()



#Excluir
def Excluir():
    while True:
        print("1. Excluir Animal")
        print("2. Excluir Doador")
        print("3. Sair")

        op = input("Digite a opção desejada? ")
        if op == "1":
            excluirAnimal()
        elif op == "2":
           excluirDoador()
        else:
            break



#Editar Doador
def editarDoador():
     print(50*"_")
     print("Se não souber o id do doador digite 0 or 'N' ")
     idDoador = input("Digite o id do doador: ").upper()
     for doador in doadores:
        if doador['Id'] == int(idDoador):
            print("Deixe o campo em branco para não alterar o valor atual.")
            nome = input(f"Digite o Nome do Doador ({doador['Nome']}): ").title() or doador['Nome']
            endereco = input(f"Digite o Endereço do Doador ({doador['Endereco']}): ") or doador['Endereco']
            telefone = input(f"Digite o Telefone do Doador ({doador['Telofone']}): ")
            telefone = int(telefone) if telefone else doador['Telofone']
            email = input(f"Digite o Email do Doador ({doador['Email']}): ") or doador['Email']

            doador.update({
                "Nome": nome,
                "Endereco": endereco,
                "Telofone": telefone,
                "Email": email,
            })
            print("Doador atualizado com sucesso!")
            time.sleep(1)
            print(50 * "-")
            return

     print("Doador não encontrado.")
     time.sleep(1)
     print(50 * "-")
     if int(idDoador) == 0 or idDoador == "N":
        verIdAnimal()
    


#Editar animais
def editarAnimal():
    print("Se não souber o id do animal digite 0 or 'N' ")
    idAnimal = input("Digite o id do animal: ").upper()
    for animal in pets:
        if animal['Id'] == int(idAnimal):
            print("Deixe o campo em branco para não alterar o valor atual.")
            nome = input(f"Digite o Nome do Animal ({animal['Nome']}): ").title() or animal['Nome']
            especie = input(f"Digite a Espécie do Animal ({animal['Especie']}): ") or animal['Especie']
            raca = input(f"Digite a Raça do Animal ({animal['Raca']}): ") or animal['Raca']
            dataNasc = input(f"Digite a Data de Nascimento do Pet ({animal['DataNasc']}): ") or animal['DataNasc']
            peso = input(f"Digite o Peso do Pet ({animal['Peso']}): ")
            peso = float(peso) if peso else animal['Peso']
            sexo = input(f"O Animal é (M - macho; F - Fêmea) ({animal['Sexo']}): ").lower() or animal['Sexo']
            doador = input(f"Qual o Id do Doador? ({animal['Doador']}): ")
            doador = int(doador) if doador else animal['Doador']
            vacina = input(f"Como está a vacinação do Animal ({animal['Vacinacao']}): ") or animal['Vacinacao']
            dtaDoacao = input(f"Digite a Data que o animal foi doado ({animal['DtaDoacao']}): ") or animal['DtaDoacao']

            animal.update({
                "Nome": nome,
                "Especie": especie,
                "Raca": raca,
                "DataNasc": dataNasc,
                "Peso": peso,
                "Sexo": sexo,
                "Doador": doador,
                "Vacinacao": vacina,
                "DtaDoacao": dtaDoacao
            })
            print("Animal atualizado com sucesso!")
            time.sleep(1)
            print(50 * "-")
            return

    print("Animal não encontrado.")
    time.sleep(1)
    print(50 * "-")
    if int(idAnimal) == 0 or idAnimal == "N":
        verIdAnimal()


# | Funcao da Edição
def Edicao():
    while True:
        print("1. Editar Animal")
        print("2. Editar Doador")
        print("3. Sair")

        op = input("Digite a opção desejada? ")
        if op == "1":
            editarAnimal()
        elif op == "2":
            editarDoador()
        else:
            break


def verIdAnimal():
    nome = input("Digite o nome do Animal: ").title()
    nomes = [animal['Nome'] for animal in pets]
    melhores_correspondencias = process.extract(nome, nomes, limit=5)
    
    encontrados = []
    for correspondencia in melhores_correspondencias:
        nome_correspondente = correspondencia[0]
        for animal in pets:
            if animal['Nome'] == nome_correspondente:
                encontrados.append(animal)
    
    if encontrados:
        for animal in encontrados:
            print(f"{animal['Nome']} o id é -> {animal['Id']}")
    else:
        print("Nenhum doador encontrado com um nome semelhante.")


def verId():
    nome = input("Digite o nome do doador: ").title()
    nomes = [doador['Nome'] for doador in doadores]
    melhores_correspondencias = process.extract(nome, nomes, limit=5)
    
    encontrados = []
    for correspondencia in melhores_correspondencias:
        nome_correspondente = correspondencia[0]
        for doador in doadores:
            if doador['Nome'] == nome_correspondente:
                encontrados.append(doador)
    
    if encontrados:
        for doador in encontrados:
            print(f"{doador['Nome']} o id é -> {doador['Id']}")
    else:
        print("Nenhum doador encontrado com um nome semelhante.")

def buscarAnimal():
    while True:
       print("1. Para buscar pelo id do doador")
       print("2. Ver Id")
       print("3. Para buscar pela data de doacao dos animais")
       print("4. Para Sair")
       
       encontrado = False

       op = input("Digite a opção desejada: ")
       if op == "1":
        buscId = int(input("Qual o id do doador? "))
        for i in doadores:
           if i['Id'] == buscId:
               print(f"{i['Nome']} doou estes animais -")
               for j in pets:
                   if j['Doador'] == buscId:
                       print(f"Nome do Animal - {j['Nome']}, Id do Doador - {j['Doador']}")
                       encontrado = True
       elif op == "2":
           verId()
           encontrado = True
       elif op == "3":
        buscDta = input("Digite a data das doação voce quer buscar: ")
        for j in pets:
            if j['DtaDoacao'] == buscDta:
             print(f"Nome do Animal - {j['Nome']}, Id do Doador - {j['Doador']}")
             encontrado = True
       if op == "4":
            break
       if not encontrado:
           print("Doador não encontrado")

        
def cadastroPets():
    global contPets
    nome = input("Digite o Nome do Animal: ").title()
    especie = input("Digite a Espécie do Animal: ")
    raca = input("Digite a Raça do Animal: ")
    dataNasc = input("Digite a Data de Nascimento do Pet: ")
    peso = float(input("Digite o Peso do Pet: "))
    sexo = input("O Animal é (M - macho; F - Fêmea): ").lower()
    doador = int(input("Qual o Id do Doador?:(Se nao tiver id coloque 0) "))
    vacina = input("Como esta a vacinação do Animal? ")
    print(f"Data que o animal foi doado: {hoje} ")


    pet = {
        "Id": int(contPets+ 1),
        "Nome": nome,
        "Especie": especie,
        "Raca": raca,
        "DataNasc": dataNasc,
        "Peso": peso,
        "Sexo": sexo,
        "Doador": doador,
        "Vacinacao": vacina,
        "DtaDoacao": hoje
    }
    pets.append(pet)
    contPets +=1
    print("Pet Cadastrado com Sucesso!")
    time.sleep(1.3)
    print(50*"-")

def listarPets():
    while True:
        if pets != []:
            for pet in pets:
                print(f"Id: {pet['Id']}, Nome do Animal: {pet['Nome']}, Especie: {pet['Especie']}, Raça: {pet['Raca']}, Data de Nascimento: {pet['DataNasc']}, Peso: {pet['Peso']}, Sexo: {pet['Sexo']}, Foi doado no dia: {pet['DtaDoacao']} ")
        else:
            print("Nenhum Pet cadastrado")
        opcaoPet = input("Deseja voltar para o menu? S -> Sim ").upper()
        if opcaoPet == "S" or opcaoPet == "SIM":
            break

def cadastroDoadores():
   global contDoador
   nome = input("Digite o nome do Doador: ").title()
   endereco = input("Digite o Endereço do Doador: ")
   telefone = int(input("Digite o Telefone do Doador: "))
   email = input("Digite o Email do Doador: ")

   doador = {
       "Id": int(contDoador +1),
      "Nome": nome,
      "Endereco": endereco,
      "Telofone": telefone,
      "Email": email,
   }
   doadores.append(doador)
   contDoador += 1
   print("Doador Cadastrado com Sucesso!")
   time.sleep(1)
   print(50*"-")

def listarDoadores():
    while True:
        if doadores:
            for cliente in doadores:
                 print(f"Id: {cliente['Id']}, Nome: {cliente['Nome']}, Endereço: {cliente['Endereco']}, Telefone: {cliente['Telofone']}, Email: {cliente['Email']}    ")
        if not doadores:
            print("Nenhum doador adicionado")
        opcaoLista = input("Deseja voltar ao menu? S -> Sim ").upper()
        if opcaoLista == "S" or opcaoLista == "SIM":
            break


def menu():
    while True:
        print("SISTEMA PARA GERENCIAR ADOÇÃO DE ANIMAIS DE ONG's")
        print("1. Cadastrar Doador")
        print("2. Cadastrar Animal")
        print("3. Listar Doadores")
        print("4. Listar Animais")
        print("5. Buscar animais pelo Doador")
        print("6. Edições -> Animais e Doadores")
        print("7. Exclusões -> Animais e Doadores")
        print("8. Sair")

        opcao = input("Digite o numero da opção que deseja: ")

        print()

        if opcao == "1":
          cadastroDoadores()
        if opcao == "2":
           cadastroPets()
        if opcao == "3":
           listarDoadores()
        if opcao == "4":
           listarPets()
        if opcao == "5":
           buscarAnimal()
        if opcao == "6":
           Edicao()
        if opcao == "7":
           pass
           Excluir()
        if opcao == "8":
           print("Fechando o Sistema...")
           break
        if opcao == "123":
           verListas()
if login():
    menu()
else:
    print("Acesso negado.")