# Criação de um Phishing com o Kali Linux

## O que é Phishing?
Phishing é um tipo de ataque cibernético que usa e-mails, mensagens de texto, telefonemas ou sites fraudulentos para enganar as pessoas a compartilhar dados confidenciais, baixar malware ou se expor a crimes cibernéticos de outras formas.

Atualmente existem bibliotecas (libs) como a `zphisher` que já fornecem templates deixando apenas a encargo do usuário a configuração deste sistema de coleta maliciosa dos dados.

## Socialphishing
Socialphish é uma poderosa ferramenta de phishing open-source extremamente popular devido à engenharia social utilizada ser mais amigável ao público. Ela oferece modelos de páginas da web para 33 sites populares, como Facebook, Instagram, Google, Snapchat, Github, Yahoo, Protonmail, Spotify, Netflix, Linkedin, WordPress, Origin, Steam, Microsoft, etc.

### Passo-a-passo

- Abra seu sistema operacional Kali Linux. Mova para a área de trabalho. Aqui você tem que criar um diretório chamado Socialphish. Neste diretório, você tem que instalar a ferramenta.

`cd Desktop`

- Agora você está na área de trabalho. Aqui você tem que criar um diretório chamado Socialphish. Para criar o diretório Maskphish use o seguinte comando.

`mkdir Socialphish`

- Você criou um diretório. Agora use o comando a seguir para mover para esse diretório.

`cd Socialphish`

- Agora você está no diretório Socialphish. Neste diretório você tem que baixar a ferramenta, o que significa que você tem que clonar a ferramenta do GitHub. Use o seguinte comando para clonar a ferramenta do GitHub.

`git clone https://github.com/xHak9x/SocialPhish.git`

- A ferramenta foi baixada no diretório Socialphish. Agora, para listar o conteúdo da ferramenta que foi baixada, use o seguinte comando.

`ls`

- Quando você listou o conteúdo da ferramenta, você pode ver que um novo diretório foi gerado pela ferramenta que é o SocialPhish. Você tem que mover para este diretório para visualizar o conteúdo da ferramenta. Para mover neste diretório, use o seguinte comando.

`cd SocialPhish`

- Para listar o conteúdo deste diretório, use o seguinte comando.

`ls`

- Agora você tem que dar permissão para a ferramenta usando o seguinte comando.

`chmod +x socialphish.sh`

- Agora você pode executar a ferramenta usando o seguinte comando. Este comando abrirá o menu de ajuda da ferramenta.

`./socialphish.sh`

- Use o Socialphish e crie uma página de phishing para o Instagram. Digite 01 e depois para encaminhamento de porta 02.

Você pode ver que o link foi gerado pela ferramenta que é a página da web de phishing do Instagram. Envie este link para a vítima. Assim que ele/ela abrir o link, ele/ela obterá uma página da web original do Instagram e assim que ele/ela preencher os detalhes na página da web. Ele será destacado no terminal do Socialphish.

Você pode ver aqui que preenchemos o formulário de login, demos o nome de usuário como geeky e a senha como geekygeeky agora, assim que a vítima clicar em login, todos os detalhes serão mostrados no terminal do Socialphish.

Você pode ver que as credenciais foram encontradas. Até você pode executar este ataque usando você mesmo em seu alvo.

## PhishMailer
PhishMailer é outra poderosa ferramenta de phishing open-sourse extremamente popular hoje em dia. Mais fácil do que o Social Engineering Toolkit ele contém alguns modelos de páginas web para 10 sites populares, como Facebook, Instagram, Google, Snapchat, GitHub, Yahoo, Proton mail, Spotify, Netflix, LinkedIn, WordPress, Origin, Steam, Microsoft, etc.

### Passo-a-Passo
- Mover para a área de trabalho. E use o seguinte comando para instalar o phishmailer e mover para o diretório da ferramenta.

```bash
cd Desktop
git clone https://www.github.com/BiZken/PhishMailer.git
cd PhishMailer/
```

- A ferramenta foi baixada. Agora, para executar a ferramenta, use o seguinte comando.

```bash
python3 PhishMailer.py
```
Você pode ver muitas opções aqui, você pode usar todas essas opções para criar e-mails de phishing. Suponha que você queira criar uma página do Instagram, digite a opção 1, se quiser criar uma página de phishing do Facebook, ela gerará o link que você pode enviar para sua vítima. É assim que o PhishMailer funciona.

- Depois de iniciar a ferramenta, preencha os campos desejados conforme preenchemos.

Já que inserimos todos os detalhes, agora abra o link no navegador e você obterá todos os detalhes. O link que inserimos no navegador abriu a página de phishing do Facebook. Depois que ele/ela inseriu o ID do usuário e a senha nos campos.

Aqui obtivemos o ID do usuário e a senha. É assim que você também pode realizar seus experimentos. O PhishMailer contém alguns modelos gerados por outra ferramenta chamada PhishMailer. O PhishMailer oferece páginas da web de modelos de phishing para 10 sites populares, como Facebook, Instagram, Google, Snapchat, GitHub, Yahoo, Proton Mail, Spotify, Netflix, LinkedIn, WordPress, Origin, Steam, Microsoft, etc. O PhishMailer também oferece uma opção para usar um modelo personalizado se alguém quiser.

## Conclusão

Existem inúmeras formas de criar um *phishing attack* utilizando-se de bibliotecas em python e/ou em bash. Na literatura internacional, ou melhor, na comunidade de tecnologia internacional a riqueza de ferramentas é imensurável, mas a qualidade da estruturação e proteção dos dados de quem as executa permanece questionável. Tais orientações mostram-se incipientes na documentação destas ferramentas.

## Bibliografia
1. IBM. Phishing. Disponível em: <https://www.ibm.com/br-pt/topics/phishing>. Acesso em: 18 dez. 2024.
2. Socialphish Phishing Tool in Kali Linux. GeeksforGeeks, 24 abr. 2021. Disponível em: <https://www.geeksforgeeks.org/socialphish-phishing-tool-in-kali-linux/>. Acesso em: 18 dez. 2024.
3. PhishMailer – Generate Professional Phishing Alert Templates in Kali Linux. GeeksforGeeks, 21 maio 2021. Disponível em: <https://www.geeksforgeeks.org/phishmailer-generate-professional-phishing-alert-templates-in-kali-linux/>. Acesso em: 18 dez. 2024.
4. Rayhan, Abu & Kinzler, Robert & Rayhan, Rajan. (2023). Cybersecurity Best Practices for Python Web Applications. 10.13140/RG.2.2.29658.11202. 
