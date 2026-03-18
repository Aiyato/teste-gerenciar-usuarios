import json
import random
with open('usuarios.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(len(dados))
print(f"usuarios: {len(dados)}")
ativos = 0 
inativos = 0
for usuario in dados:
    if usuario['ativo'] == True:
        ativos += 1
    else:
        inativos += 1
print(f"ativos: {ativos}")
print(f"inativos: {inativos}")

nome_usuario = input("Digite o nome do usuário: ")
for usuario in dados:
    if usuario['nome'].lower().strip().replace(" ", "") == nome_usuario.lower().strip().replace(" ", ""):
        print(f"Usuário encontrado: {usuario}")
        break
else:
    print("Usuário não encontrado.")

resposta = input("Deseja adicionar um novo usuário? (sim/nao): ").lower().strip()
if resposta == 'sim':

    nome = input("Digite o nome do novo usuário: ")
    email = input("Digite o email do novo usuário: ")
    id_aleatorio = random.randint(1001, 9999)
    ids_existentes = [u['id'] for u in dados]
    while True:
        id_aleatorio = random.randint(1001, 9999)
        if id_aleatorio not in ids_existentes:
            break
    novo_usuario = {
        "id": id_aleatorio,
        "nome": nome,
        "email": email,
        "ativo":random.choice([True, False])
    }
    dados.append(novo_usuario)
    with open('usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print(f"Novo usuário adicionado: {novo_usuario}")
elif resposta == 'nao':
    print("encerrando o programa.")
else:
    print("Resposta inválida. Encerrando o programa.")
    exit()

    



