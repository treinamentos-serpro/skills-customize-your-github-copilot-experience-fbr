# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construir uma API REST para gerenciar uma coleção de livros usando FastAPI, praticando criação de rotas HTTP, validação de dados com modelos Pydantic e respostas apropriadas para diferentes situações.

## 📝 Tarefas

### 🛠️ Criar endpoints de consulta

#### Descrição

Complete a API para permitir que clientes consultem todos os livros e busquem um livro específico pelo seu identificador.

#### Requisitos

O programa concluído deve:

- Criar um endpoint `GET /books` que retorne a lista de livros.
- Criar um endpoint `GET /books/{book_id}` que retorne o livro correspondente.
- Retornar o status HTTP `404` quando o identificador não existir.
- Manter cada livro com, no mínimo, `id`, `title`, `author` e `available`.

### 🛠️ Adicionar criação e validação de livros

#### Descrição

Adicione um endpoint para cadastrar livros. Use um modelo Pydantic para validar os dados recebidos no corpo da requisição antes de incluí-los na coleção.

#### Requisitos

O programa concluído deve:

- Criar um endpoint `POST /books` que aceite um novo livro no corpo da requisição.
- Validar que `title` e `author` sejam preenchidos.
- Definir um identificador único e o valor inicial de `available` como `true` para cada novo livro.
- Retornar o livro criado com o status HTTP `201`.
- Rejeitar automaticamente dados inválidos com uma resposta de validação do FastAPI.

### 🛠️ Implementar atualização e remoção

#### Descrição

Complete o ciclo CRUD permitindo alterar a disponibilidade de um livro e removê-lo da coleção.

#### Requisitos

O programa concluído deve:

- Criar um endpoint `PATCH /books/{book_id}` para atualizar a disponibilidade do livro.
- Criar um endpoint `DELETE /books/{book_id}` para remover o livro.
- Retornar o status HTTP `404` quando a atualização ou remoção usar um identificador inexistente.
- Retornar uma resposta JSON confirmando a remoção bem-sucedida.
- Manter a documentação interativa da API acessível em `/docs`.
