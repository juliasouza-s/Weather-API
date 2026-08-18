## Weather API

API REST desenvolvida em **Python e FastAPI** que consulta dados meteorológicos da **Visual Crossing Weather API** e retorna as informações em formato JSON.

O projeto também utiliza **Redis para cache** das consultas e **Rate Limiting** para controlar o número de requisições.

## Tecnologias

* Python
* FastAPI
* Redis

## Funcionalidades

* Consulta do clima por cidade
* Temperatura atual, sensação térmica, máxima e mínima

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
