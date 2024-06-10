def remover_contato(contatos):

    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    nome = input("Digite o nome do contato que deseja remover: ")

    for contato in contatos:
        if contato['nome'] == nome:
            contatos.remove(contato)
            print("Contato removido com sucesso!")
            return


    print("Contato não encontrado.")
