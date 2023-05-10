# desafio_ascan

## Iniciando o projeto do desafio de Back end iniciante - ASCAN

O aplicação do desafio Ascan consiste em uma aplicação back end rest API com funcionalidades de mensageria utilizando o protocolo MQTT

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](#desafio_ascan)
   * [Tabela de Conteudo](#tabela-de-conteúdos)
   * [Como rodar o projeto](#como-rodar-o-projeto)
      * [Pre Requisitos](#pré-requisitos)
      * [dependecias](#dependecias)
      * [Rodando a aplicação](#rodando-a-aplicação)
   * [Tecnologias](#tecnologias)
<!--te-->

# Como Rodar o projeto


### Pré-requisitos

Antes de começar a rodar o projeto, você vai precisar instalar em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [python](https://www.python.org/), [mysql](https://www.mysql.com/), [rabbitmq](https://www.rabbitmq.com/)  e [docker](https://docs.docker.com/get-docker/)(opcional)

Após isso é recomendável a instalação de um editor de código(caso não tenha), como o [VSCode](https://code.visualstudio.com/)

**Antes de continuar, caso já tenha o `docker` e o `docker compose` instalado basta apenas fazer o clone do repositório, acessar a pasta do projecto e rodar comando `docker compose up -d`, deste modo o comando estarão rodando em background 3 containers: A aplicação, o banco de dados mysql e o broquer rabbitmq**

Agora caso queira rodar a aplicação localmente pode seguir com as instruções abaixo.

Posterirormente após fazer o clone do repositório e acessar a pasta desafio_ascan crie uma arquivo `.env` com as seguintes variáveis de ambiente:<br>
        `DB_USERNAME=<nome do usuário do banco de dados>`<br>
        `DB_PASSWORD=<password do usuário>`<br>
        `DB_PORT=3306`<br>
        `DB_HOST=localhost`<br>
        `FLASK_APP=src`<br>
        `FLASK_ENV=development`<br>
        `SECRET_KEY=dev`<br>
        `JWT_SECRET_KEY=JWT_SECRET_KEY`<br>
        `EXCHANGE_NAME=ascan_exchange`<br>
        `QUEUE_NAME=ascan_que`<br>
        `ROUTING_KEY=ascan_key`<br>
        `RABBITMQ_HOST=localhost`<br>

### dependências

para ver a versões de cada pacote acesse o [requirements.txt](requirements.txt) do projeto

### Rodando a aplicação


1. #### Clone este repositório
   `git clone https://github.com/josedembo/desafio_ascan`

2. #### Acesse a pasta do projeto no terminal/cmd
   `cd desafio_ascan`

3. #### crie um ambiente virtual
    `python3 -m venv venv`

3. #### Instale as dependências(pode usar qualquel uma das opções abaixo)
 
   `pip install -r requirements.txt` 

4. #### caso já tenha o [mysql](https://www.postgresql.org/download/) instalado em sua máquina, crie um novo database com o nome `desafio_ascan`. 5.Caso não tenha o mysql ou broquer do rabbitmq instalado em sua máquina, mas tiver o [docker](https://docs.docker.com/get-docker/) instalado execute o camando abaixo para rodar um container do mysql e do rabbitmq

   `docker-compose up -d`

5. #### execute qualquer uma das opções abaixo para rodar as migrations e criar as tabelas no banco de dados

   `alembic upgrade head`

6. #### Execute a aplicação em modo de desenvolvimento

   `flask run`

#### O servidor estará rodando  na porta: 5000
#### Pode consumir a API usando [Insomnia](https://insomnia.rest/download), [postman](https://www.postman.com/downloads/##) ou qualquer  ferramenta de sua preferência

Agora pode acessar a documentação da API usando o Swagger UI em: `http:localhost:5000/docs/`
## Tecnologias
As ferramentas abaixo foram usadas para a construção do projeto: 

- [x] [python](https://nodejs.org/en/)
- [x] [flask](https://www.typescriptlang.org/)
- [x] [Docker](https://www.docker.com/)
- [x] [sqlAlchemy](https://typeorm.io/#/)
- [x] [rabbitmq](https://typeorm.io/#/)

