import telebot
from telebot import types

bot = telebot.TeleBot('YOUR TOKEN')

@bot.message_handler(commands=['help', 'start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Домашнее задание 📖')
    item5 = types.KeyboardButton('Домашнее задание на завтра 🏠')
    item2 = types.KeyboardButton('Рассписание уроков и кабинеты 📝')
    item3 = types.KeyboardButton('Рассписание звонков 🛎️')
    item4 = types.KeyboardButton('Фото дневника 📙')
    item7 = types.KeyboardButton('⚠Вопросы')
    item6 = types.KeyboardButton('/start')
    markup.add(item1, item5, item2, item3, item4, item6, item7 )


    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

    @bot.message_handler(content_types=['text'])
    def bot_message(message):
        if message.chat.type == 'private':
            if message.text == 'Домашнее задание 📖' :
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item8 = types.KeyboardButton('понеділок')
                item9 = types.KeyboardButton('вівторок')
                item10 = types.KeyboardButton('середа')
                item11 = types.KeyboardButton('четвер')
                item12 = types.KeyboardButton('п`ятниця')
                back1 = types.KeyboardButton('⬅️назад')
                markup.add(item8, item9, item10, item11, item12, back1)
                bot.send_message(message.chat.id, 'Домашнее задание 📖', reply_markup=markup)
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
                item1 = types.KeyboardButton('Домашнее задание 📖')
                item5 = types.KeyboardButton('Домашнее задание на завтра 🏠')
                item2 = types.KeyboardButton('Рассписание уроков и кабинеты 📝')
                item3 = types.KeyboardButton('Рассписание звонков 🛎️')
                item4 = types.KeyboardButton('Фото дневника 📙')
                item7 = types.KeyboardButton('⚠Вопросы')
                item6 = types.KeyboardButton('/start')
                markup.add(item1, item5, item2, item3, item4, item6, item7)
                bot.send_message(message.chat.id, '⬅️Назад', reply_markup=markup)
            elif message.text == 'Домашнее задание на завтра 🏠':
                bot.send_message(message.chat.id, '\n \n \n \n ')
            elif message.text == 'Фото дневника 📙':
                bot.send_message(message.chat.id, 'Фото дневника 📙')
                p = open("YOUR.jpg", 'rb')
                bot.send_photo(message.chat.id, p )
            elif message.text == 'Рассписание звонков 🛎️':
                bot.send_message(message.chat.id, '\n1) 8.30-9.15         \n2) 9.30-10.15        \n3) 10.30-11.15         \n4) 11.30-12.15           \n5) 12.30 -13.15          \n6) 13.30-14.15         \n7) 14.30-15.05        \n8) 15.10-15.55')
            elif message.text == '⚠Вопросы':
                bot.send_message(message.chat.id, '\n Здесь собраны вопросы которые могут возникнуть во время использования бота \n1.Пункт "Домашнее задание 📖" - там я пишу домашнее задание по дням недели(Например: Сегодня понедельник, и я пишу то что задали именно в в этот день в пункте "понедельник" \n2.Фото дневника 📙 - обновляеться каждый раз в конце недели \n3.По поводу "Почему бот не работает?", дело в том что Сервера где работает бот переодически отключаються и неизвестно когда они могут отключиться , и из-за этого нужно перезапускать бота чтобы он снова работал \n4."Когда можно узнать дз?" - дз можно узнать в 18:00 \nНа этом вроде бы всё, если что-то упустил то можно написать мне в Viber 😉 ')
            elif message.text == 'Рассписание уроков и кабинеты 📝':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton('Понеділок')
                item4 = types.KeyboardButton('Вівторок')
                item5 = types.KeyboardButton('Середа')
                item6 = types.KeyboardButton('Четвер')
                item7 = types.KeyboardButton('Пятниця')
                back = types.KeyboardButton('⬅️Назад')
                markup.add(item3, item4, item5, item6, item7, back)
                bot.send_message(message.chat.id, 'Рассписание уроков и кабинеты 📝', reply_markup = markup )
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
                item1 = types.KeyboardButton('Домашнее задание 📖')
                item5 = types.KeyboardButton('Домашнее задание на завтра 🏠')
                item2 = types.KeyboardButton('Рассписание уроков и кабинеты 📝')
                item3 = types.KeyboardButton('Рассписание звонков 🛎️')
                item4 = types.KeyboardButton('Фото дневника 📙')
                item7 = types.KeyboardButton('⚠Вопросы')
                item6 = types.KeyboardButton('/start')
                markup.add(item1, item5, item2, item3, item4, item6, item7 )

                bot.send_message(message.chat.id, '⬅️Назад' , reply_markup = markup)

bot.polling(none_stop = True)
