#Exercício 1 – Custo de Licenças
nome_sistema = input("Digite o nome do sistema: ")
lic1 = float(input("Digite o valor da licença 1: "))
lic2 = float(input("Digite o valor da licença 2: "))
total = lic1 + lic2
print("Sistema:", nome_sistema)
print("Custo total: R$", total)


#Exercício 3 – Média de Chamados
equipe = input("Digite o nome da equipe: ")
c1 = int(input("Digite a quantidade de chamados do dia 1: "))
c2 = int(input("Digite a quantidade de chamados do dia 2: "))
media = (c1 + c2) / 2
print("Equipe:", equipe)
print("Média diária de chamados:", media)

# Exemplo 10 – Crescimento de Usuários de uma Plataforma
# Entrada de dados
usuarios_iniciais = int(input("Digite o número inicial de usuários: "))
meses = int(input("Digite a quantidade de meses: "))
# Processamento
usuarios_finais = usuarios_iniciais * (2 ** meses)
# Saída
print("Total de usuários após", meses, "meses:", usuarios_finais)

# Exemplo 9 – Distribuição de Processamento em Servidores
# Entrada de dados
total_registros = int(input("Digite a quantidade total de registros: "))
quantidade_servidores = int(input("Digite a quantidade de servidores disponíveis: "))
# Processamento
registros_por_servidor = total_registros / quantidade_servidores
# Saída
print("Cada servidor deverá processar", registros_por_servidor, "registros.")
