import telebot
bot = telebot.TeleBot('')
@bot.message.handler(content_types=['text'])

def Cheapest():
	num_1 = int(input("Введите стоимость первого товара"))
	amount_1 = int(input("Введитель количество первого товара"))
	num_2 = int(input("Введите стоимость второго товара"))
	amount_2 = int(input("Введите количество второго товара"))

	sum_1 = num_1 / amount_1
	sum_2 = num_2 / amount_2

	if sum_1 < sum_2:
		print("Первый товар купить выгоднее")
	elif sum_1 == sum_2:
		print("Стоимость товаров одинаковая")
	else:
		print("Второй товар купить выгоднее")
def get_text_messages(message):
	if message.text == "/start":
		Cheapest()
get_text_messages()
bot.polling(none_stop=True, interval=0)
