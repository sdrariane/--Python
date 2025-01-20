# Bootcamp Heineken
## Sumário

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [Construindo um Esquema Conceitual para Banco de Dados](#construindo-um-esquema-conceitual-para-banco-de-dados)
- [Construindo seu Primeiro Projeto Lógico de Banco de Dados](#construindo-seu-primeiro-projeto-lógico-de-banco-de-dados)
   * [01. Criação do Esquema do Banco de Dados](#01-criação-do-esquema-do-banco-de-dados)
   * [02. Inserção de Dados para Testes](#02-inserção-de-dados-para-testes)
   * [03. Queries SQL](#03-queries-sql)
      + [3.1 Recuperações simples com SELECT Statement](#31-recuperações-simples-com-select-statement)
      + [3.2 Filtros com WHERE Statement](#32-filtros-com-where-statement)
      + [3.3 Atributos derivados](#33-atributos-derivados)
      + [3.4 Ordenação com ORDER BY](#34-ordenação-com-order-by)
      + [3.5 Filtros em grupos – HAVING Statement](#35-filtros-em-grupos-having-statement)
      + [3.6 Junções entre tabelas](#36-junções-entre-tabelas)
- [Construa um Projeto Lógico de Banco de Dados do Zero](#construa-um-projeto-lógico-de-banco-de-dados-do-zero)
   * [01. Criação do Esquema do Banco de Dados](#01-criação-do-esquema-do-banco-de-dados-1)
   * [02. Inserção de Dados para Testes](#02-inserção-de-dados-para-testes-1)
   * [03. Queries SQL](#03-queries-sql-1)
      + [3.1 Recuperações simples com SELECT Statement](#31-recuperações-simples-com-select-statement-1)
      + [3.2 Filtros com WHERE Statement](#32-filtros-com-where-statement-1)
      + [3.3 Atributos derivados](#33-atributos-derivados-1)
      + [3.4 Ordenação com ORDER BY](#34-ordenação-com-order-by-1)
      + [3.5 Filtros em grupos – HAVING Statement](#35-filtros-em-grupos-having-statement-1)
      + [3.6 Junções entre tabelas](#36-junções-entre-tabelas-1)
- [Criando um Dashboard de Vendas do Xbox](#criando-um-dashboard-de-vendas-do-xbox)

<!-- TOC end -->

##Refinando um Projeto Conceitual de Banco de Dados – E-COMMERCE

```sql
-- Tabelas principais

-- Cliente
CREATE TABLE Cliente (
    ClienteID INT PRIMARY KEY IDENTITY,
    TipoCliente CHAR(2) CHECK (TipoCliente IN ('PF', 'PJ')), -- PF: Pessoa Física, PJ: Pessoa Jurídica
    Nome VARCHAR(255) NOT NULL,
    Documento VARCHAR(14) NOT NULL UNIQUE, -- CPF para PF ou CNPJ para PJ
    Email VARCHAR(255) NOT NULL UNIQUE,
    Telefone VARCHAR(15)
);

-- Forma de Pagamento
CREATE TABLE FormaPagamento (
    PagamentoID INT PRIMARY KEY IDENTITY,
    TipoPagamento VARCHAR(50) NOT NULL, -- Ex.: Cartão de Crédito, Boleto, Pix
    DetalhesPagamento VARCHAR(255) NULL -- Ex.: Número do cartão ou chave Pix
);

-- ClienteFormaPagamento (Relacionamento N:N entre Cliente e FormaPagamento)
CREATE TABLE ClienteFormaPagamento (
    ClienteID INT NOT NULL,
    PagamentoID INT NOT NULL,
    PRIMARY KEY (ClienteID, PagamentoID),
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ClienteID),
    FOREIGN KEY (PagamentoID) REFERENCES FormaPagamento(PagamentoID)
);

-- Pedido
CREATE TABLE Pedido (
    PedidoID INT PRIMARY KEY IDENTITY,
    ClienteID INT NOT NULL,
    DataPedido DATETIME NOT NULL DEFAULT GETDATE(),
    Total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ClienteID)
);

-- Entrega
CREATE TABLE Entrega (
    EntregaID INT PRIMARY KEY IDENTITY,
    PedidoID INT NOT NULL,
    StatusEntrega VARCHAR(50) NOT NULL, -- Ex.: Em preparo, Enviado, Entregue
    CodigoRastreamento VARCHAR(100) NULL,
    DataAtualizacao DATETIME NOT NULL DEFAULT GETDATE(),
    FOREIGN KEY (PedidoID) REFERENCES Pedido(PedidoID)
);

-- Produtos
CREATE TABLE Produto (
    ProdutoID INT PRIMARY KEY IDENTITY,
    NomeProduto VARCHAR(255) NOT NULL,
    Descricao VARCHAR(255) NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    Estoque INT NOT NULL
);

-- PedidoProduto (Relacionamento N:N entre Pedido e Produto)
CREATE TABLE PedidoProduto (
    PedidoID INT NOT NULL,
    ProdutoID INT NOT NULL,
    Quantidade INT NOT NULL CHECK (Quantidade > 0),
    PrecoUnitario DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PedidoID, ProdutoID),
    FOREIGN KEY (PedidoID) REFERENCES Pedido(PedidoID),
    FOREIGN KEY (ProdutoID) REFERENCES Produto(ProdutoID)
);

```

## Construindo um Esquema Conceitual para Banco de Dados

```sql

-- Tabela de Clientes
CREATE TABLE Cliente (
    ClienteID INT PRIMARY KEY IDENTITY,
    Nome VARCHAR(255) NOT NULL,
    Telefone VARCHAR(15),
    Email VARCHAR(255) UNIQUE,
    Endereco VARCHAR(255)
);

-- Tabela de Veículos
CREATE TABLE Veiculo (
    VeiculoID INT PRIMARY KEY IDENTITY,
    ClienteID INT NOT NULL,
    Marca VARCHAR(50) NOT NULL,
    Modelo VARCHAR(50) NOT NULL,
    Placa VARCHAR(10) UNIQUE NOT NULL,
    AnoFabricacao INT NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ClienteID)
);

-- Tabela de Mecânicos
CREATE TABLE Mecanico (
    MecanicoID INT PRIMARY KEY IDENTITY,
    Nome VARCHAR(255) NOT NULL,
    Endereco VARCHAR(255),
    Especialidade VARCHAR(100)
);

-- Tabela de Equipes
CREATE TABLE Equipe (
    EquipeID INT PRIMARY KEY IDENTITY,
    NomeEquipe VARCHAR(100) NOT NULL
);

-- Relacionamento entre Equipe e Mecânicos (N:N)
CREATE TABLE EquipeMecanico (
    EquipeID INT NOT NULL,
    MecanicoID INT NOT NULL,
    PRIMARY KEY (EquipeID, MecanicoID),
    FOREIGN KEY (EquipeID) REFERENCES Equipe(EquipeID),
    FOREIGN KEY (MecanicoID) REFERENCES Mecanico(MecanicoID)
);

-- Tabela de Serviços
CREATE TABLE Servico (
    ServicoID INT PRIMARY KEY IDENTITY,
    Descricao VARCHAR(255) NOT NULL,
    ValorMaoDeObra DECIMAL(10, 2) NOT NULL
);

-- Tabela de Peças
CREATE TABLE Peca (
    PecaID INT PRIMARY KEY IDENTITY,
    Nome VARCHAR(100) NOT NULL,
    Valor DECIMAL(10, 2) NOT NULL
);

-- Tabela de Ordens de Serviço (OS)
CREATE TABLE OrdemServico (
    OSID INT PRIMARY KEY IDENTITY,
    VeiculoID INT NOT NULL,
    EquipeID INT NOT NULL,
    DataEmissao DATETIME NOT NULL DEFAULT GETDATE(),
    DataConclusao DATETIME NULL,
    ValorTotal DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    Status VARCHAR(50) NOT NULL, -- Ex.: Pendente, Em Execução, Concluído
    FOREIGN KEY (VeiculoID) REFERENCES Veiculo(VeiculoID),
    FOREIGN KEY (EquipeID) REFERENCES Equipe(EquipeID)
);

-- Relacionamento entre OS e Serviços (N:N)
CREATE TABLE OSServico (
    OSID INT NOT NULL,
    ServicoID INT NOT NULL,
    Quantidade INT NOT NULL CHECK (Quantidade > 0),
    Valor DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OSID, ServicoID),
    FOREIGN KEY (OSID) REFERENCES OrdemServico(OSID),
    FOREIGN KEY (ServicoID) REFERENCES Servico(ServicoID)
);

-- Relacionamento entre OS e Peças (N:N)
CREATE TABLE OSPeca (
    OSID INT NOT NULL,
    PecaID INT NOT NULL,
    Quantidade INT NOT NULL CHECK (Quantidade > 0),
    Valor DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OSID, PecaID),
    FOREIGN KEY (OSID) REFERENCES OrdemServico(OSID),
    FOREIGN KEY (PecaID) REFERENCES Peca(PecaID)
);

```

## Construindo seu Primeiro Projeto Lógico de Banco de Dados
### 01. Criação do Esquema do Banco de Dados

```sql
-- Criação do banco de dados
CREATE DATABASE ECommerceDB;
GO

USE ECommerceDB;
GO

-- Tabela de Clientes (PJ e PF)
CREATE TABLE Clientes (
    ClienteID INT IDENTITY(1,1) PRIMARY KEY,
    Nome NVARCHAR(100) NOT NULL,
    Tipo NVARCHAR(2) CHECK (Tipo IN ('PJ', 'PF')) NOT NULL,
    CNPJ_CPF NVARCHAR(20) NOT NULL UNIQUE
);

-- Tabela de Formas de Pagamento
CREATE TABLE FormasPagamento (
    PagamentoID INT IDENTITY(1,1) PRIMARY KEY,
    Metodo NVARCHAR(50) NOT NULL,
    Detalhes NVARCHAR(255) NULL
);

-- Tabela de Pedidos
CREATE TABLE Pedidos (
    PedidoID INT IDENTITY(1,1) PRIMARY KEY,
    ClienteID INT NOT NULL FOREIGN KEY REFERENCES Clientes(ClienteID),
    DataPedido DATETIME NOT NULL,
    ValorTotal DECIMAL(10, 2) NOT NULL
);

-- Tabela de Entregas
CREATE TABLE Entregas (
    EntregaID INT IDENTITY(1,1) PRIMARY KEY,
    PedidoID INT NOT NULL FOREIGN KEY REFERENCES Pedidos(PedidoID),
    Status NVARCHAR(50) NOT NULL,
    CodigoRastreamento NVARCHAR(50) NOT NULL
);

-- Tabela de Produtos
CREATE TABLE Produtos (
    ProdutoID INT IDENTITY(1,1) PRIMARY KEY,
    NomeProduto NVARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    FornecedorID INT NOT NULL
);

-- Tabela de Estoques
CREATE TABLE Estoques (
    EstoqueID INT IDENTITY(1,1) PRIMARY KEY,
    ProdutoID INT NOT NULL FOREIGN KEY REFERENCES Produtos(ProdutoID),
    Quantidade INT NOT NULL
);

-- Tabela de Fornecedores
CREATE TABLE Fornecedores (
    FornecedorID INT IDENTITY(1,1) PRIMARY KEY,
    NomeFornecedor NVARCHAR(100) NOT NULL,
    Telefone NVARCHAR(15) NULL
);

-- Tabela Pedido_Produto para relacionamento N:N
CREATE TABLE Pedido_Produto (
    PedidoID INT NOT NULL FOREIGN KEY REFERENCES Pedidos(PedidoID),
    ProdutoID INT NOT NULL FOREIGN KEY REFERENCES Produtos(ProdutoID),
    Quantidade INT NOT NULL,
    PRIMARY KEY (PedidoID, ProdutoID)
);
GO

```

### 02. Inserção de Dados para Testes

```sql
-- Inserindo clientes
INSERT INTO Cliente (Nome, TipoCliente, Documento) VALUES
('João Silva', 'PF', '12345678901'),
('Empresa XYZ', 'PJ', '98765432000198');

-- Inserindo fornecedores
INSERT INTO Fornecedor (Nome, Contato) VALUES
('Fornecedor A', 'fornecedor_a@example.com'),
('Fornecedor B', 'fornecedor_b@example.com');

-- Inserindo produtos
INSERT INTO Produto (NomeProduto, FornecedorID, Preco, Estoque) VALUES
('Produto 1', 1, 100.00, 50),
('Produto 2', 2, 200.00, 30);

-- Inserindo pedidos
INSERT INTO Pedido (ClienteID, DataPedido, ValorTotal, Status) VALUES
(1, '2025-01-10', 500.00, 'Concluído'),
(2, '2025-01-12', 1000.00, 'Pendente');

-- Inserindo pagamentos
INSERT INTO Pagamento (PedidoID, FormaPagamento, ValorPago) VALUES
(1, 'Cartão de Crédito', 500.00),
(2, 'Boleto Bancário', 1000.00);

-- Inserindo entregas
INSERT INTO Entrega (PedidoID, StatusEntrega, CodigoRastreamento) VALUES
(1, 'Entregue', 'ABC123456'),
(2, 'Em Transporte', 'DEF654321');

-- Inserindo produtos nos pedidos
INSERT INTO PedidoProduto (PedidoID, ProdutoID, Quantidade, PrecoUnitario) VALUES
(1, 1, 2, 100.00),
(2, 2, 3, 200.00);
GO
```

### 03. Queries SQL
#### 3.1 Recuperações simples com SELECT Statement

```sql
-- Recuperar todos os clientes
SELECT * FROM Cliente;

-- Recuperar todos os produtos
SELECT * FROM Produto;
```

#### 3.2 Filtros com WHERE Statement

```sql
-- Buscar pedidos concluídos
SELECT * FROM Pedido WHERE Status = 'Concluído';

-- Buscar produtos com estoque abaixo de 40 unidades
SELECT * FROM Produto WHERE Estoque < 40;
```

#### 3.3 Atributos derivados

```sql
-- Calcular o valor total de cada pedido (derivado de PedidoProduto)
SELECT 
    PedidoID, 
    SUM(Quantidade * PrecoUnitario) AS ValorCalculado 
FROM PedidoProduto
GROUP BY PedidoID;
```

#### 3.4 Ordenação com ORDER BY

```sql
-- Ordenar clientes pelo nome
SELECT * FROM Cliente ORDER BY Nome;

-- Ordenar produtos pelo preço de forma decrescente
SELECT * FROM Produto ORDER BY Preco DESC;
```

#### 3.5 Filtros em grupos – HAVING Statement

```sql
-- Listar pedidos com valor total maior que 600
SELECT 
    PedidoID, 
    SUM(Quantidade * PrecoUnitario) AS ValorCalculado 
FROM PedidoProduto
GROUP BY PedidoID
HAVING SUM(Quantidade * PrecoUnitario) > 600;
```

#### 3.6 Junções entre tabelas

```sql
-- Relacionar pedidos com os clientes
SELECT 
    p.PedidoID, 
    c.Nome AS NomeCliente, 
    p.DataPedido, 
    p.Status 
FROM Pedido p
JOIN Cliente c ON p.ClienteID = c.ClienteID;

-- Relacionar produtos com fornecedores
SELECT 
    pr.NomeProduto, 
    f.Nome AS NomeFornecedor 
FROM Produto pr
JOIN Fornecedor f ON pr.FornecedorID = f.FornecedorID;

-- Relação de pedidos, produtos e clientes
SELECT 
    pp.PedidoID, 
    c.Nome AS NomeCliente, 
    pr.NomeProduto, 
    pp.Quantidade, 
    pp.PrecoUnitario 
FROM PedidoProduto pp
JOIN Pedido p ON pp.PedidoID = p.PedidoID
JOIN Cliente c ON p.ClienteID = c.ClienteID
JOIN Produto pr ON pp.ProdutoID = pr.ProdutoID;
```

## Construa um Projeto Lógico de Banco de Dados do Zero
### 01. Criação do Esquema do Banco de Dados

```sql
-- Criação do banco de dados
CREATE DATABASE LojaOnline;
GO

USE LojaOnline;
GO

-- Tabela de Clientes
CREATE TABLE Cliente (
    ClienteID INT PRIMARY KEY IDENTITY(1,1),
    Nome NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    TipoCliente NVARCHAR(2) CHECK (TipoCliente IN ('PF', 'PJ')), -- PF: Pessoa Física, PJ: Pessoa Jurídica
    Documento NVARCHAR(20) UNIQUE NOT NULL
);

-- Tabela de Produtos
CREATE TABLE Produto (
    ProdutoID INT PRIMARY KEY IDENTITY(1,1),
    NomeProduto NVARCHAR(100) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Estoque INT NOT NULL
);

-- Tabela de Pedidos
CREATE TABLE Pedido (
    PedidoID INT PRIMARY KEY IDENTITY(1,1),
    ClienteID INT NOT NULL FOREIGN KEY REFERENCES Cliente(ClienteID),
    DataPedido DATE NOT NULL,
    ValorTotal DECIMAL(10,2),
    Status NVARCHAR(50)
);

-- Tabela de Itens do Pedido
CREATE TABLE PedidoProduto (
    PedidoProdutoID INT PRIMARY KEY IDENTITY(1,1),
    PedidoID INT NOT NULL FOREIGN KEY REFERENCES Pedido(PedidoID),
    ProdutoID INT NOT NULL FOREIGN KEY REFERENCES Produto(ProdutoID),
    Quantidade INT NOT NULL,
    PrecoUnitario DECIMAL(10,2) NOT NULL
);
GO
```

### 02. Inserção de Dados para Testes

```sql
-- Inserindo clientes
INSERT INTO Cliente (Nome, Email, TipoCliente, Documento) VALUES
('João Silva', 'joao.silva@example.com', 'PF', '12345678901'),
('Empresa ABC', 'contato@empresaabc.com.br', 'PJ', '98765432000198');

-- Inserindo produtos
INSERT INTO Produto (NomeProduto, Preco, Estoque) VALUES
('Notebook', 3000.00, 10),
('Smartphone', 1500.00, 20),
('Tablet', 1000.00, 15);

-- Inserindo pedidos
INSERT INTO Pedido (ClienteID, DataPedido, ValorTotal, Status) VALUES
(1, '2025-01-15', 4500.00, 'Concluído'),
(2, '2025-01-16', 3000.00, 'Pendente');

-- Inserindo itens dos pedidos
INSERT INTO PedidoProduto (PedidoID, ProdutoID, Quantidade, PrecoUnitario) VALUES
(1, 1, 1, 3000.00),
(1, 2, 1, 1500.00),
(2, 1, 1, 3000.00);
GO
```

### 03. Queries SQL
#### 3.1 Recuperações simples com SELECT Statement

```sql
-- Recuperar todos os clientes
SELECT * FROM Cliente;

-- Recuperar todos os produtos com estoque disponível
SELECT NomeProduto, Estoque FROM Produto WHERE Estoque > 0;
```

#### 3.2 Filtros com WHERE Statement

```sql
-- Recuperar pedidos concluídos
SELECT * FROM Pedido WHERE Status = 'Concluído';

-- Buscar produtos com preço maior que R$1.500,00
SELECT * FROM Produto WHERE Preco > 1500.00;
```

#### 3.3 Atributos derivados

```sql
-- Calcular o valor total dos itens em cada pedido
SELECT 
    PedidoID, 
    SUM(Quantidade * PrecoUnitario) AS ValorCalculado
FROM PedidoProduto
GROUP BY PedidoID;
```

#### 3.4 Ordenação com ORDER BY

```sql
-- Ordenar clientes pelo nome em ordem alfabética
SELECT * FROM Cliente ORDER BY Nome;

-- Ordenar produtos pelo preço, do mais caro ao mais barato
SELECT * FROM Produto ORDER BY Preco DESC;
```

#### 3.5 Filtros em grupos – HAVING Statement

```sql
-- Listar pedidos cujo valor total é maior que R$3.000,00
SELECT 
    PedidoID, 
    SUM(Quantidade * PrecoUnitario) AS ValorCalculado
FROM PedidoProduto
GROUP BY PedidoID
HAVING SUM(Quantidade * PrecoUnitario) > 3000;
```

#### 3.6 Junções entre tabelas

```sql
-- Relacionar pedidos com os clientes
SELECT 
    p.PedidoID,
    c.Nome AS NomeCliente,
    p.DataPedido,
    p.Status
FROM Pedido p
JOIN Cliente c ON p.ClienteID = c.ClienteID;

-- Relacionar produtos aos pedidos
SELECT 
    pp.PedidoID,
    pr.NomeProduto,
    pp.Quantidade,
    pp.PrecoUnitario
FROM PedidoProduto pp
JOIN Produto pr ON pp.ProdutoID = pr.ProdutoID;

-- Detalhar os pedidos, incluindo cliente e itens
SELECT 
    p.PedidoID,
    c.Nome AS NomeCliente,
    pr.NomeProduto,
    pp.Quantidade,
    pp.PrecoUnitario,
    (pp.Quantidade * pp.PrecoUnitario) AS ValorItem
FROM Pedido p
JOIN Cliente c ON p.ClienteID = c.ClienteID
JOIN PedidoProduto pp ON p.PedidoID = pp.PedidoID
JOIN Produto pr ON pp.ProdutoID = pr.ProdutoID;
```

## Criando um Dashboard de Vendas do Xbox
