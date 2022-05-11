from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client 

# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Добро пожаловать! Покажи на что способен твой ум!', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему в личные сообщения!')

# @dp.message_handler(commands=['Функции'])
async def math_open_comand(message : types.Message):
	await bot.send_message(message.from_user.id, 'Я помогаю развить навыки устного счета путем выдачи случайных математических примеров и ведения статистики правильных ответов на них')

# @dp.message_handler(commands=['Виды_примеров'])
async def mathfun_open_comand(message : types.Message):
	await bot.send_message(message.from_user.id, 'Я использую примеры на сложение, умножение, вычитание и деление.')

def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start', 'help'])
	dp.register_message_handler(math_open_comand, commands=['Функции'])
	dp.register_message_handler(mathfun_open_comand, commands=['Виды_примеров'])



