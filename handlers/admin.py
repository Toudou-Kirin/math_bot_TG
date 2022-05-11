from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
import random

class FSMAdmin(StatesGroup):
	end_plus = State()

# @dp.message_handler(commands='Пример', state=None)
c = None
async def start_math_plus(message : types.Message):
	await FSMAdmin.end_plus.set()
	global c
	a = random.randint(0, 50)
	b = random.randint(0, 50)
	c = a + b
	await message.reply('Пример' + str(a) + ' + ' + str(b))

# @dp.message_handler(state=FSMMath.end)
async def load_end_plus(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['end_plus'] = int(message.text)

	async with state.proxy() as data:
		if data['end_plus'] == c:
			await message.reply('Верно!')
		else:
			await message.reply('Неверно!')
	await state.finish()

class FSMAdmins(StatesGroup):
 	end_minus = State()
 	
q = None
async def start_math_minus(message : types.Message):
	await FSMAdmins.end_minus.set()
	global q
	w = random.randint(50, 100)
	e = random.randint(0, 49)
	q = w - e
	await message.reply('Пример: ' + str(w) + ' - ' + str(e))

# @dp.message_handler(state=FSMMath.end)
async def load_end_minus(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['end_minus'] = int(message.text)

	async with state.proxy() as data:	
		if data['end_minus'] == q:
			await message.reply('Верно!')
		else:
			await message.reply('Неверно!')
	await state.finish()

class FSMAdmin2(StatesGroup):
	end_prois = State()	

r = None
async def start_math_prois(message : types.Message):
	await FSMAdmin2.end_prois.set()
	global r
	t = random.randint(0, 10)
	y = random.randint(0, 10)
	r = t * y
	await message.reply('Пример' + str(t) + ' * ' + str(y))

# @dp.message_handler(state=FSMMath.end)
async def load_end_prois(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['end_prois'] = int(message.text)

	async with state.proxy() as data:	
		if data['end_prois'] == r:
			await message.reply('Верно!')
		else:
			await message.reply('Неверно!')
	await state.finish()	

class FSMAdmin3(StatesGroup):
	end_del = State()	

i = None
async def start_math_del(message : types.Message):
	await FSMAdmin3.end_del.set()
	global i
	o = random.randint(10, 100)
	p = random.randint(0, 10)
	i = o / p
	await message.reply('Пример' + str(o) + ' / ' + str(p))

# @dp.message_handler(state=FSMMath.end)
async def load_end_del(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['end_del'] = int(message.text)

	async with state.proxy() as data:	
		if data['end_del'] == int(i):
			await message.reply('Верно!')
		else:
			await message.reply('Неверно!')	
	await state.finish()	


def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(start_math_plus, commands=['ПримерСложение'], state=None)
	dp.register_message_handler(load_end_plus, state=FSMAdmin.end_plus) 
	dp.register_message_handler(start_math_minus, commands=['ПримерВычитание'], state=None)
	dp.register_message_handler(load_end_minus, state=FSMAdmins.end_minus)
	dp.register_message_handler(start_math_prois, commands=['ПримерУмножение'], state=None)
	dp.register_message_handler(load_end_prois, state=FSMAdmin2.end_prois)
	dp.register_message_handler(start_math_del, commands=['ПримерДеление'], state=None)
	dp.register_message_handler(load_end_del, state=FSMAdmin3.end_del)