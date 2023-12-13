import telebot
import os
from dotenv import * 
from database.database_settings import *
from views.panels.main_panel import main_menu_panel
from views.panels.admin_panel import admin_menu_panel
from views.panels.worker_panel import worker_menu_panel
from controllers.get_data import Get_data
from controllers.add_data import Add_data
from controllers.remove_data import Remove_data
from controllers.access_rights import Access_rights
from views.states.admin_state import Admin_state, Waiting_answer_admin
from views.states.worker_state import Worker_state, Waiting_answer_worker


token_dotenv = os.environ.get('TOKEN')
admin_id_dotenv = os.environ.get('ADMIN_ID')
bot = telebot.TeleBot(token_dotenv, parse_mode=None)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}", reply_markup=main_menu_panel)

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Тут будет информация о боте!')

@bot.message_handler(commands=['card'])
def card_menu(message):
    Get_data.check_my_card(bot, message)

@bot.message_handler(commands=['id'])
def get_my_id(message):
    bot.send_message(message.chat.id, f'Ваш telegram id: {message.from_user.id}')

@bot.message_handler(commands=['admin'])
def admin(message):
    Access_rights.check_admin(message.chat.id)
    if Admin_state.admin_status == True:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, вы вошли в панель администратора', reply_markup=admin_menu_panel)
    else: pass

@bot.message_handler(commands=['add_worker'])
def add_worker_handler(message):
    if Admin_state.admin_status == True:
        Waiting_answer_admin.add_worker = True
        bot.send_message(message.chat.id, 'Введите id пользователя: Пример (7788990)')
    else: pass

@bot.message_handler(commands=['remove_worker'])
def remove_worker_handler(message):
    if Admin_state.admin_status == True:
        Waiting_answer_admin.remove_worker = True
        bot.send_message(message.chat.id, 'Введите id пользователя: Пример: (7788990)')
    else: pass

@bot.message_handler(commands=['worker_list'])
def check_worker_list_handler(message):
    if Admin_state.admin_status == True:
        Get_data.check_workers_list(bot, message)
    else: pass

@bot.message_handler(commands=['statistics'])
def statistics(message):
    if Admin_state.admin_status == True:
        Get_data.check_all_users(bot, message)
    else: pass

@bot.message_handler(commands=['worker'])
def worker(message):
    Access_rights.check_worker(message.from_user.id)
    if Worker_state.worker_status == True:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, вы вошли в панель сотрудника', reply_markup=worker_menu_panel)
    else: pass

@bot.message_handler(commands=['add_card'])
def add_card_handler(message):
    Access_rights.check_worker(message.from_user.id)
    if Worker_state.worker_status == True:
        Waiting_answer_worker.add_card = True
        bot.send_message(message.chat.id, 'Введите номер телефона и id пользователя: Пример: (+7998887766, 7788990)')
    else: pass

@bot.message_handler(commands=['remove_card'])
def remove_card_handler(message):
    Access_rights.check_worker(message.from_user.id)
    if Worker_state.worker_status == True:
        Waiting_answer_worker.remove_card = True
        bot.send_message(message.chat.id, 'Введите номер телефона пользователя: Пример: (+7998887766, 7788990)')
    else: pass

@bot.message_handler(commands=['check_card'])
def check_card_handler(message):
    Access_rights.check_worker(message.from_user.id)
    if Worker_state.worker_status == True:
        Waiting_answer_worker.check_card = True
        bot.send_message(message.chat.id, 'Введите номер телефона пользователя: Пример: (+7998887766, 7788990)')
    else: pass

@bot.message_handler(commands=['add_coffee_point'])
def add_coffee_point_handler(message):
    Access_rights.check_worker(message.from_user.id)
    if Worker_state.worker_status == True:
        Waiting_answer_worker.add_coffee_point = True
        bot.send_message(message.chat.id, 'Введите номер телефона пользователя и кол-во онлайн-печатей: Пример: (+7998887766, 2)')
    else: pass

@bot.message_handler(commands=['make_free_coffee'])
def make_free_coffee_handler(message):
    Access_rights.check_worker(message.from_user.id)
    if Worker_state.worker_status == True:
        Waiting_answer_worker.make_free_coffee = True
        bot.send_message(message.chat.id, 'Введите номер телефона пользователя и кол-во бесплатных напитков, которые хотели бы списать: Пример: (+7998887766, 1)')
    else: pass

@bot.message_handler(func=lambda message: True)
def all_message_handler(message):
    if Admin_state.admin_status == True:
        if Waiting_answer_admin.add_worker == True:
            Add_data.add_worker(bot, message, message.text)
            Waiting_answer_admin.add_worker = False
            
        elif Waiting_answer_admin.remove_worker == True:
            Remove_data.remove_worker(bot, message, message.text)
            Waiting_answer_admin.remove_worker = False

        elif Waiting_answer_worker.add_card == True:
            Add_data.add_new_card(bot, message, message.text)
            Waiting_answer_worker.add_card = False

        elif Waiting_answer_worker.remove_card == True:
            Remove_data.remove_card(bot, message, message.text)
            Waiting_answer_worker.remove_card = False

        elif Waiting_answer_worker.check_card == True:
            Get_data.check_card(bot, message, message.text)
            Waiting_answer_worker.check_card = False

        elif Waiting_answer_worker.add_coffee_point == True:
            Add_data.add_coffee_point(bot, message, message.text)
            Waiting_answer_worker.add_coffee_point = False

        elif Waiting_answer_worker.make_free_coffee == True:
            Remove_data.make_free_coffee(bot, message, message.text)
            Waiting_answer_worker.make_free_coffee = False

        else: pass

    else: pass

bot.infinity_polling(none_stop=True)
