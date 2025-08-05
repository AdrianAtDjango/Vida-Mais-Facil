# 👨‍⚕️ Vida+Fácil
Vida+Fácil é um portal web destinado à conectar profixxionais de saúde, cuidadores e pacientes da terceira idade, sendo a conexão dos idosos ao meio tecnologico. 

## 📦 Funcionalidades
* Cadastro e Autenticação de usuários
* Agendamento de consultas médicas
* Cadastro de indicadores de saúde (Pressão, Frequência Cardíaca, Peso e Glicemia)
* Acesso à conteúdos educativos para o público da 3ª idade


## ⚙ Tecnologias 
* Python 3.13+
* Django 
* Django Ninja (for API)
* SQLite (banco de dados padrão)
* HTML e SCSS (com DTL)

## 🚀 Como executar o projeto
1. Clone o repositório:
```bash
git clone https://github.com/AdrianAtDjango/Vida-Mais-Facil
```

2. Vá ao repositório, crie e ative uma venv python:
```bash
cd Vida-Mais-Facil
python -m venv venv
source venv/bin/activate # Linux/MacOS
venv\Scripts\activate # Windows
```

3. Instale as depêndencias e vá à pasta do projeto:
```bash
pip install django
pip install django-ninja
cd core
```

4. Faças as migrações e execute o servidor:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```