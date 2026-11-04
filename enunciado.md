# Lista de Exercícios — Dicionários (enunciado)

Transcrição textual do material **aula_dicionarios.pdf** fornecido para a atividade.

## Lista de exercícios

1. Crie um dicionário chamado `aluno` com as chaves `"nome"`, `"idade"` e `"curso"`. Em seguida, exiba apenas o nome do aluno.
2. Adicione uma nova chave `"nota"` com valor 9.5 ao dicionário `aluno`. Depois, remova a chave `"idade"`.
3. Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço:

   ```python
   produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}
   ```

4. Dado o dicionário `aluno`, verifique se existe a chave `"curso"`.
5. Crie um dicionário chamado `turma` que contenha dois alunos, cada um com nome e nota. Depois, exiba o nome do primeiro aluno e a nota do segundo aluno.
6. Crie um dicionário representando um carro com as chaves: `marca`, `modelo` e `ano`.
   - a. Adicione ao dicionário do carro a chave `'cor'`.
   - b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como valor).
   - c. Acesse a nota de um dos alunos e exiba.
   - d. Remova um aluno do dicionário de notas.

## Estudo de Caso: Cadastro de Produtos

Um supermercado deseja armazenar informações sobre seus produtos. Cada produto deve conter: nome, preço e quantidade em estoque. Utilize um dicionário para representar e manipular essas informações.

Exemplo conceitual do enunciado:

```python
produto = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
```

## Estudo de Caso 2: Agenda Telefônica

Uma agenda pode ser representada como um dicionário em que as chaves são os nomes das pessoas e os valores são os números de telefone.

```python
agenda = {"Maria": "99999-1234", "João": "98888-5678"}
print("Telefone da Maria:", agenda["Maria"])
```

> **Importante:** os estudos de caso constam no enunciado, mas ainda não fazem parte da implementação em `aluno.py`.
