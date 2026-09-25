autorizacao = input("Autorizou receber contato? (sim/nao): ")
telefone_cadastrado = input("Possui telefone cadastrado? (sim/nao): ")

if autorizacao == "sim" and telefone_cadastrado == "sim":
    print("Contato liberado")
else:
    print("Contato não liberado")
