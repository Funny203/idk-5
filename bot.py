import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, '''Привет! Я бот, который рассказывает советы по экологии\n\n
        Мои команды: \n\n
        /sort  <наименования мусора для утилизации>\n
        /time  <наименование предмета>
        /how many <наименование количество токсичных выбросов за год предметом>
        '''
        )

@bot.message_handler(commands=['sort'])
def sort_item(message):
    key = telebot.util.extract_arguments(message.text).lower()
    list_utils = [
        'телевизор',
        'батарейки', 
        'пылесос', 
        'бытовая техника', 
        'шины', 
        'аккамуляторы', 
        'нефтепродукты', 
        'градусники', 
        'мед.отходы'
        ]
    if key in list_utils:
        bot.send_message(message.chat.id, f'{key} необходимо отдавать на переработку')
    else:
         bot.send_message(message.chat.id, f'{key} не является опасным отходом')


@bot.message_handler(commands=['time'])
def time_item(message):
    key = telebot.util.extract_arguments(message.text).lower()
    decompose_items = {
        'пластиковая бутылка': '450 лет',
        'стеклянная бутылка': '1-2 миллиона лет',
        'бумага': '2-5 лет',
        'картон': '1-3 года',
        'книга': '50-100 лет',
        'журнал': '10-50 лет',
        'резиновая покрышка': '50-80 лет',
        'батарейки': '1-5 лет',
        'аккумуляторы': '5-10 лет',
        'телевизор': '100-500 лет',
        'пылесос': '100-500 лет',
        'нефтепродукты': '100-500 лет',
        'градусник': '100-500 лет',
        'медицинские отходы': '100-500 лет',
        'банановая кожура': '2-5 недель',
        'полиэтиленовый пакет': '10-20 дет'
    }
    if key in decompose_items:
        bot.send_message(message.chat.id, f'Время разложения {key}: {decompose_items[key]}')
    else:
        bot.send_message(message.chat.id, f'Время разложения {key} неизвестно')
        

@bot.message_handler(commands=['how many'])
def time_item(message):
    key = telebot.util.extract_arguments(message.text).lower()
    toxic_emissions = {
        'машина': '800кг. окиси углерода, 40кг окиси азота, 200кг углеродов',
        'промышленные мероприятия': 'более 100 тонн оксида углерода и около 10 тонн окиси азота',
        'поезд': 'около 760 тонн окиси углерода'
    }
    if key in toxic_emissions:
        bot.send_message(message.chat.id, f'Кличество выбросов за год {key}: {toxic_emissions[key]}')
    else:
        bot.send_message(message.chat.id, f'Кличество выбросов за год {key} неизвестно')


                       

bot.infinity_polling()