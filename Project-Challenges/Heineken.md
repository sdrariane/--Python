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
