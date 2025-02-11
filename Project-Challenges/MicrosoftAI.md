# 🛠️ Como Criar uma Conta na Microsoft Azure para Utilizar o Playground

### Passo 1: Acesse o Site da Azure
1. Clique [aqui](https://azure.microsoft.com/en-us/free/) para acessar o site oficial da Microsoft Azure.
2. Você será redirecionado para a página de **Criação de Conta Gratuita** da Azure.

### Passo 2: Iniciar o Processo de Criação de Conta
1. Na página inicial, clique no botão **Start free** ou **Comece gratuitamente**.
   - ![start-free](https://docs.microsoft.com/en-us/azure/media/azure-portal-free-trial-start.png)

### Passo 3: Entrar ou Criar uma Conta Microsoft
1. Se você já possui uma conta Microsoft, faça o login com suas credenciais.
2. Se não possui, clique em **Create one!** ou **Crie uma!** para criar uma nova conta.

### Passo 4: Preencher os Detalhes da Conta
1. Preencha os detalhes necessários como:
   - Nome
   - Sobrenome
   - País/Região
   - Endereço de E-mail
   - Senha

### Passo 5: Verificação de Identidade
1. A Microsoft solicitará uma verificação de identidade. Escolha uma das opções disponíveis:
   - Verificação por número de telefone (receber um código por SMS)
   - Verificação por e-mail (receber um código por e-mail)

### Passo 6: Detalhes de Pagamento
1. Insira os detalhes do seu cartão de crédito ou débito para verificação. **Nota:** Não haverá cobrança durante o período de avaliação gratuita.

### Passo 7: Aceitar os Termos e Condições
1. Leia e aceite os termos e condições da Microsoft Azure.
2. Clique em **Next** ou **Próximo**.

### Passo 8: Configuração Inicial
1. Após criar a conta, você será redirecionado para o portal da Azure.
2. Complete as configurações iniciais conforme solicitado.

### Passo 9: Acessar o Playground
1. No portal da Azure, navegue até a seção **Playground**.
2. Explore e aproveite os recursos gratuitos disponíveis.

### Recursos Adicionais
- Para mais detalhes, consulte a [Documentação Oficial da Azure](https://docs.microsoft.com/en-us/azure/)
- Visite a [Comunidade Microsoft](https://techcommunity.microsoft.com/) para suporte e dicas.

### 🚀 Pronto!
Agora você está pronto para usar a Microsoft Azure e explorar todas as funcionalidades do Playground! 🎉

# 🌟 Guia Detalhado de Implementação de APIs no Azure OpenAI

## 🧠 Introdução aos Agentes de IA
Os agentes de IA são sistemas que usam técnicas de inteligência artificial para realizar tarefas específicas de maneira autônoma. Eles podem ser utilizados em diversas áreas, como atendimento ao cliente, automação de processos, análise de dados e muito mais. A integração com APIs permite que esses agentes se comuniquem com outros sistemas e acessem dados externos para melhorar seu desempenho.

## 🚀 Passo-a-Passo para Implementação de APIs no Azure OpenAI

### Passo 1: Criação de uma Conta no Azure
1. Acesse o site do [Azure](https://azure.microsoft.com/en-us/free/).
2. Clique no botão **Start free** ou **Comece gratuitamente**.
3. Siga os passos para criar sua conta, conforme descrito no [guia de criação de conta](https://github.com/sdrariane/como-criar-conta-azure-playground.md).

### Passo 2: Configuração do Serviço Azure OpenAI
1. Após criar sua conta e fazer login no portal Azure, navegue até a seção **Create a resource**.
2. Procure por **Azure OpenAI** e selecione a opção correspondente.
3. Clique em **Create** para iniciar a configuração do serviço.

### Passo 3: Preenchimento dos Detalhes do Serviço
1. Escolha a **Subscription** apropriada.
2. Selecione um **Resource Group** ou crie um novo.
3. Dê um nome único para o seu serviço em **Name**.
4. Escolha a **Location** adequada para a sua organização.
5. Clique em **Review + create** e, em seguida, em **Create** para provisionar o serviço.

### Passo 4: Configuração da API
1. Após a criação do serviço, navegue até o recurso Azure OpenAI criado.
2. Na seção **Keys and Endpoint**, copie a **API Key** e o **Endpoint**.

### Passo 5: Implementação da API
1. No seu ambiente de desenvolvimento, instale as bibliotecas necessárias para fazer chamadas HTTP (e.g., `requests` para Python).
2. Configure seu código para autenticar e fazer chamadas à API usando a **API Key** e o **Endpoint**.

```python name=api_implementation.py
import requests

# Substitua 'your_api_key' e 'your_endpoint' pelos valores copiados
api_key = 'your_api_key'
endpoint = 'your_endpoint'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

data = {
    'prompt': 'Escreva um poema sobre a primavera.',
    'max_tokens': 50
}

response = requests.post(f'{endpoint}/v1/engines/davinci/completions', headers=headers, json=data)

print(response.json())
```
