from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text
import emoji

bot = Bot(token='5379019831:AAGMS6fhq48vEpydXIdcCtTP67DJ9hI662U')
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
button7 = KeyboardButton(emoji.emojize('Redação'))

# ------------------ GABARITO COMENTADO
button8 = KeyboardButton(emoji.emojize('Gabaritos'))

gabarito01 = text(emoji.emojize('📐 Matemática 1977 - 1999 ✨'))
button13 = InlineKeyboardButton(text=gabarito01, url="https://cutt.ly/lJa1Bbz")
 
gabarito02 = text(emoji.emojize('📐 Matemática 2000 - 2022 ✨'))
button14 = InlineKeyboardButton(text=gabarito02, url="")
   
gabarito03 = text(emoji.emojize('🚀 Física 1977 - 1999 ✨'))
button15 = InlineKeyboardButton(text=gabarito03, url="")

keyboard_PRODUCTS = InlineKeyboardMarkup().add(button13)

# ------------------ CONTEÚDO GRATUITO
button11 = KeyboardButton(emoji.emojize('Conteúdo Gratuito'))

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button7).add(button8).add(button11)

# LOJA ---------------------------------------------------------------------------------------------------------------
re = text(emoji.emojize('🧠 Resiliência Estudos ✨'))
button9 = InlineKeyboardButton(text=re, url="https://sites.google.com/view/resilincia-estudos/home")

keyboard_inlineReply2 = InlineKeyboardMarkup().add(button9)

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
  await  message.reply("Escolha uma categoria",reply_markup = keyboard2)
  
  if message.text == 'Gabaritos':
    await  message.reply("BORA", reply_markup=keyboard_PRODUCTS, parse_mode=ParseMode.MARKDOWN)
  
 # CONECTE-SE --------------------------------------------------------------------------------------------------------
 elif message.text == 'Conecte-se':
   reply03 = text(emoji.emojize("""Adoro gente novaaa 🤩✨"""))
   await message.reply(reply03, reply_markup=keyboard_inlineReply3, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler()
async def sub_answer(mess: types.Message):
  if mess.text == 'Redação':
    redacao = text(emoji.emojize('📝 Redação ✨'))
    button12 = InlineKeyboardButton(text=redacao, url="")
    
    # GABARITOS ------------------------------
  elif mess.text == 'Gabaritos':     
    reply05 = text(emoji.emojize("""Bora garantir essa aprovação!!"""));
    await  mess.reply(reply05, reply_markup=keyboard_PRODUCTS, parse_mode=ParseMode.MARKDOWN)
 
executor.start_polling(dp)