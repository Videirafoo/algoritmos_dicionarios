# Algoritmos — Dicionários em Python

**Trabalho acadêmico:** Lista de Exercícios — Dicionários  
**Aluno:** Fernando Otávio Videira Junior  
**Instituição:** Universidade de Vassouras — Campus Saquarema  
**Curso:** Engenharia de Software, 2º período  
**Disciplina:** Algoritmos em Python

## Objetivo

Praticar criação, consulta, inserção, remoção e iteração em dicionários (`dict`) com exemplos de alunos, produtos, turmas, carros e notas.

## Exercícios implementados

O arquivo [`aluno.py`](./aluno.py) contém as soluções das **questões 1 a 6**, incluindo os itens 6a–6d.

| Questão | Implementação |
| --- | --- |
| 1 | Cria `aluno` e exibe seu nome. |
| 2 | Acrescenta a nota 9.5 e remove a chave `idade`. |
| 3 | Lista produtos e preços usando `.items()`. |
| 4 | Verifica se existe a chave `curso`. |
| 5 | Consulta dois alunos armazenados na turma. |
| 6 | Cria o dicionário `carro`, adiciona `cor` e manipula notas de três alunos. |

O [enunciado da lista](./enunciado.md) também apresenta os estudos de caso **Cadastro de Produtos** e **Agenda Telefônica**. Esses estudos adicionais **não estão implementados** no arquivo `aluno.py` enviado.

## Como executar no VS Code

1. Instale o **Python 3**.
2. Abra o repositório no VS Code.
3. Acesse **Terminal → Novo Terminal**.
4. Execute:

```bash
python aluno.py
```

No Windows, caso o comando `python` não funcione, use:

```powershell
py aluno.py
```

O programa usa somente a biblioteca padrão do Python, não necessita de instalação de dependências e imprime os resultados no terminal.

## Arquivos do repositório

- [`aluno.py`](./aluno.py): código Python da atividade.
- [`enunciado.md`](./enunciado.md): transcrição dos exercícios e estudos de caso.
- [`README.md`](./README.md): documentação de execução e escopo.
- [`.gitignore`](./.gitignore): arquivos temporários ignorados pelo Git.

## Validação

- Sintaxe verificada com `python -m py_compile aluno.py`.
- Execução integral verificada com `python aluno.py`, encerrando sem exceções.
- Resultados exibidos no terminal para os exercícios presentes no código.

---

Saquarema/RJ · 2026  
Repositório acadêmico público.
