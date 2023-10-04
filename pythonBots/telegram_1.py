# имя бота coddyMustafo 
# никнейм бота coddyMustafoBot 
# ссылка на бота https://t.me/coddyMustafoBot 
 
# token = "" 
import telebot 
#импортируем из библиотеки time метод sleep 
from time import sleep 
from telebot import types 
import random 
TOKEN = "6592109240:AAHuA_O2jaYHY_4vpymLxoj9Jozz1Gc36po" 
 
#библиотека телебот содержить класс  TeleBot 
 
#обект     = библиотека.класс(свойства) 
mySuperBot = telebot.TeleBot(TOKEN) 
 
#обработчик команды /start 
@mySuperBot.message_handler(commands=['start']) 
def obrabotkaKomandiStart(message): 
     
    #создаем клавиатуру с 2 кнопками 
    raskladka1=types.ReplyKeyboardMarkup(resize_keyboard=True) 
    levoeknopka =types.KeyboardButton('Как дела') 
    pravayaknopka =types.KeyboardButton('Кубик брость?') 
    raskladka1.add(levoeknopka, pravayaknopka) 
    
    # mySuperBot.send_message(комуОтправить, какое собщениеОтправить) 
    mySuperBot.send_message(message.chat.id, "Ассаламу алейкум ва рахматулохи баракату, {0.first_name}. \n Это <b>{1.first_name}</b>. Меня создал <b>Nazarzoda</b>".format(message.from_user, mySuperBot.get_me()), parse_mode='html', reply_markup=raskladka1) 
@mySuperBot.message_handler(content_types=["text"]) 
def lalala(message): 
    if message.chat.type=='private': 
        if message.text=='Как дела': 
            raskladkavibora=types.InlineKeyboardMarkup(row_width=2)
            leftbutton=types.InlineKeyboardButton('Хорошо', callback_data='good')
            Rightbutton=types.InlineKeyboardButton('Не очень', callback_data='bad')
            raskladkavibora.add(leftbutton,Rightbutton)
            mySuperBot.send_message(message.chat.id, 'не жалуюсь Хвала Аллаху. А у тебя? ', reply_markup=raskladkavibora) 
        elif message.text=='Кубик брость?':
            mySuperBot.send_message(message.chat.id,str(random.randint(1,6)))
        
        else: 
            sleep(2)
            mySuperBot.send_chat_action(message.chat.id, "typing")
            otvet1 = "даже не знаю что сказать.." 
            otvet2 = "поговорим об этом позже" 
            otvet3 = "Нормаль говори" 
            otvet4 = "мне нечего сказать" 
            otvet5 = "ПоДаркая фикр кадими" 

            nechevoskazat = [otvet1, otvet2, otvet3,otvet4,otvet5] 
            sleep(1)
            mySuperBot.send_chat_action(message.chat.id, "typing")
            
            mySuperBot.send_message(message.chat.id, random.choice(nechevoskazat)) 
             
            #отпрака такого же текаста  
            #mySuperBot.send_message(message.chat.id, message.text) 
             
             
@mySuperBot.message_handler(commands=['bye']) 
 
def obrabotkaKomandiStart(message): 
    mySuperBot.send_chat_action(message.chat.id, "typing") 
 
    # mySuperBot.send_message(комуОтправить, какое собщениеОтправить) 
    mySuperBot.send_message(message.chat.id, "пока") 
@mySuperBot.callback_query_handler(func=lambda call:True)
def otvetchik(call):
    try:
        if call.message:
            if call.data=='good':
                mySuperBot.send_message(call.message.chat.id,'Вот и Хорошо')
            if call.data=='bad':
                mySuperBot.send_message(call.message.chat.id,'Не унывай <b.{0.first_name}</b>,бывало и хуже'.format(call.from_user))
            # тут   что сделаем
    except Exception as e:
        print(repr(e))
            #удаляем возможность ответа клавиатуры
        mySuperBot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
        text='не жалуюсь Хвала Аллаху. А у тебя?', reply_markup=None)
            
#запуск бота 
mySuperBot.polling(none_stop = True)