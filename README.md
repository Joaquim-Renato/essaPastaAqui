# Criando uma Api para cadastrar produtos  

## Comandos
apos abrir o prompt de comando devo navegar até meu disco local c: ou d:
``````cmd
D:
``````

com o comando `cd` devo navegar até o diretorio em que meu projeto se encotontra 
EX: 
cd essaPastaAqui

``````cmd
D: cd essaPastaAqui
``````
### Depois com os seguintes comandos: 

``````cmd
python -m django startproject pricetracker

python manage.py startapp product
``````
### Para "rodar" nosso projeto utilizamos o comando 

``````bash
python manage.py runserver

``````

### Primeiros passos:


- configurar banco de dados:

em `settings.py` -> seções INSTALLED_APPS e DATABASES:

``````python

INSTALLED_APPS = [
    'django.contrib.admin',  # Interface de administração
    'django.contrib.auth',   # Sistema de autenticação
    'django.contrib.contenttypes',  # Suporte para tipos de conteúdo
    'django.contrib.sessions',  # Gerenciamento de sessões
    'django.contrib.messages',  # Suporte para mensagens
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos

    #  apps personalizados
    'pricetracker',
    'product',  # Substitui pelo nome do meu app
]

``````

``````python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',  # Porta padrão do MySQL
    }
}

``````

## Configurar o models : 

- Importação do módulo de modelos: O Django fornece uma classe base para criar modelos (models.Model), que deve ser herdada por todos os seus modelos.

- Definição de classes: Cada classe no models.py representa uma tabela no banco de dados.

- Campos: Cada atributo da classe representa uma coluna da tabela. O Django fornece diferentes tipos de campo para cada tipo de dado.

#### Exemplo de uso:
```python
from django.db import models

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)  # Chave primária com incremento automático
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

```

### Tipos de Campos Comuns

- **CharField**: Para textos curtos. Deve definir o parâmetro `max_length`.
- **TextField**: Para textos longos.
- **IntegerField**: Para números inteiros.
- **DecimalField**: Para números decimais. Deve definir `max_digits` (total de dígitos) e `decimal_places` (número de casas decimais).
- **DateTimeField**: Para datas e horários.
- **BooleanField**: Para valores `True/False`.
- **ForeignKey**: Para relacionamentos "um para muitos" entre tabelas.
- **ManyToManyField**: Para relacionamentos "muitos para muitos".
- **AutoField**: Para chaves primárias automáticas (gerado automaticamente se não especificado).


`AutoField` -> 
### AutoField no Django

O `AutoField` é um campo no Django que gera automaticamente valores incrementais únicos, geralmente usado como chave primária em modelos. Por padrão, o Django cria um campo `id` como `AutoField` se nenhuma chave primária for definida. É ideal para criar identificadores únicos de forma automática.



### Comandos para Gerenciar o Banco de Dados

No Django, os comandos abaixo são usados para gerenciar as migrações do banco de dados. As migrações garantem que as alterações feitas nos modelos sejam refletidas na estrutura do banco de dados.

#### `python manage.py makemigrations`
Este comando analisa os modelos definidos no projeto e cria arquivos de migração para registrar as alterações na estrutura do banco de dados, como a criação ou modificação de tabelas.

#### `python manage.py migrate`
Aplica as migrações pendentes ao banco de dados, criando ou alterando as tabelas de acordo com os arquivos de migração gerados.

#### Exemplo de Uso:
1. Crie as migrações com:

``````bash 
python manage.py makemigrations
    
``````

2. Aplique as migrações ao banco de dados com:

``````bash 
python manage.py migrate  

``````
---
### Criar uma pasta `TEMPLATES`

`Templates` devera armazenar os arquivos de template HTML 

#### Para que Serve a Pasta templates
Renderizar Dados Dinâmicos: Permite exibir informações vindas das views (como dados do banco de dados) dentro de páginas HTML.

Separação de Lógica e Apresentação: Mantém a lógica (views e modelos) separada do design (templates), facilitando a manutenção e organização do código.

Reutilização de Layouts: Usando herança de templates, você pode criar um layout comum para todas as páginas e reutilizá-lo.

### Alaterar o views:
O arquivo views.py no Django é responsável por definir a lógica que controla como os dados são exibidos ou processados em resposta às solicitações feitas pelos usuários. Ele conecta os modelos (dados) e os templates (interface do usuário), retornando respostas ao navegador ou outros clientes.

`views.py` 

Funções Principais do views.py
Receber solicitações: Processa as requisições feitas pelo cliente (navegador ou API) para o servidor.

Processar dados: Pode buscar, criar, atualizar ou excluir dados nos modelos e executar qualquer lógica necessária.

Retornar respostas: Envia uma resposta ao cliente, como:

Uma página HTML renderizada (template).
Dados em formatos como JSON ou XML (em APIs).
Um redirecionamento para outra página.

------

### Em seguida : 

na pasta product devo criar um arquivo `urls.py` no meu app 

-------
###  Lembrete 

Retornar em `settings.py` para configurar o "DIRS"
em 'BASE_DIR' existem um 

--------

# Importante lembrar de configurar 

em `templates` -> `cadprod.html` :
 {% csrf_token %} 

### Lembrete: 

'{{}}' duas chaves -> aponta/puxa uma variavel - para exibir variaveis; 

'{% %}' -> quando é uma ação utilizo chaves e porcentagem 


`strftime` = string format time
 -----

 ## Links importantes 
 
 Biblioteca de gráficos JavaScript simples, mas flexível, para a Web moderna

 https://www.chartjs.org/

----
 vb f