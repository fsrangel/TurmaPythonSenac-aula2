def atualizar_contato(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    nome = input("Digite o nome do contato que deseja atualizar: ")
    for contato in contatos:
        if contato['nome'] == nome:
            print(f"Contato encontrado: {contato}")
            contato['telefone'] = input("Digite o novo telefone: ")
            contato['email'] = input("Digite o novo email: ")
            print("Contato atualizado com sucesso!")
            return
    print("Contato não encontrado.")
