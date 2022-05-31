from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text
import emoji

bot = Bot(token='Oops! That is secret!')
dp = Dispatcher(bot)

# MENU INICIAL -------------------------------------------------------------------------------------------------------
button1 = KeyboardButton(emoji.emojize('Redes sociais'))
button2 = KeyboardButton(emoji.emojize('Produtos'))
button3 = KeyboardButton(emoji.emojize('Conecte-se'))

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3)

# REDES SOCIAIS ------------------------------------------------------------------------------------------------------
youtube = text(emoji.emojize('🎬 YouTube ✨'))
button4 = InlineKeyboardButton(text=youtube, url="https://www.youtube.com/channel/UC15lNALBGkXBEv3_tQ3QQOA")

pinterest = text(emoji.emojize('📰 Pinterest ✨'))
button5 = InlineKeyboardButton(text=pinterest, url="https://br.pinterest.com/resilienciaestudos/_saved/")

twitter = text(emoji.emojize('💡 Twitter ✨'))
button6 = InlineKeyboardButton(text=twitter, url="https://twitter.com/resiliencia_est")

keyboard_inlineReply1 = InlineKeyboardMarkup().add(button4).add(button5).add(button6)

# PRODUTOS -----------------------------------------------------------------------------------------------------------
redacao = text(emoji.emojize('📓 Redação ✨'))
buttonR = InlineKeyboardButton(text=redacao, callback_data='redacao')

gabaritos = text(emoji.emojize('📑 Gabaritos ✨'))
buttonG = InlineKeyboardButton(text=gabaritos, callback_data='gabaritos')

free_content = text(emoji.emojize('✏️ Conteúdo Gratuito ✨'))
buttonF = InlineKeyboardButton(text=free_content, callback_data='free_content')

keyboard_PRODUCTS = InlineKeyboardMarkup().add(buttonR).add(buttonG).add(buttonF)

# ------------------ REDAÇÃO ---------------------------------------------------------------------------------------------

politica = text(emoji.emojize('🗳️ Política ✨'))
buttonP = InlineKeyboardButton(text=politica, url="https://cutt.ly/wJgGa5K")

sociologia = text(emoji.emojize('🤼 Sociologia ✨'))
buttonS = InlineKeyboardButton(text=sociologia, url="https://cutt.ly/CJgGgbn")

religiao = text(emoji.emojize('🕊️ Religião ✨'))
buttonR = InlineKeyboardButton(text=religiao, url="https://cutt.ly/eJgGhCG")

filosofia = text(emoji.emojize('💡 Filosofia ✨'))
buttonF = InlineKeyboardButton(text=filosofia, url="https://cutt.ly/6JgGktJ")

keyboard_REDACAO = InlineKeyboardMarkup().add(buttonP).add(buttonS).add(buttonR).add(buttonF)

reply_maconha = text(emoji.emojize("""Calma que aqui o ponto não sobre certo ou errado, mas sobre economia e ciência
                                   \n Deixei até o link do preview pra você dar uma olhadinha e ver 🥰✨"""))

maconha = text(emoji.emojize('🌿 Criminalização da Maconha ✨'))
buttonM = InlineKeyboardButton(text=maconha, url="https://cutt.ly/nJgGdJe")

previewM = text(emoji.emojize('📼 Preview ✨'))
previewM = InlineKeyboardButton(text=previewM, url="https://www.youtube.com/watch?v=Huc8q-IdqZI")

keyboard_MACONHA = InlineKeyboardMarkup().add(buttonM).add(previewM)

# ------------------ GABARITO COMENTADO -------------------------------------------------------------------------------

gabarito01 = text(emoji.emojize('📐 Matemática 1977 - 1999 ✨'))
button13 = InlineKeyboardButton(text=gabarito01, url="https://cutt.ly/lJa1Bbz")
 
gabarito02 = text(emoji.emojize('📐 Matemática 2000 - 2022 ✨'))
button14 = InlineKeyboardButton(text=gabarito02, url="https://cutt.ly/lJgFAiw")
   
gabarito03 = text(emoji.emojize('🚀 Física 1977 - 1999 ✨'))
button15 = InlineKeyboardButton(text=gabarito03, url="https://cutt.ly/dJgFDgv")

keyboard_gabaritos = InlineKeyboardMarkup().add(button13).add(button14).add(button15)

# ------------------ CONTEÚDO GRATUITO -------------------------------------------------------------------------------


# LOJA ---------------------------------------------------------------------------------------------------------------
re = text(emoji.emojize('🧠 Resiliência Estudos ✨'))
site = InlineKeyboardButton(text=re, url="https://sites.google.com/view/resilincia-estudos/home")

keyboard_inlineReply2 = InlineKeyboardMarkup().add(site)

# CONECTE-SE ---------------------------------------------------------------------------------------------------------
telegramGroupGeral = text(emoji.emojize('🦾 Grupo do Telegram ✨'))
button10 = InlineKeyboardButton(text=telegramGroupGeral, url="https://t.me/+c1rCZtdEYig0Mjlh")

keyboard_inlineReply3 = InlineKeyboardMarkup().add(button10)

# FUNÇÕES ------------------------------------------------------------------------------------------------------------
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
 await message.reply("Olá! sou o bot do Resiliência Estudos. No que posso ajudar?", reply_markup=keyboard1)

@dp.message_handler()
async def kb_answer(message: types.Message):
  
 # REDES SOCIAIS -----------------------------------------------------------------------------------------------------
 if message.text == 'Redes sociais':
  reply01 = text(emoji.emojize("""🥰 Escolha qual(is) você deseja seguir ✨"""))
  await message.reply(reply01, reply_markup=keyboard_inlineReply1, parse_mode=ParseMode.MARKDOWN)
 
 # PRODUTOS ----------------------------------------------------------------------------------------------------------
 elif message.text == 'Produtos':
  reply02 = text(emoji.emojize("""Não se esqueça de conferir a loja online também! 😍✨"""))
   
  await  message.reply(reply02, reply_markup=keyboard_inlineReply2, parse_mode=ParseMode.MARKDOWN)
  await  message.reply("Escolha uma categoria",reply_markup = keyboard_PRODUCTS)
    
 # CONECTE-SE --------------------------------------------------------------------------------------------------------
 elif message.text == 'Conecte-se':
   reply03 = text(emoji.emojize("""Adoro gente novaaa 🤩✨"""))
   await message.reply(reply03, reply_markup=keyboard_inlineReply3, parse_mode=ParseMode.MARKDOWN)

@dp.callback_query_handler(text = ['redacao', 'gabaritos', 'gratuito'])
async def products(call: types.CallbackQuery):
  
  if call.data == 'redacao':
    reply_redacao = text(emoji.emojize("""Bora garantir esse notão! 🤩✨"""))
    await call.message.answer(reply_redacao, reply_markup=keyboard_REDACAO, parse_mode=ParseMode.MARKDOWN)
    await call.message.answer(reply_maconha, reply_markup=keyboard_MACONHA, parse_mode=ParseMode.MARKDOWN)
  
  if call.data == 'gabaritos':
    reply_gabaritos = text(emoji.emojize("""Você será redireciondo diretamente para a página de compra, mas se quiser ver os previews de cada material basta visitar o site do cursinho 🥰
                                         \n Adoraria que você desse uma olhadinha 😇
                                         \n Se já tem certeza do que adiquirir, bora garantir essa aprovação! 🤩✨"""))
    await call.message.answer(reply_gabaritos, reply_markup=keyboard_gabaritos, parse_mode=ParseMode.MARKDOWN)
    
executor.start_polling(dp)
