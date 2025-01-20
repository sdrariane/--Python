## Refinando um Projeto Conceitual de Banco de Dados – E-COMMERCE

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
