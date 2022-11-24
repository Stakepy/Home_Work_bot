import telebot
from telebot import types

bot = telebot.TeleBot('2026610191:AAFKojnzwct6u-FVSLTpSMxp7qk9UZLwvUU')

@bot.message_handler(commands=['help', 'start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Домашнє завдання 📖')
    item5 = types.KeyboardButton('Домашнє завдання на завтра 🏠')
    item2 = types.KeyboardButton('Розклад уроків 📝')
    item3 = types.KeyboardButton('Розклад дзвінків 🛎️')
    item4 = types.KeyboardButton('Фото щоденника 📙')
    item7 = types.KeyboardButton('⚠Питання')
    item33 = types.KeyboardButton('Книжки 📚')
    item6 = types.KeyboardButton('/start')
    markup.add(item1, item5, item2, item3, item4, item6, item33, item7 )


    bot.send_message(message.chat.id,
                     'Привіт, {0.first_name}!'.format(message.from_user), reply_markup = markup)

    @bot.message_handler(content_types=['text'])
    def bot_message(message):
        if message.chat.type == 'private':
            if message.text == 'Домашнє завдання 📖' :
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item8 = types.KeyboardButton('понеділок')
                item9 = types.KeyboardButton('вівторок')
                item10 = types.KeyboardButton('середа')
                item11 = types.KeyboardButton('четвер')
                item12 = types.KeyboardButton('п`ятниця')
                back1 = types.KeyboardButton('⬅️назад')
                markup.add(item8, item9, item10, item11, item12, back1)
                bot.send_message(message.chat.id, 'Домашнє завдання 📖', reply_markup=markup)
            elif message.text == 'понеділок':
                    bot.send_message(message.chat.id,
                                 '\n1.Геометрія : '
                                 '\n2.Право : '
                                 '\n3.Фіз-ра '
                                 '\n4.Фізика : '
                                 '\n5.Зарубіжна література : '
                                 '\n6.Англійська мова : '
                                 '\n7. -  '
                                 '\n8. -  ')
            elif message.text == 'вівторок':
                bot.send_message(message.chat.id,
                                 '\n1. -  '
                                 '\n2.Геометрія : '
                                 '\n3.Алгебра : '
                                 '\n4.Біологія : '
                                 '\n5.Укр.Літ : '
                                 '\n6.Англійська : '
                                 '\n7.Інформатика(1группа) : '
                                 '\n8.Історія України : ')

            elif message.text == 'середа':
                bot.send_message(message.chat.id,
                                 '\n1. -  '
                                 '\n2.Зарубіжна література : '
                                 '\n3.Фіз-ра '
                                 '\n4.Укр.Літ : '
                                 '\n5.Фізика : '
                                 '\n6.Всесвітня Історія : '
                                 '\n7.Інформатика : '
                                 '\n8.Онови здоров : ')
            elif message.text == 'четвер':
                bot.send_message(message.chat.id,
                                 '\n1.Хімія : '
                                 '\n2.Мистецтво : '
                                 '\n3.Праця '
                                 '\n4.Українська мова(1группа) : '
                                 '\n5.Фізика : '
                                 '\n6.Історія: '
                                 '\n7.Хімія : '
                                 '\n8. -  ')
            elif message.text == 'п`ятниця':
                bot.send_message(message.chat.id,
                                 '\n1.Алгебра : '
                                 '\n2.Алгебра : '
                                 '\n3.Українська мова(1группа) : '
                                 '\n4.Географія : '
                                 '\n5.Фіз-ра '
                                 '\n6.Біологія : '
                                 '\n7.Англійська мова : '
                                 '\n8. -  ')
            elif message.text == '⬅️назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Домашнє завдання 📖')
                item5 = types.KeyboardButton('Домашнє завдання на завтра 🏠')
                item2 = types.KeyboardButton('Розклад уроків 📝')
                item3 = types.KeyboardButton('Розклад дзвінків 🛎️')
                item4 = types.KeyboardButton('Фото дневника 📙')
                item7 = types.KeyboardButton('⚠Питання')
                item33 = types.KeyboardButton('Книжки 📚')
                item6 = types.KeyboardButton('/start')
                markup.add(item1, item5, item2, item3, item4, item6, item33, item7)
                bot.send_message(message.chat.id, '⬅️Назад', reply_markup=markup)
            elif message.text == 'Домашнє завдання на завтра 🏠':
                bot.send_message(message.chat.id, '\n \n \n \n ')
            elif message.text == 'Фото щоденника 📙':
                bot.send_message(message.chat.id, 'Фото щоденника 📙')
                p = open("h.jpg", 'rb')
                bot.send_photo(message.chat.id, p )
            elif message.text == 'Розклад дзвінків 🛎️':
                bot.send_message(message.chat.id, '\n1) 8.30-9.15         \n2) 9.30-10.15        \n3) 10.30-11.15         \n4) 11.30-12.15           \n5) 12.30 -13.15          \n6) 13.30-14.15         \n7) 14.30-15.05        \n8) 15.10-15.55')
            elif message.text == '⚠Питання':
                bot.send_message(message.chat.id, '\n Тут зібрані питання які можуть виникнути під час використання бота \n1.Пункт "Домашнє завдання 📖" - там я пишу домашнє завдання по днях тижня(Наприклад: Сьогодні понеділок, і я пишу те, що задали саме в цей день в пункті " понеділок" \n2.Фото щоденника 📙 - оновлюється щоразу наприкінці тижня \n3.З приводу "Чому бот не працює?", справа в тому що Сервера де працює бот переодично відключаються і невідомо коли вони можуть відключитися, і через це потрібно перезапускати бота щоб він знову працював \n4."Коли можна дізнатися дз?" - дз можна дізнатися о 18:00 \nНа цьому начебто все, якщо щось упустив то можна написати мені в Viber 😉 ')
            elif message.text == 'Розклад уроків 📝':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton('Понеділок')
                item4 = types.KeyboardButton('Вівторок')
                item5 = types.KeyboardButton('Середа')
                item6 = types.KeyboardButton('Четвер')
                item7 = types.KeyboardButton('Пятниця')
                back = types.KeyboardButton('⬅️Назад')
                markup.add(item3, item4, item5, item6, item7, back)
                bot.send_message(message.chat.id, 'Розклад уроків 📝', reply_markup = markup )
            elif message.text == 'Понеділок':
                bot.send_message(message.chat.id,
                                 '\n1.Геометрія (№27, 3 поверх)  '
                                 '\n2.Право (№36, 3 поверх)  '
                                 '\n3.Фіз-ра  '
                                 '\n4.Фізика (№29, 3 поверх)  '
                                 '\n5.Зарубіжна література (№32, 3 поверх)  '
                                 '\n6.Англійська мова (№38, 3 поверх)  '
                                 '\n7. -  '
                                 '\n8. -  ')
            elif message.text == 'Вівторок':
                bot.send_message(message.chat.id,
                                 '\n1. -  '
                                 '\n2.Геометрія (№27, 3 поверх)  '
                                 '\n3.Геометрія/Алгебра (№32, 3 поверх)  '
                                 '\n4.Біологія (№38, 3 поверх)  '
                                 '\n5.Укр.Літ (№38, 3 поверх)  '
                                 '\n6.Англійська мова (№28, 3 поверх)  '
                                 '\n7.Інформатика (№21, 2 поверх - №23, 2 поверх)  '
                                 '\n8.Історія (№33, 3 поверх)  ')

            elif message.text == 'Середа':
                bot.send_message(message.chat.id,
                                 '\n1. -  '
                                 '\n2.Зарубіжна література (№01)  '
                                 '\n3.Фіз-ра  '
                                 '\n4.Укр.Літ (№36, 3 поверх)  '
                                 '\n5.Фізика (№35, 3 поверх)  '
                                 '\n6.Історія (№33, 3 поверх)  '
                                 '\n7.Інформатика (№21, 2 поверх - №23, 2 поверх)  '
                                 '\n8.Онови здоров (№27, 3 поверх)  ')
            elif message.text == 'Четвер':
                bot.send_message(message.chat.id,
                                 '\n1.Хімія (№38, 3 поверх)  '
                                 '\n2.Мистецтво (№33, 3 поверх)  '
                                 '\n3.Праця (№01 - №02)  '
                                 '\n4.Українська мова (№28, 3 поверх - №32, 3 поверх)  '
                                 '\n5.Фізика (№20, 2 поверх)  '
                                 '\n6.Історія/Географія (№35, 3 поверх)  '
                                 '\n7.Хімія (№35, 3 поверх)  '
                                 '\n8. -  ')
            elif message.text == 'Пятниця':
                bot.send_message(message.chat.id,
                                 '\n1.Алгебра (№38, 3 поверх)  '
                                 '\n2.Алгебра (№21, 2 поверх)  '
                                 '\n3.Українська мова (№26, 2 поверх - №39, 3 поверх)  '
                                 '\n4.Географія (№32, 3 поверх)  '
                                 '\n5.Фіз-ра  '
                                 '\n6.Біологія (№23, 2 поверх)  '
                                 '\n7.Англійська мова (№33, 3 поверх)  '
                                 '\n8. -  ')
            elif message.text == '⬅️Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Домашнє завдання 📖')
                item5 = types.KeyboardButton('Домашнє завдання на завтра 🏠')
                item2 = types.KeyboardButton('Розклад уроків 📝')
                item3 = types.KeyboardButton('Розклад дзвінків 🛎️')
                item4 = types.KeyboardButton('Фото щоденника 📙')
                item7 = types.KeyboardButton('⚠Питання')
                item33 = types.KeyboardButton('Книжки 📚')
                item6 = types.KeyboardButton('/start')
                markup.add(item1, item5, item2, item3, item4, item6, item33, item7 )
                bot.send_message(message.chat.id, '⬅️Назад' , reply_markup = markup)

            if message.text == 'Книжки 📚':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item8 = types.KeyboardButton('1')
                    item9 = types.KeyboardButton('2')
                    item10 = types.KeyboardButton('3')
                    item11 = types.KeyboardButton('4')
                    item12 = types.KeyboardButton('5')
                    back2 = types.KeyboardButton('⬅️  Назад')
                    start2 = types.KeyboardButton('/restart')
                    markup.add(item8, item9, item10, item11, item12, back2, start2)
                    bot.send_message(message.chat.id, 'Comming soon!', reply_markup=markup)
            elif message.text == '⬅️  Назад':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton('Домашнє завдання 📖')
                    item5 = types.KeyboardButton('Домашнє завдання на завтра 🏠')
                    item2 = types.KeyboardButton('Розклад уроків 📝')
                    item3 = types.KeyboardButton('Рассписание звонков 🛎️')
                    item4 = types.KeyboardButton('Фото щоденника 📙')
                    item7 = types.KeyboardButton('⚠Питання')
                    item33 = types.KeyboardButton('Книжки 📚')
                    item6 = types.KeyboardButton('/start')
                    markup.add(item1, item5, item2, item3, item4, item6, item33, item7)
                    bot.send_message(message.chat.id, '⬅️  Назад', reply_markup=markup)
            elif message.text == '1':
                with open("1.pdf", "rb") as file:
                    f = file.read()
                    bot.send_document(message.chat.id, open(r'1.pdf' , 'rb' ))



bot.polling(none_stop = True)