# 🚗 ForceIA Multimarcas

Sistema de gestão de carros desenvolvido com Django, permitindo cadastro, listagem, edição e remoção de veículos com integração de IA para geração automática de descrições.

## 📋 Funcionalidades

- **Autenticação de Usuários**: Sistema completo de registro, login e logout
- **Gestão de Carros**: CRUD completo (Create, Read, Update, Delete)
- **Gestão de Marcas**: Cadastro de marcas de veículos
- **Busca**: Sistema de busca de carros por modelo
- **Upload de Imagens**: Suporte para fotos dos veículos
- **Descrições Inteligentes**: Geração automática de descrições usando OpenAI GPT
- **Inventário**: Controle automático de estoque e valor total dos carros
- **Validações**: Regras de negócio para valores mínimos e anos de fabricação

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Django 5.2.7**
- **PostgreSQL** - Banco de dados
- **OpenAI API** - Geração de descrições com IA
- **uWSGI** - Servidor de aplicação
- **Pillow** - Processamento de imagens

## 📦 Instalação

### Pré-requisitos

- Python 3.8+
- PostgreSQL
- pip

### Passo a passo

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install django psycopg2-binary Pillow openai python-dotenv uwsgi
```

4. **Configure o banco de dados**

Crie um banco PostgreSQL chamado `carros` e ajuste as credenciais em `app/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carros',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. **Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_api_openai
```

6. **Execute as migrações**
```bash
python manage.py migrate
```

7. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

8. **Inicie o servidor**
```bash
python manage.py runserver
```

Acesse: `http://localhost:8000/cars/`

## 🗂️ Estrutura do Projeto

```
├── accounts/              # App de autenticação
│   ├── templates/        # Templates de login e registro
│   └── views.py          # Views de autenticação
├── cars/                 # App principal de carros
│   ├── migrations/       # Migrações do banco
│   ├── templates/        # Templates dos carros
│   ├── admin.py          # Configuração do admin
│   ├── forms.py          # Formulários
│   ├── models.py         # Modelos (Car, Brand, CarInventory)
│   ├── signals.py        # Signals para inventário e IA
│   └── views.py          # Views baseadas em classes
├── app/                  # Configurações do projeto
│   ├── settings.py       # Configurações Django
│   ├── urls.py           # Rotas principais
│   └── templates/        # Template base
├── openai_api/           # Integração com OpenAI
│   └── client.py         # Cliente da API
└── manage.py             # Gerenciador Django
```

## 🎯 Modelos de Dados

### Brand (Marca)
- `name`: Nome da marca

### Car (Carro)
- `model`: Modelo do carro
- `brand`: Marca (ForeignKey)
- `factory_year`: Ano de fabricação (≥ 1975)
- `model_year`: Ano do modelo
- `plate`: Placa
- `value`: Valor (≥ R$ 20.000)
- `photo`: Foto do veículo
- `bio`: Descrição (gerada automaticamente por IA)

### CarInventory (Inventário)
- `cars_count`: Quantidade de carros
- `cars_value`: Valor total do inventário
- `created_at`: Data/hora de criação

## 🔐 Regras de Autenticação

- **Páginas públicas**: Lista de carros, detalhes
- **Páginas protegidas**: Cadastro de carros, marcas, edição e exclusão (requer login)

## 🤖 Integração com IA

O sistema utiliza a API da OpenAI (GPT-4.1-nano) para gerar automaticamente descrições dos carros baseadas em:
- Modelo
- Marca
- Valor
- Ano de fabricação

A descrição é limitada a 200 caracteres e é gerada automaticamente ao salvar um novo carro.

## 📊 Sistema de Inventário

O sistema mantém automaticamente um registro histórico do inventário através de signals Django:
- **post_save**: Atualiza inventário ao salvar um carro
- **post_delete**: Atualiza inventário ao deletar um carro

## 🚀 Deploy com uWSGI

O projeto inclui configuração para deploy com uWSGI. Arquivo de configuração: `carros_uwsgi.ini`

```bash
uwsgi --ini carros_uwsgi.ini
```

## 📝 Validações

- Valor mínimo: R$ 20.000
- Ano de fabricação: A partir de 1975
- Campos obrigatórios validados nos formulários

## 🎨 Interface

Interface responsiva com:
- Grid de carros (3 colunas em desktop, 2 em tablet)
- Cards com hover effects
- Sistema de busca integrado
- Navegação intuitiva

## 🔒 Segurança

⚠️ **ATENÇÃO**: Este projeto contém credenciais expostas no código. Para uso em produção:

1. Remova as credenciais do `settings.py`
2. Use variáveis de ambiente para todas as credenciais
3. Altere a `SECRET_KEY`
4. Configure `DEBUG = False`
5. Configure `ALLOWED_HOSTS` adequadamente

## 📄 Licença

Este projeto é livre para uso educacional e pessoal.

## 👨‍💻 Autor

ForceIA Multimarcas - Sistema de Gestão de Veículos

---

**Desenvolvido com Django 🎸**
