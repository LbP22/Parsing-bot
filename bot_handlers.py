from emoji import emojize
from bot import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_config import admin_id, Search


async def start_notification(dp):
    text = 'Я проснулся :sleepy:'
    await bot.send_message(admin_id[0], emojize(text, True))


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет! Для начала работы напиши: /search')


@dp.message_handler(commands=['help'])
async def help_com(message: types.Message):
    await message.answer('Пока что не могу ничем тебе помочь. Придётся ждать. Прости')


@dp.message_handler(commands=['search'])
async def search(message: types.Message):
    b_design = types.KeyboardButton('Дизайн')
    b_program = types.KeyboardButton('Программирование')
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b_design, b_program)
    await message.answer('Что тебя интересует?', reply_markup=kb)
    await Search.object.set()


@dp.message_handler(state=object)
async def search(message: types.Message, state: FSMContext):
    answer = message.text
    b_design = types.KeyboardButton('Дизайн')
    b_program = types.KeyboardButton('Программирование')
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b_design, b_program)
    await message.answer(emojize('Принял :ok_hand:\nТеперь выбери подкатегории'), reply_markup=kb)
    await Search.object.set()


@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    user = {}
    if text == 'Дизайнер' and not text.startswith('/'):
        obj = 'design'
        await message.reply('Хорошо, идём дальше')
