import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

#list = ['Вишня', 'Арбуз', 'Жвачка', 'Дыня']
"""
def vib(message):
    markup3 = types.ReplyKeyboardMarkup()
    cherry = types.KeyboardButton('Вишня')
    watermelon = types.KeyboardButton('Арбуз')
    gum = types.KeyboardButton('Жвачка')
    melon = types.KeyboardButton('Дыня')
    markup3.add(cherry, watermelon, gum, melon)
    bot.send_message(message.chat.id, 'ghgf',  reply_markup=markup3)
"""
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b> {message.from_user.last_name} , я продаю жидкости для вейпа, желайшь ли ты преобрести что-то?'
    markup = types.ReplyKeyboardMarkup()
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    we = types.KeyboardButton('О нас')
    markup.add(yes, no, we)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
@bot.message_handler()
def get_text_messages(message):
    if message.text == "Да" or message.text == "да":
        markup1 = types.ReplyKeyboardMarkup()
        husky = types.KeyboardButton('husky')
        hot_spot = types.KeyboardButton('HotSpot')
        xvoa = types.KeyboardButton('ХВОЯ')
        glitch = types.KeyboardButton('Glitch Sauce')
        markup1.add(husky, hot_spot, xvoa, glitch)
        bot.send_message(message.from_user.id, "Отлично, какого производеля хотите жидкость(Выбрать два раза)?", reply_markup=markup1)

    elif message.text == "Нет" or message.text == "нет":
        bot.send_message(message.from_user.id, "Всего хорошего , приходи ещё . Если не сложно расскажи о нас друзьям (t.me/prodagaMaximbot)")

    elif message.text == 'О нас' or message.text == 'о нас':
        bot.send_message(message.chat.id, 'Меня зовут Максим. Я продаю жидкости для вейпов уже год. Имеем быстрых и качественных поставщиков .\n Жижа хорошая и недорогая) ')

    elif message.text == 'husky':
        bot.register_next_step_handler(message, smak)
        photo_husky = open('Huski.jpg', 'rb')
        bot.send_photo(message.chat.id, photo_husky, 'подтвердите выбор:')
        #bot.register_next_step_handler(message, smak)
    elif message.text == 'Вишня':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Арбуз':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Жвачка':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Дыня':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)


    elif message.text == 'HotSpot':
        bot.register_next_step_handler(message, smak)
        photo_husky = open('HotSpot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo_husky, 'подтвердите выбор:')
        # bot.register_next_step_handler(message, smak)
    elif message.text == 'Вишня':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Арбуз':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Жвачка':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Дыня':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)


    elif message.text == 'ХВОЯ':
        bot.register_next_step_handler(message, smak)
        photo_husky = open('XVOA.jpg', 'rb')
        bot.send_photo(message.chat.id, photo_husky, 'подтвердите выбор:')
        # bot.register_next_step_handler(message, smak)
    elif message.text == 'Вишня':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Арбуз':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Жвачка':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Дыня':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)


    elif message.text == 'Glitch Sauce':
        bot.register_next_step_handler(message, smak)
        photo_husky = open('Glitch.jpg', 'rb')
        bot.send_photo(message.chat.id, photo_husky, 'подтвердите выбор:')
        # bot.register_next_step_handler(message, smak)
    elif message.text == 'Вишня':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Арбуз':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Жвачка':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Дыня':
        bot.send_message(message.chat.id, 'Стоимость жижки 17руб, введите количесво')
        bot.register_next_step_handler(message, calc)

def smak(message):
    markup3 = types.ReplyKeyboardMarkup()
    cherry = types.KeyboardButton('Вишня')
    watermelon = types.KeyboardButton('Арбуз')
    gum = types.KeyboardButton('Жвачка')
    melon = types.KeyboardButton('Дыня')
    markup3.add(cherry, watermelon, gum, melon)
    bot.send_message(message.chat.id, 'Выбирайте вкус', reply_markup=markup3)



def calc(message):
    #print(type(message))
    summa = int(message.text)
    azov = 17*summa
    marcup_finish = types.InlineKeyboardMarkup()
    btn_yes = types.InlineKeyboardButton('Да', callback_data= 'furtic')
    btn_no = types.InlineKeyboardButton('Нет', callback_data='nofurtic')
    marcup_finish.add(btn_yes, btn_no)
    bot.send_message(message.chat.id, f'Ваша сумма: {azov}руб , подтвердите заказ ', reply_markup=marcup_finish)
    #bot.register_next_step_handler(message, finsh)



@bot.callback_query_handler(func=lambda call: True)
def callback_func(call):
    if call.message:
        if call.data == 'furtic':
            bot.send_message(call.message.chat.id, 'я отпралю вам данные карты , на которую вы должны оплатить \n 4255190132032098 ,\n 11/25,\n после завершения оплаты с вами свяжется курьер')
        elif call.data == 'nofurtic':
            bot.send_message(call.message.chat.id, ' напишите команду /start, чтобы вернуться к выбору ')
"""
def finsh(message):
    first_name = message.chat.first_name
    user_name = message.chat.username
    admin_id = 961613088
    app_name = []
    app_summa = []
    app_username = []
    app_name.append(first_name)
    app_username.append(user_name)
    app_summa.append()
    bot.send_message(admin_id,f'поступил заказ от {app_name[0]}\n'
                              f'его имя {user_name[0]}\n'
                              f'его заказ {app_summa[0]}')
    app_name.clear()
    app_username.clear()
    app_summa.clear()
    bot.send_message(message.chat.id, 'Заявка отправлена !')
"""




bot.polling(none_stop=True)

