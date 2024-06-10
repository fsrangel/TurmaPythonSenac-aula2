def visualizar_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        for idx, contato in enumerate(contatos, start=1):
            print(f"Contato {idx}:")
            print(f"  Nome: {contato['nome']}")
            print(f"  Telefone: {contato['telefone']}")
            print(f"  Email: {contato['email']}")
