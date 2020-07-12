# Sistema de Varejo

Sistema demo para criação de produtos, usuários e cálculo de desconto em cada produto de acordo com o usuário, e datas e/ou eventos especiais.


## Estrutura

O Sistema é composto por 2 serviços;

#### Calculator Service:

Serviço que realiza o cálculo de desconto de cada produto.
O Serviço recebe o `id` do produto e pode receber o `id` do usuário e realiza o desconto para o produto informado. 
> curl -X GET  http://localhost:3333/discounts/1/?userId=1

    [CALCULATOR-SERVICE]/discounts/<product_id>/?userId=<user_id>
    
    {
      "total_discount": N,
      "final_price": V
    }
    N = Total de desconto do produto em (%)
    V = Valor final do produto com desconto

#### Base Service:

Serviço que realiza as operações de CRUD de Produtos e Usuários.
Esse serviço faz uma consulta para calcular o desconto que cada produto vai ter dependedo do usuário.    

##### API End-Points  

> products/  
> users/  

## Documentação da API

[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

**Produto**
    
    {
        "id": 1,
        "title": "Produto 1",
        "description": " Descrição do produto 1",
        "price": "100.00",
        "base_discount_percent": 0.1,
    }

**Usuário**
    
    {
        "id": 1,
        "first_name": "João",
        "last_name": "Silva",
        "birthdate": "2020-03-01"
    }

### Como Executar o Projeto:
Para subir os serviços seguir a ordem de comandos abaixo.
> make build
> make loaddata

`make build` inicia os todos os serviços (`postgres`, `base-service`, `calculator-service`)
`make loaddata` : popula o banco de dados com valores iniciais.

