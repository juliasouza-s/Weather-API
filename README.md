# 🌤️ Weather API

API REST desenvolvida em **Python e FastAPI** que consulta dados meteorológicos da **Visual Crossing Weather API** e retorna as informações em formato JSON.

O projeto também utiliza **Redis para cache** das consultas e **Rate Limiting** para controlar o número de requisições.

## 🛠️ Tecnologias

* Python
* FastAPI
* Pydantic
* Redis
* Requests
* Visual Crossing Weather API
* Git/GitHub

## ⚙️ Funcionalidades

* Consulta do clima por cidade
* Temperatura atual, sensação térmica, máxima e mínima
* Condições meteorológicas
* Cache de consultas com Redis
* Rate limiting
* Validação de parâmetros
* Tratamento de cidades inválidas
* Variáveis de ambiente para informações sensíveis


## Executando o projeto

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/juliasouza-s/weather-api.git
cd weather-api
pip install -r requirements.txt
```

Configure as variáveis de ambiente no arquivo `.env`:

```env
WEATHER_API_KEY=sua_chave_aqui
REDIS_HOST=localhost
REDIS_PORT=6379
```

Inicie o Redis e execute a aplicação:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## Exemplo

```http
GET /weather?city=São Paulo
```

Resposta:

```json
{
  "city": "São Paulo, SP",
  "temperature": 20.4,
  "feelslike": 19.8,
  "temp_max": 22.1,
  "temp_min": 16.7,
  "conditions": "Partially cloudy"
}
```

## Objetivo

Projeto desenvolvido para praticar **desenvolvimento de APIs com Python**, integração com serviços externos, **cache com Redis**, controle de requisições e organização de aplicações backend.
