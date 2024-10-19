# Site de Anúncios de Carros

Este projeto é um **site simples para anunciar carros**, desenvolvido com **Python** e o framework **Django**, utilizando o banco de dados **PostgreSQL**.

## Funcionalidades

- Cadastro e login de usuários
- Adicionar, editar e excluir anúncios de carros
- Visualizar lista de carros anunciados
- Interface amigável e responsiva

## Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Framework:** Django
- **Banco de Dados:** PostgreSQL

## Requisitos do Projeto

Para rodar o projeto localmente, você precisará ter instalados:

- Python 3.x
- PostgreSQL
- Django 4.x
- Virtualenv (opcional, mas recomendado)

## Como Executar o Projeto

### 1. Clone o repositório
Faça o clone do repositório para a sua máquina local:

```bash
git clone https://github.com/llyndev/project-car.git
cd project-car
```

### 2. Crie um ambiente virtual

Se você estiver usando `virtualenv`, pode criar e ativar o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate      # Windows
```
### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Certifique-se de que você tem o PostgreSQL rodando. Depois, configure as credenciais do banco de dados no arquivo settings.py:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Comandos 

Comandos para fazer a migração do banco de dados, criar super usúario e iniciar o servidor

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver

