# 🛒 Dashboard de Compras com Streamlit

![Dashboard](images/dashboard.png)

Dashboard interativo desenvolvido com **Python, Pandas e Streamlit** para análise de compras, produtos, vendedores e faturamento em tempo real.

O projeto permite visualizar métricas importantes, aplicar filtros dinâmicos e gerar insights de forma rápida e intuitiva por meio de uma interface web simples e responsiva.

---

## 📊 Funcionalidades

- Visualização de indicadores de vendas
- Análise de faturamento
- Consulta de produtos vendidos
- Análise por loja e vendedor
- Filtros interativos
- Atualização dinâmica dos dados
- Interface desenvolvida com Streamlit

---

## 🗂️ Estrutura dos Dados

O projeto utiliza três conjuntos de dados:

### Compras
Contém o histórico das vendas realizadas.

| Coluna |
|----------|
| data |
| id_compra |
| loja |
| vendedor |
| produto |
| cliente_nome |
| cliente_genero |
| forma_pagto |

### Produtos
Informações sobre os produtos comercializados.

| Coluna |
|----------|
| id |
| nome |
| preco |

### Lojas
Informações das lojas participantes.

| Coluna |
|----------|
| estado |
| cidade |
| vendedores |

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Streamlit

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Entre na pasta do projeto

```bash
cd seu-repositorio
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o dashboard

```bash
streamlit run app.py
```

---

## 📈 Exemplos de Análises

- Faturamento total
- Produtos mais vendidos
- Distribuição de formas de pagamento
- Desempenho por vendedor
- Comparação entre lojas
- Perfil dos clientes

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com fins de estudo e portfólio, aplicando conceitos de:

- Manipulação de dados com Pandas
- Visualização de informações
- Desenvolvimento de dashboards
- Análise exploratória de dados
- Criação de aplicações web com Streamlit

---

## 👨‍💻 Autor

José Marques

Desenvolvedor focado em Python, Ciência de Dados e Engenharia de Dados.
