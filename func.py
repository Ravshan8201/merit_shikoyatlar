from email import message

import requests as requests
import telegram

from cons import *
from cons import dct
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove, bot
from sql_cons import *
from sql_murojaat import *
import sqlite3
from datetime import date
today = date.today()
import random
import logging
import requests
import json

def start(update, context):
    try:
        user_id = update.message.chat_id
    except Exception:
        user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    lang_ = cur.execute(select_Lang.format(user_id)).fetchall()
    connect.commit()
    try:
        user_id = update.message.chat_id
    except Exception:
        user_id = update.callback_query.from_user.id
    try:
        TG_ID = TG_ID[0][0]
        lang_ = lang_[0][0]
    except Exception:
        pass
    if TG_ID!=user_id:
       id = random.randint(100000,100000000)
       cur.execute(first_insert.format(user_id, id, 1))
       cur.execute(first_insert_murojat.format(user_id, id ))
       connect.commit()
       knopka_lang = [
           KeyboardButton(text='РУС🇷🇺'),
           KeyboardButton(text='УЗБ🇺🇿')
       ]
       context.bot.send_message(chat_id=user_id, text='Выберите язык:\nТилни танланг:',
                             reply_markup=ReplyKeyboardMarkup([knopka_lang], resize_keyboard=True))

    if TG_ID==user_id:
       cur.execute(upd_Stage.format('{}', user_id).format(20))
       connect.commit()
       knopka = [
           KeyboardButton(text=butdct[lang_][8]),
           KeyboardButton(text=butdct[lang_][9])]
       context.bot.send_message(chat_id=user_id, text=dct[lang_][7], parse_mode='Markdown',
                             reply_markup=ReplyKeyboardMarkup([knopka], resize_keyboard=True))

def audio(update, context):
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    connect.commit()
    user_id = update.message.chat_id

    lang_ = cur.execute(select_Lang.format(user_id)).fetchall()
    try:
        lang_ = lang_[0][0]
    except Exception:
        context.bot.send_message(chat_id=user_id, text=dct[2][13])
    context.bot.send_message(chat_id=user_id, text=dct[lang_][13])



def next_func(update, context):
    connect = sqlite3.connect('users.sqlite')
    cur = connect.cursor()
    connect.commit()
    user_id = update.message.chat_id
    m_id = update.message.message_id
    f_name = update.message.from_user.first_name


    stage_ = cur.execute(select_Stage.format(user_id)).fetchall()
    lang_ = cur.execute(select_Lang.format(user_id)).fetchall()
    a_name = cur.execute(select_Ism.format(user_id)).fetchall()
    s_name = cur.execute(select_Familiya.format(user_id)).fetchall()
    num = cur.execute(select_Telefon.format(user_id)).fetchall()
    SizKimsiz = cur.execute(select_SizKimsiz.format(user_id)).fetchall()
    MijozTuri = cur.execute(select_MijozTuri.format(user_id)).fetchall()
    FarzandSoni = cur.execute(select_FarzandSoni.format(user_id)).fetchall()
    MurojaatTuri = cur.execute(select_MurojaatTuri.format(user_id)).fetchall()
    Filial = cur.execute(select_Filial.format(user_id)).fetchall()
    Soha = cur.execute(select_Soha.format(user_id)).fetchall()
    Matn = cur.execute(select_Matn.format(user_id)).fetchall()
    Status = cur.execute(select_Status.format(user_id)).fetchall()
    Javobgar = cur.execute(select_Javobgar.format(user_id)).fetchall()
    OxirgiMuddat = cur.execute(select_OxirgiMuddat.format(user_id)).fetchall()
    MijozBahosi = cur.execute(select_MijozBahosi.format(user_id)).fetchall()
    QoshganShaxs = cur.execute(select_QoshganShaxs.format(user_id)).fetchall()
    QoshilganVaqt = cur.execute(select_QoshilganVaqt.format(user_id)).fetchall()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    murojatid =  cur.execute(select_MurojaatID.format(user_id)).fetchall()
    connect.commit()

    try:
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        num = num[0][0]
        a_name = a_name[0][0]
        s_name = s_name[0][0]
        SizKimsiz = SizKimsiz[0][0]
        MijozTuri = MijozTuri[0][0]
        FarzandSoni = FarzandSoni[0][0]
        MurojaatTuri = MurojaatTuri[0][0]
        Filial = Filial[0][0]
        Soha = Soha[0][0]
        Matn = Matn[0][0]
        Status = Status[0][0]
        Javobgar = Javobgar[0][0]
        OxirgiMuddat = OxirgiMuddat[0][0]
        MijozBahosi = MijozBahosi[0][0]
        QoshganShaxs = QoshganShaxs[0][0]
        QoshilganVaqt = QoshilganVaqt[0][0]
        TG_ID=TG_ID[0][0]
        murojatid = murojatid [0][0]
    except Exception:
        pass
    message = update.message.text
    message = str(message)

    if stage_ == 1 and message == 'РУС🇷🇺':
        knopka_lang = [
            KeyboardButton(text='РУС🇷🇺'),
            KeyboardButton(text='УЗБ🇺🇿')
        ]
        context.bot.send_message(chat_id=user_id, text=dct[1][0], parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardRemove([knopka_lang], resize_keyboard=True))

        cur.execute(upd_Lang.format(1, user_id))
        cur.execute(upd_Stage.format(2, user_id))
        connect.commit()

    if stage_ == 1 and message == 'УЗБ🇺🇿':
        knopka_lang = [
            KeyboardButton(text='РУС🇷🇺'),
            KeyboardButton(text='УЗБ🇺🇿')
        ]
        context.bot.send_message(chat_id=user_id, text=dct[2][0], parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardRemove([knopka_lang], resize_keyboard=True))

        cur.execute(upd_Lang.format(2, user_id))
        cur.execute(upd_Stage.format('{}', user_id).format(2))
        connect.commit()

    if stage_ == 2 and " " in message and int(len(message)) >= 7:
        print('12321dfeferw')
        message_list = message.split()
        familiya = message_list[0]
        ism = message_list[1]
        print(ism)
        cur.execute(upd_Familiya.format(familiya, user_id))

        cur.execute(upd_Ism.format(ism, user_id))

        cur.execute(upd_Stage.format('{}', user_id).format(3))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][1], parse_mode='Markdown')

    # betda nomer tekshiradi va kimligini soridi

    if stage_ == 3 and len(str(message)) == 9:

            message = int(message)
            cur.execute(upd_Telefon.format(message, user_id))
            cur.execute(upd_Stage.format(4, user_id))
            connect.commit()
            knopka = [
                KeyboardButton(text=butdct[lang_][0]),
                KeyboardButton(text=butdct[lang_][1])
            ]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][2], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([knopka], resize_keyboard=True))
            print(1)
    if stage_ == 3 and len(str(message)) != 9:
        try:

           f= int(message)
           f+1
           context.bot.send_message(chat_id=user_id, text= dct[lang_][1] , parse_mode='Markdown')
        except Exception:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][1], parse_mode='Markdown')


    if stage_ == 2 and len(str(message)) < 7 or stage_ == 2 and " " not in message:
            print(11)

            context.bot.send_message(chat_id=user_id, text=dct[lang_][0] ,parse_mode='Markdown')



    # errorga bu
    if stage_ == 4 and message not in butdct[lang_][0:2]:
        context.bot.send_message(chat_id=user_id, text=dct[lang_][2], parse_mode='Markdown')

    # ishlidid bu maktabga aloqasi bormi yomi soridi
    if stage_ == 4 and message in butdct[lang_][0:2]:
        cur.execute(upd_SizKimsiz.format(message, user_id))

        knopka = [
            KeyboardButton(text=butdct[lang_][2]),
            KeyboardButton(text=butdct[lang_][3])
        ]

        if message == butdct[lang_][0]:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][3], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([knopka], resize_keyboard=True))
            cur.execute(upd_Stage.format(5, user_id))
            connect.commit()

        if message == butdct[lang_][1]:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][4], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([knopka], resize_keyboard=True))
            cur.execute(upd_Stage.format(6, user_id))
            connect.commit()
    # bergan ota va farzand soni bowlaniwi
    if stage_ == 5 and message in butdct[lang_][2:4]:
        cur.execute(upd_MijozTuri.format(message, user_id))
        connect.commit()

        if message == butdct[lang_][2] and SizKimsiz == butdct[lang_][0]:
            # bergan ota va farzand soni
            knopka1 = [
                KeyboardButton(text=butdct[lang_][4]),
                KeyboardButton(text=butdct[lang_][5])]
            knopka =    [KeyboardButton(text=butdct[lang_][6]),
                KeyboardButton(text=butdct[lang_][7])]

            context.bot.send_message(chat_id=user_id, text=dct[lang_][5], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([knopka1,knopka], resize_keyboard=True))
            cur.execute(upd_Stage.format(6, user_id))
            connect.commit()
        # bermoqchi ota va farzand soni
        if message == butdct[lang_][3] and SizKimsiz == butdct[lang_][0]:
            knopka1 = [
                KeyboardButton(text=butdct[lang_][4]),
                KeyboardButton(text=butdct[lang_][5])]
            knopka =    [KeyboardButton(text=butdct[lang_][6]),
                KeyboardButton(text=butdct[lang_][7])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][6], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([knopka1,knopka], resize_keyboard=True))
            cur.execute(upd_Stage.format(6, user_id))
            connect.commit()
    if stage_ == 5 and message  != butdct[lang_][2:4] :
        context.bot.send_message(chat_id=user_id, text=dct[lang_][12],  parse_mode='Markdown')

     #bettta otalar sonadan keladi bolalar xa yoqdan va murojat turi soraladi
    if stage_ == 6 and message in butdct[lang_][4:8] or stage_ == 6 and SizKimsiz == butdct[lang_][1]:
        #OTALARGA
        if SizKimsiz != butdct[lang_][1]:
            cur.execute(upd_FarzandSoni.format(message, user_id))
            knopka = [
                KeyboardButton(text=butdct[lang_][8]),
                KeyboardButton(text=butdct[lang_][9])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][7], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([knopka], resize_keyboard=True))
            cur.execute(upd_Stage.format(7, user_id))
            connect.commit()
        #BOLALRGA
        if SizKimsiz == butdct[lang_][1]:
            cur.execute(upd_MijozTuri.format(message, user_id))
            knopka = [
                KeyboardButton(text=butdct[lang_][8]),
                KeyboardButton(text=butdct[lang_][9])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][7], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([knopka], resize_keyboard=True))
            cur.execute(upd_Stage.format(7, user_id))
            connect.commit()

    #if stage_ == 6 and message not in butdct[lang_][4:8] and or stage_ == 6 and SizKimsiz == butdct[lang_][1] and :
     #   context.bot.send_message(chat_id=user_id, text="❗️❗️❗️" + dct[lang_][12] + "1❗️❗️❗️", parse_mode='Markdown')

    SHEETY_ENDPOINT = 'https://api.sheety.co/233cb5bb0144964d59970ce45f378d08/meritSchoolsFeedbackSystem/filiallar'
    butfilial = requests.get(url=SHEETY_ENDPOINT)
    logging.basicConfig()
    #Validatsiya
   # if stage_ == 7 and message not in butdct[lang_][8:10]  :
      #  context.bot.send_message(chat_id=user_id, text="❗️❗️❗️" + dct[lang_][12] + "❗️❗️❗️", parse_mode='Markdown')


    if stage_ == 7 and message in butdct[lang_][8:10]  or stage_== 20 and message in butdct[lang_][8:10]:
        SHEETY_ENDPOINT = 'https://api.sheety.co/233cb5bb0144964d59970ce45f378d08/meritSchoolsFeedbackSystem/filiallar'
        butfilial = requests.get(url=SHEETY_ENDPOINT)
        logging.basicConfig()
        print(butfilial)
        butfilial = butfilial.text
        print(butfilial)
        butfilial = json.loads(butfilial)
        print(butfilial)
        butfilial = butfilial['filiallar']
        list = []
        for e in butfilial:
            print(e['nomi'])
            list.append(e['nomi'])
        print(list)

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(list, 2)
        buttons = []
        for e in tovar_list:
            b = []
            for k in e:
                k = k
                print(k)
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)

        context.bot.send_message(chat_id=user_id, text=dct[lang_][8], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        cur.execute(upd_MurojaatTuri.format(message, user_id))
        cur.execute(upd_Stage.format(7.5, user_id))
        connect.commit()
    SHEETY_ENDPOINT = 'https://api.sheety.co/233cb5bb0144964d59970ce45f378d08/meritSchoolsFeedbackSystem/filiallar'
    butfilial = requests.get(url=SHEETY_ENDPOINT)
    logging.basicConfig()
    butfilial = butfilial.text
    butfilial = json.loads(butfilial)
    print(butfilial)
    butfilial = butfilial['filiallar']
    list = []
    for e in butfilial:
        print(e['nomi'])
        list.append(e['nomi'])
    print(list)
    SHEETY_ENDPOINT = 'https://api.sheety.co/233cb5bb0144964d59970ce45f378d08/meritSchoolsFeedbackSystem/sohalar'
    butsoha = requests.get(url=SHEETY_ENDPOINT)
    logging.basicConfig()
    if stage_ == 7.5 and message in list:

            butsoha = butsoha.text
            butsoha = json.loads(butsoha)
            butsoha = butsoha['sohalar']
            list = []
            for e in butsoha:
                print(e['nomi'])
                list.append(e['nomi'])
            print(list)

            def func_chunks_generators(lst, n):
                for i in range(0, len(lst), n):
                    yield lst[i: i + n]

            tovar_list = func_chunks_generators(list, 2)
            buttons = []
            for e in tovar_list:
                b = []
                for k in e:
                    k = k
                    print(k)
                    a = KeyboardButton(text=str(k))
                    b.append(a)
                buttons.append(b)

            context.bot.send_message(chat_id=user_id, text=dct[lang_][10], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
            cur.execute(upd_Filial.format(message, user_id))
            cur.execute(upd_Stage.format(8, user_id))
            connect.commit()
    butsoha = butsoha.text
    butsoha = json.loads(butsoha)
    butsoha = butsoha['sohalar']
    for e in butsoha:
        print(e['nomi'])
        list.append(e['nomi'])
    print(list)

    if stage_ == 8 and message in  list:
            knopka = [
                KeyboardButton(text="FILIAL GOOGLDAN"),
                KeyboardButton(text="FILIAL GOOGLDAN2")]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][9], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardRemove([knopka], resize_keyboard=True))
            cur.execute(upd_Soha.format(message, user_id))
            cur.execute(upd_Stage.format(9, user_id))
            connect.commit()

    if stage_ == 9 and message !='1':
        cur.execute(upd_Matn.format(message, user_id))
        cur.execute(upd_Stage.format(9, user_id))
        connect.commit()
        try:
            user_id = update.message.chat_id
        except Exception:
            user_id = update.callback_query.from_user.id

        knopka= [
            InlineKeyboardButton(text='Start', callback_data='start'),
        ]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][11],parse_mode='Markdown',
                                 reply_markup=InlineKeyboardMarkup([knopka]))





        SHEETY_ENDPOINT = 'https://api.sheety.co/233cb5bb0144964d59970ce45f378d08/meritSchoolsFeedbackSystem/murojaatlar'
        data = {
                "murojaatlar": {
                    "murojaatid": "{}".format(murojatid),
                    "telefon": "{}".format(num),
                    "ism": "{}".format(a_name),
                    "familiya": "{}".format(s_name),
                    "sizKimsiz": "{}".format(SizKimsiz),
                    "mijozTuri": "{}".format(MijozTuri),
                    "farzandSoni": "{}".format(FarzandSoni),
                    "murojaatTuri": "{}".format(MurojaatTuri),
                    "filial": "{}".format(Filial),
                    "soha": "{}".format(Soha),
                    "matn": "{}".format(message),
                    "status": "{}".format('Қабул қилинди'),
                    "javobgar": "{}".format(Javobgar),
                    "oxirgiMuddat": "{}".format(OxirgiMuddat),
                    "mijozBahosi": "{}".format(MijozBahosi),
                    "qoshganShaxs": "{}".format(QoshganShaxs),
                    "qoshilganVaqt": "{}".format(today),
                    "oxirgiOzgarishVaqti": "{}".format(OxirgiMuddat),
                    "oxirgiOzgartirganShaxs": "{}".format(" "),
                    "tg_id": "{}".format(TG_ID),

                }
            }

        response = requests.post(url=SHEETY_ENDPOINT, json=data)
        logging.basicConfig()

















