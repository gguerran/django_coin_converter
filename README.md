# DJANGO COIN CONVERTER

Esta aplicação consiste em uma pequena API que converte valores entre vários tipos de moedas.
Até o momento foram testadas as seguintes: 
```
USD
BRL
EUR
BTC
ETH
```

Abaixo estão descritas as informações sobre o funcionamento e o consumo da mesma.

## Download do repositório

    git clone https://github.com/gguerran/django_coin_converter.git

## Instalação
Não é necessário instalar a mesma, desde que o `Docker` e o `docker-compose` estejam instalados, apenas criar o .env:
```
cp example.env .env
```
Caso não estejam, siga as seguintes instruções:
```
cd django_coin_converter
cp example.env .env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
```

## Rodando a aplicação
Caso esteja usando o Docker o seguinte comando roda aplicação:
```
docker compose up
```
Caso contrário, o comando é:
```
./manage.py runserver
```

# API

Abaixo está descrito como utilizar a API.
Uma documentação melhor descrita e testável se encontra em http://127.0.0.1:8000/api/v1/swagger/

## Request

`GET /converter`

    curl -X 'GET' 'http://127.0.0.1:8000/api/v1/converter?amount=150.35&from=ETH&to=USD' -H 'accept: application/json'

## Responses

### Sucesso: 200
    
    {
        "from": "ETH",
        "to": "USD",
        "amount": 150.35,
        "converted": 244834.4505,
        "date": "2023-02-06"
    }

### Erro: 400
    
    {
        "error": "Não foi possível converter as moedas. Verifique os parâmetros informados."
    }
