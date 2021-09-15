# 📮 Posts API
### API de posts CRUD desenvolvida com Flask e MongoDB

#### Projeto concluído ✔️

[Sobre](#sobre) • [Tecnologias](#tecnologias) • [Demonstração](#demonstração) • [Autora](#autora) • [Licença](#licença)

## Sobre
É possivel criar, editar, visualizar e excluir posts utilizando o endpoint /posts. Exemplo dos campos necessários para a criação de um post:
```
{
  "author": "",
  "title": "",
  "content": "",
  "tags": [
    "",
    ""
  ]
}
```
\
Para rodar a aplicação é preciso ter o MongoDB instalado no seu computador, também lembre-se de entrar no ambiente virtual (venv) e instalar todas as dependências do projeto! 😄

## Tecnologias
As seguintes ferramentas foram utilizadas na construção do projeto:

* Python
* Flask
* MongoDB

## Demonstração
#### POST /posts - Retorna o post criado com id, created_at e updated_at
![Rota post](https://i.imgur.com/Agq89ry.png)
#### GET /posts - Retorna uma lista com todos os posts
![Rota get](https://i.imgur.com/JS367ZE.png)
#### GET /posts/<:id> - Retorna o post com id correspondente ou erro 404
![Rota get - id](https://i.imgur.com/nolzYzJ.png)
![Rota get - id erro](https://i.imgur.com/pUxuneT.png)
#### PATCH /posts/<:id> - Retorna o post atualizado
![Rota patch](https://i.imgur.com/iX5dxdz.png)
#### DELETE /posts/<:id> - Retorna o post deletado
![Rota delete](https://i.imgur.com/v2fHqyw.png)

## Autora
Feito com ❤️ por:

Laiane Suzart - <a href="https://www.linkedin.com/in/laianesuzart/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
<a href="https://github.com/laianesuzart" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>

## Licença
Este projeto está sob a licença [MIT](https://choosealicense.com/licenses/mit/).
