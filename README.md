# Brilho ✨
O objetivo deste projeto é desenvolver um aplicativo de caráter social que permita que os usuários resgatem cupons no Centro Velho de São Paulo, esse projeto será desenvolvido durante o Terceiro Semestre do curso Análise e Desenvolvimento de Sistemas do Centro Universitário Belas Artes de São Paulo.

# Documentação ✉️
[**Clique aqui para acessar a documentação da API**](https://brilho-api.onrender.com/docs#/?)
![image](https://github.com/thaizacn/brilho-python/assets/77704621/2d5a6499-f124-47df-bd40-4e04759cd100)

## Funcionalidades

### 1. Consultar Todos os Cupons
- **Endpoint:** `/cupons`
- **Método:** GET
- **Descrição:** Retorna uma lista de todos os cupons disponíveis.

### 2. Consultar Cupom por ID
- **Endpoint:** `/cupons/{cupom_id}`
- **Método:** GET
- **Descrição:** Retorna detalhes de um cupom específico com base no ID fornecido.

### 3. Cadastrar Novo Cupom
- **Endpoint:** `/cupons`
- **Método:** POST
- **Descrição:** Cadastra um novo cupom com base nos dados fornecidos no corpo da solicitação.

### 4. Resgatar Cupom
- **Endpoint:** `/cupons/{cupom_id}`
- **Método:** DELETE
- **Descrição:** Marca um cupom como resgatado com base no ID fornecido.

# Configuração ⚙️

### Requisitos
- Python 3.8 ou superior
- Docker (opcional)

### Instalação
1. Clone o repositório: `git clone https://github.com/seu-usuario/seu-repositorio.git`
2. Entre no diretório do projeto: `cd brilho-python`

### Execução sem Docker
1. Crie um ambiente virtual: `python -m venv venv`
2. Ative o ambiente virtual:
   - No Windows: `venv\Scripts\activate`
   - No Linux/Mac: `source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o aplicativo: `uvicorn main:app --host 0.0.0.0 --port 8000`

### Execução com Docker
1. Certifique-se de ter o Docker instalado.
2. Execute o comando: `docker build -t brilho-python .`
3. Execute o contêiner: `docker run -p 8000:8500 brilho-python`


# 🛠️ Tecnologias 
- Este projeto foi desenvolvido em Python
- O Banco de Dados para consumo é o Postgress

# 🎁 Agradecimentos
Esse projeto foi feito com muito amor pela equipe "Café sem Açucar" e poderá ser utilizado como veículo de estudo por qualquer um que, assim como nós, tenha o desejo genuíno por mudar o mundo. Nós conseguimos. Juntos.

⌨️ com ❤️ por Café sem Açúcar ☕ 
