# Atualizações no Código

## Manipulação de Exceção de Integridade de Dados

Para garantir que tratamos corretamente a exceção `IntegrityError`, implementamos um manipulador de exceção personalizado. Isso nos permite lidar com situações em que ocorre uma violação de integridade de dados, como tentar inserir um atleta com um CPF que já está em uso.

```python
@router.exception_handler(IntegrityError)
async def integrity_error_handler(request, exc):
    # 🚫 Manipulação da Exceção de Integridade dos Dados 🚫
```

## Adição de Paginação

Adicionamos suporte para paginação aos endpoints de consulta (`query`). Agora, você pode usar os parâmetros `limit` e `offset` para controlar o número de resultados retornados e a posição de início dos resultados, respectivamente.

```python
@router.get(
    '/', 
    summary='Consultar todos os Atletas',
    status_code=status.HTTP_200_OK,
    response_model=Page[AtletaOut],
)
async def query(
    db_session: DatabaseDependency,
    nome: str = Query(None),
    cpf: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)
) -> Page[AtletaOut]:
    # 🔄 Adicionado suporte para Paginação 🔄
```
## Customização da Response de Retorno

Personalizamos a resposta de retorno dos endpoints para incluir apenas os campos necessários. No caso do endpoint que retorna todos os atletas (`query`), modificamos a resposta para incluir apenas os campos 'nome', 'centro de treinamento' e 'categoria'.

```python
@router.get(
    '/', 
    summary='Consultar todos os Atletas',
    status_code=status.HTTP_200_OK,
    response_model=Page[AtletaOut],
)
async def query(
    db_session: DatabaseDependency,
    nome: str = Query(None),
    cpf: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)
) -> Page[AtletaOut]:
    # 🔄 Adicionado suporte para Paginação 🔄
    # 🎨 Customização da Response de Retorno 🎨
```
