import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

RESPOSTA_1, RESPOSTA_2 = range(2)

def start(update, context):
    reply_keyboard = [['1', '2', '3','4']]
    update.message.reply_text(
        ('Olá! Seja bem vindo ao atendimento virtual do Banco Carrefour!\n\n '
        'Caso você queira saber mais sobre o cartão Carrefour, digite 1;\n '
        'Sobre Seguros, digite 2;\n '
        'A respeito dos Serviços oferecidos, digite 3;\n '
        'Mas se quiser saber sobre Promoções, digite 4; \n\n'
        'Você pode voltar a qualquer momento para o menu inicial, basta apenas digitar /start.'),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return RESPOSTA_1

def pergunta_1(update, context):
    text = update.message.text
    context.user_data['pergunta_1'] = text

    if text == '1':
        resposta =  ('O cartão de crédito Carrefour é aceito em todos os locais credenciados Visa e Mastercard, dentrou ou fora do país. Tendo como benefícios exclusivos: \n\n'+
                    'Produtos com descontos exclusivos nas Lojas Carrefour e no site; \n Produtos sinalizados com o selo de primeira parcela paga; \n'+
                    'Produtos sinalizados nas Lojas Carrefour ou no site podem ser parcelados em até 24x sem juros;\n'+
                    'Parcelamento em até 10x sem juros nas Drogarias Carrefour; \n Prazo maior para pagar o combustível nos postos Carrefour;\n\n'+
                    'Se quiser saber sobre as Vantagens do cartão Carrefour, por favor digite 1\n'+
                    'Se quiser pedir seu cartão Carrefour, digite 2 \n'+
                    'Para desbloquear seu cartão digite 3 \n'+
                    'Para saber onde baixar o aplicativo Carrefour digite 4 \n')
        reply_keyboard = [['1', '2', '3', '4']]
    elif text == '2':
        resposta = ('Os seguros do Cartão Carrefour são os seguintes: \n\n'+
                    '1. Proteção Hospitalar; \n 2. Sorte Grande; \n 3. Proteção Dental; \n 4. Seguro Premiado; \n'+ 
                    '5. Lar Seguro; \n 6. Parcele Fácil; \n 7. Crédito Pessoal; \n 8. Fatura Premiada; \n\n'+
                    'Sobre qual assunto sua dúvida advém? Digite o número para facilitarmos! \n')
        reply_keyboard = [['1', '2', '3', '4', '5', '6', '7', '8']]
    elif text == '3':
        resposta = ('Os serviços do Cartão Carrefour são: \n\n 1. Parcele Fácil; \n 2. Crédito Pessoal; \n 3. PagContas; \n 4. Saque Rápido; \n'+
        '5. SMS Controle Total; \n 6. Parcela Pronta; \n\n'+
        'Sobre qual assunto sua dúvida advém? Digite o número para facilitarmos! \n')
        reply_keyboard = [['1', '2', '3', '4', '5', '6']]
    elif text == '4':
        resposta = ('Para participar é fácil! A cada R$ 10,00 em compras com o cartão carrefour, você ganha um número da sorte! \n\n'
                    'Aumente suas chances comprando no Carrefour e ganhando números da sorte em dobro OU contratando um seguro no cartão'
                    'e assim ganhando mais um número da sorte!\n\n''São sorteados 8 prêmios de 50 mil reais em barras de ouro pela'
                    'Loteria Federal ao final da Promoção, e 200 valos compras de R$ 250,00 reais (que você pode ganhar na raspadinha'
                    'virtual)!\n\n''Como participar da raspadinha virtual? Basta seguir os passos abaixo:\n\n 1. Acesse "vernúmeros da sorte"'
                    'com seu CPF  e data de nascimento. \n 2. Clique em "raspar agora" e veja se tem jogadas disponíveis. \n 3. Aí é só'
                    'raspar e torcer!\n\n Para saber mais e tirar suas dúvidas, acesse o site do Banco Carrefour, através deste link:'
                    'https://www.carrefoursolucoes.com.br/promocao')

    
    update.message.reply_text(resposta,reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return RESPOSTA_2

def pergunta_2(update, context):
    text = update.message.text
    user_data = context.user_data
    escolha = user_data['pergunta_1']

    user_data['pergunta_2'] = text

    if escolha == '1':
        if text == '1':
            resposta = 'As vantagens do Cartão Carrefour são:\n\n Isenção da parcela da anuidade usando pelo menos uma vez por mês, em qualquer Carrefour;\n Controle de transações por SMS, mediante contratação de serviço;\n Até 14 opções de data de vencimento;\n Prazo maior para pagar, utilizando a melhor data de compra;\n Até 04 cartões adicionais gratuitos;\n Saque rápido na Rede 24Horas e Rede Cirrus/Plus; \n Pagamento da fatura em qualquer Banco; \n Limite liberado na hora, ao pagar a fatura nos caixas da Loja Carrefour;\n Contrate o Crédito Pessoal em nossa Central de Relacionamento e tenha dinheiro na sua conta em até 72 horas, consulto condições'
        elif text == '2':
            resposta = '1.Solicite: peça já o seu cartão indo até a Loja Carrefour mais próxima, ou através do site Carrefour Soluções que você pode acessar clicando no link a seguir: https://www.carrefoursolucoes.com.br/ \n 2. Receba seu cartão em casa ou saia com ele direto da loja. Consulte as lojas com esta disponibilidade \n 3. Desbloqueie através dos canais Carrefour disponibilizados \n 4. Aproveite usando o cartão e assim tendo acesso a benefícios e serviços exclusivos para você! \n'
        elif text == '3':
            resposta = 'Você pode desbloquear seu cartão através de: \n\n 1. Terminais de Serviço (TAS): presentes em todas as lojas Carrefour; \n 2. Central de Atendimento: para regiões metropolitanas ligue 4004 6200, e para demais regiões, ligue 0800 709 6200 \n 3. App Cartão Carrefour: baixe o aplicativo e aproveite as facilidades!\n '
        elif text == '4':
            resposta = 'Através do aplicativo você pode consultar suas compras, limites, os melhores dias para realizar suas compras e acessar sua fatura. Disponível na Google Play (https://play.google.com/store/apps/details?id=br.com.carrefour.cartaocarrefour) e App Store (https://apps.apple.com/br/app/cart%C3%A3o-carrefour/id1156553924) \n'
    elif escolha == '2':
        if text == '1':
            resposta = 'Você não precisa esperar os problemas de saúde acontecerem para se proteger. Ao adquirir o Proteção Hospitalar pelo seu Cartão Carrefour, você garante dinheiro no bolso enquanto estiver hospitalizado.\n\n Em caso de internação (por acidente ou doença) você recebe diárias de até R$ 300 por internação hospitalar. Independente de você ter ou não plano de saúde, o dinheiro da indenização é pago diretamente a você. \n\n O Proteção Hospitalar inclui ainda uma Assistência Funeral, com prestação de serviços de até R$ 3.300. Por mais R$ 1,00, estenda a cobertura para toda sua família. \n\n Caso queira saber mais sobre os planos disponíveis e seu valor, acesse o site através deste link: https://www.carrefoursolucoes.com.br/web/guest/seguros/hospitalar'
        elif text == '2':
            resposta = 'Não é todo mundo que gosta de pensar nisso, mas planejamento pode ser a segurança da sua família em momentos difíceis. O nosso auxílio funeral traz essa tranquilidade com a garantia da cobertura de despesas em caso de morte acidental do titular. Para saber mais acesse este link que te levará direto à página sobre este tópico: https://www.carrefoursolucoes.com.br/web/guest/seguros/sorte-grande'
        elif text == '3':
            resposta = 'O Proteção Dental Carrefour é a assistência odontológica que os seus dentes precisam. Os nossos serviços incluem emergências, limpezas, extrações, restaurações, raios-x, tratamentos de canal, tratamentos de gengiva e até instalação de aparelhos ortodônticos. Para saber mais, acesse o link que o direcionará à página: https://www.carrefoursolucoes.com.br/web/guest/seguros/dental'
        elif text == '4':
            resposta = 'Com o Seguraço Premiado você garante a segurança do seu Cartão Carrefour e evita despesas feitas indevidamente, como saque e compras sob coação e roubo em caixa eletrônico. Em todos esses casos, garantimos o pagamento das suas perdas. \n Se você sofrer roubo ou furto qualificado de bolsa ou carteira, que contenha o cartão segurado, além dos pagamento das suas despesas, oferecemos também assistência com suporte com táxi até a sua residência ou até a delegacia; o cancelamento e remissão dos cartões roubados ou furtados; e a notificação de perda, roubo ou furto do seu aparelho celular. \n Para saber mais, acesse o link que o levará diretamente à página: https://www.carrefoursolucoes.com.br/web/guest/seguros/seguraco-premiado'
        elif text == '5':
            resposta = 'Lar Seguro é o seguro que ajuda você a resolver danos e imprevistos em sua casa ou apartamento. Com ele, sua residência fica protegida contra diversos riscos, além de estar coberta por assistências que vão tornar sua vida mais prática e tranquila. \n Para contratar o Lar Seguro você não precisa ser dono do imóvel. Basta que seja um imóvel residencial em área urbana, ocupado e construído em alvenaria. E se o imóvel for uma casa, podemos oferecer limpeza de caixa da água com mão de obra especializada. \n Caso deseje contratar mais um Lar Seguro para um imóvel diferente do seu endereço cadastral, você poderá entrar em contato com nossa central de atendimento, ou ir ao Carrefour Hiper mais próximo. Para saber mais sobre este benefício, acesse: https://www.carrefoursolucoes.com.br/web/guest/seguros/lar-seguro '
        elif text == '6':
            resposta = 'Em casos de desemprego involuntário ou de incapacidade física total temporária, o seguro garante o pagamento do saldo devedor* do financiamento da fatura contratado através da adesão ao Parcele Fácil nas situações cobertas abaixo. Confira as coberturas e limites máximos de indenizações abaixo. Consulte Condições Gerais do Seguro Parcele Fácil em www.bnpparibascardif.com. Para mais informações, acesse: https://www.carrefoursolucoes.com.br/web/guest/seguros/parcele-facil1'
        elif text == '7':
            resposta = 'Em casos de desemprego involuntário ou de incapacidade física total temporária, o seguro garante o pagamento do saldo devedor* do empréstimo contratado através da adesão ao Crédito Pessoal nas situações listadas abaixo. Acesse para saber mais: https://www.carrefoursolucoes.com.br/web/guest/seguros/credito-pessoal1'
        elif text == '8':
            resposta = 'O seguro Fatura Premiada é a tranquilidade que faltava pro seu dia. Em casos de desemprego involuntário ou de incapacidade física total e temporária, o seguro garante o pagamento do saldo devedor do seu Cartão Carrefour até o limite de R$ 5.000,00. Além disso, você ainda concorre a R$ 10.000,00 líquido, em sorteios mensais. Para saber mais, acesse: https://www.carrefoursolucoes.com.br/web/guest/fatura-premiada'
    elif escolha == '3':
        if text == '1':
            resposta = 'Ao parcelar a sua fatura, você sabe exatamente quanto vai pagar no próximo mês e por quanto tempo terá que pagar. Assim, fica mais fácil deixar suas contas em dia. \n\n Para parcelamento de fatura e terminal de autoatendimento, siga o seguinte procedimento:\n 1. Escolha uma das 8 opções de parcelamento disponíveis; \n 2. Pague o valor exato da entrada em um banco, lotérica ou em uma de nossas lojas até a data de vencimento; \n 3. Pronto! Parcelamento contratado! \n\n Agora se for através de site ou central de atendimento, siga estas instruções: \n\n 1. Simule a opção de parcelamento ideal para você. Caso as opções predefinidas não atendam a sua necessidade, você pode simular até chegar à melhor opção. \n 2. Confirme a contratação do parcelamento \n 3. Se optar pelo plano com entrada, pague exatamente o valor escolhido em um banco, lotérica ou em nossas lojas até a data de vencimento. \n 4. Pronto! Parcelamento contratado! \n\n Para mais informações, acesse: https://www.carrefoursolucoes.com.br/web/guest/servicos/parcele'
        elif text == '2':
            resposta = 'O crédito pessoal funciona como um empréstimo depositado direto em conta corrente ou poupança. \n\n Se você precisar de uma quantia adicional na hora de pagar as contas vencidas, acertar pendências ou turbinar o seu negócio, o Carrefour Soluções Financeiras facilita a sua vida com o Crédito Pessoal. \n\n Coloque os seus projetos emprática, sem burocracia, com uma das taxas mais competitivas do mercado. E você tem até 24 vezes para pagar o empréstimo. \n\n Entre em contato com a nossa Central de Relacionamento, conheça todas as nossas condições especiais e saiba se você é um cliente pré- aprovado para adquirir o serviço de Crédito Pessoal. \n\n Veja como é fácil ter crédito direto na sua conta:\n 1. Ligue para a central de relacionamento: O telefone é 4004-6200 para regiões metropolitanas ou 0800-709-6200 em demais localidades. O serviço funciona de segunda a sábado, exceto feriados, das 8h às 21h (horário de Brasília). \n 2. Contrate o valor total ou parte do valor: Com os benefícios do cartão de crédito Carrefour, você pode parcelar o valor contratado em até 24 vezes. \n 3. O dinheiro é depositado na sua conta: O crédito é depositado na sua conta corrente ou poupança em até 72 horas úteis. \n 4. Crédito pessoal contratado com sucesso! O valor da sua parcela é lançado todo mês na fatura do seu Cartão de crédito Carrefour.\n\n Para saber mais, acesse: https://www.carrefoursolucoes.com.br/credito-pessoal'
        elif text == '3':
            resposta = 'Com o cartão de crédito Carrefour, você pode pagar diversos tipos de contas em uma única data de vencimento. Como contas de água, luz, gás e de telefone.\n\n Para mais informações, acesse: https://www.carrefoursolucoes.com.br/servicos/pag-contas'
        elif text == '4':
            resposta = 'Com o cartão de crédito Carrefour, você aproveita da comodidade de sacar dinheiro em caixas eletrônicos da rede Banco 24 Horas, com condições especiais de pagamento. \n\n Saque dinheiro à vista a qualquer hora e tenha um prazo maior para pagar. \n\n Parcele o pagamento do seu saque em até 24 vezes e pague a primeira parcela em até 70 dias. \n\n Confira as Condições para este serviço: \n 1. O limite de saque está condicionado à análise de crédito e ao limite de compras disponível no cartão. \n 2. Os saques estão disponíveis no Brasil ou no exterior. As operações no exterior, para clientes MasterCard ocorre via Rede Cirrus e, para clientes Visa, com a Rede Plus. \n\n Para mais informações, acesse: https://www.carrefoursolucoes.com.br/servicos/saque-rapido'
        elif text == '5':
            resposta = 'Acompanhe a movimentação do seu cartão de crédito Carrefour, ao receber um SMS, no seu celular, a cada transação efetuada. Assim, você tem segurança e controle de suas compras e dos seus adicionais.\n\n Quais as vantagens do SMS controle? om este serviço, você recebe mensagens com as principais informações sobre:\n 1. Seus gastos: Transações de compras aprovadas em território nacional. \n 2. Saques em dinheiro: Valor, hora e local que a transação foi realizada. \n 3. PagContas: Transações de pagamentos efetuados. \n 4. Fechamento e pagamento de fatura: Informativo com o valor e data de vencimento da fatura, além da confirmação da efetivação do pagamento.\n\n Onde contratar? Para começar a receber mensagens via SMS, basta cadastrar o número do seu telefone celular e contratar o serviço:\n 1. Site: Após o login, vá até a página do SMS Controle Total e cadastre seu celular. \n 2. Lojas Carrefour: Solicite para o atendente do Cartão Carrefour a efetivação do seu cadastro. \n 3. Atendimento: Ligue na Central de Atendimento e solicite a adesão ao serviço. Selecione o telefone certo para sua necessidade, para saber, basta acessar este link que irá direcioná-lo à página com os telefones das centrais de atendimento:https://www.carrefoursolucoes.com.br/central-telefonica \n 4. Terminal de Autoatendimento: Vá até um terminal e tenha acesso o serviço, cadastrando o seu celular. \n\n Para mais informações, acesse: https://www.carrefoursolucoes.com.br/sms-controle-total '
        elif text == '6':
            resposta = 'Com as novas regras do Conselho Monetário Nacional (Resolução nº 4.549/2017), ao optar pelo pagamento mínimo da fatura, você poderá financiar o saldo pelo crédito rotativo por apenas um mês. Na fatura seguinte, você deverá pagar o que sobrou da fatura anterior ou optar por uma das modalidades de parcelamento ofertadas com juros reduzidos. Para saber mais e tirar possíveis dúvidas, acesse: https://www.carrefoursolucoes.com.br/parcela-pronta'
    
    update.message.reply_text(resposta,reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text('Espero que suas dúvidas estejam claras',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def main():
    updater = Updater("TOKEN", use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            RESPOSTA_1: [MessageHandler(Filters.regex('[1-3]'), pergunta_1)],

            RESPOSTA_2: [MessageHandler(Filters.regex('[1-8]'), pergunta_2)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()