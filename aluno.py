# questão1
aluno = {
    "nome":  "Fernando",
    "idade": "41",
    "curso": "Engenharia de Software"
}

print("1 - Nome:", aluno["nome"])

# questão 2

aluno["nota"] = 9.5
del aluno["idade"]
print("2 - Aluno:", aluno)

# questão 3

produtos = {
    "Arroz": 15.90,
    "Feijao": 9.50,
    "Macarrão": 4.20
}
print("3 - produtos")
for nome, preco in produtos.items():
    print(nome, "- R$", f"{preco:.2f}")

# questão 4

if "curso" in aluno:
    print("4 - A chave curso existe.")
else:
    print("4 - A chave curso não existe.")

# questão 5


turma = {
    "alunos": [
        {"nome": "lula", "nota": "1,0"},
        {"nome": "lala", "nota": "3.0"}
    ]
}

print("5 - Primeiro aluno: ", turma["alunos"][0]["nome"])
print("5 - Segundo aluno nota:", turma["alunos"][1]["nota"])

# questao 6 

carro = {
    "marca": "Fiat",
    "modelo": "Pulse",
    "ano": "2027"
}
carro ["cor"] = "preto"
print("6 - carro:" , carro)

# questão 6b

notas = {
    "Aninha": 9.0,
    "Pedro": 5.0,
    "Lucas": 8.0

}
print("6b - Notas:")
for nome, nota in notas.items():
    print(nome, ".", nota)

# questao 6c
print("6c - Nota de Pedro:", notas["Pedro"])

# questao 6d

del notas["Lucas"]
print("6d - Apos remover Lucas:",notas)
