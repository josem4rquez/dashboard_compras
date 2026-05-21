import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

pasta_datasets = Path(__file__).parent / "datasets"

pasta_datasets.mkdir(parents=True, exist_ok=True)

LOJAS = [
    {"estado": "SP", "cidade": "São Paulo", 
     "vendedores": ["João Silva", "Maria Oliveira", "Carlos Santos"]},
    {"estado": "MG", "cidade": "Belo Horizonte", 
     "vendedores": ["João Pedro", "Maria Paula", "Antonio Santos"]},
    {"estado": "RJ", "cidade": "Rio de Janeiro", 
     "vendedores": ["Pedro Souza", "Maria Santos", "Marlene Oliveira"]},
    {"estado": "PR", "cidade": "Curitiba", 
     "vendedores": ["José Marques", "Mariana Miranda", "Carlos Alberto"]},
    {"estado": "SC", "cidade": "Florianópolis", 
     "vendedores": ["Eduardo Silva", "Emilia Costa", "Tiago Santos"]},
]

PRODUTOS = [
    {"nome": "Smartphone Samsung Galaxy", "id": 0, "preco": 1500.00},
    {"nome": "Notebook Dell Inspiron", "id": 1, "preco": 3500.00},
    {"nome": "Tablet Apple iPad", "id": 2, "preco": 2500.00},
    {"nome": "PC Gamer Pichau", "id": 3, "preco": 5000.00},
    {"nome": "Apple Watch 3", "id": 4, "preco": 3000.00},
]

FORMA_PAGTO = ["Cartão de Crédito", "Boleto", "Pix", "Dinheiro"]
GENERO_CLIENTE = ["Masculino", "Feminino"]

compras = []

for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja["vendedores"])
    produto = random.choice(PRODUTOS)
    hora_compra = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)
    )
    genero_cliente = random.choice(GENERO_CLIENTE)
    nome_cliente = names.get_full_name(genero_cliente)
    forma_pagto = random.choice(FORMA_PAGTO)

    compras.append({
        "data": hora_compra,
        "id_compra": 0,
        "loja": loja["cidade"],
        "vendedor": vendedor,
        "produto": produto["nome"],
        "cliente_nome": nome_cliente,
        "cliente_genero": genero_cliente.replace("female", "feminino").replace("male", "masculino"),
        "forma_pagto": forma_pagto,
    })

df_compras = pd.DataFrame(compras).set_index("data").sort_index()
df_compras["id_compra"] = [i for i in range(len(df_compras))]

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)


#Exportando Dataframes
df_compras.to_csv(pasta_datasets / "compras.csv", decimal =",", sep=";")
df_lojas.to_csv(pasta_datasets / "lojas.csv", decimal =",", sep=";")
df_produtos.to_csv(pasta_datasets / "produtos.csv", decimal =",", sep=";")

df_compras.to_excel(pasta_datasets / "compras.xlsx")
df_lojas.to_excel(pasta_datasets / "lojas.xlsx")
df_produtos.to_excel(pasta_datasets / "produtos.xlsx")