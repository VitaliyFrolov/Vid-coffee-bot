import sqlite3


class Remove_data():
    def remove_card(bot, message, phone_number):
        db = sqlite3.connect('./database/vid_coffee.db')
        db_cursor = db.cursor()
        
        db_cursor.execute("SELECT * FROM cards WHERE phone_number = ?", (phone_number,))
        existing_card = db_cursor.fetchone()
        
        if existing_card:
            db_cursor.execute("DELETE FROM cards WHERE phone_number = ?", (phone_number,))
            bot.send_message(message.chat.id, f'Карточка с номером {phone_number} успешно удалена!')
        else:
            bot.send_message(message.chat.id, f'Карточка с номером {phone_number} не найдена!')
        
        db.commit()
        db.close()

    def remove_worker(bot, message, worker_id):
        db = sqlite3.connect('./database/vid_coffee.db', check_same_thread=False)
        db_cursor = db.cursor()

        db_cursor.execute("SELECT tg_id FROM workers WHERE tg_id=?", (worker_id,))
        worker = db_cursor.fetchone()

        if worker:
            db_cursor.execute("DELETE FROM workers WHERE tg_id=?", (worker_id,))
            bot.send_message(message.chat.id, 'Сотрудние успешно удален!')
        else:
            bot.send_message(message.chat.id, 'Такой сотрудник не найден!')

        db.commit()
        db.close()

    def make_free_coffee(bot, message, messages):
        data = messages.split()
        phone_number = data[0].replace(',', '')
        free_coffee = int(data[1])

        db = sqlite3.connect('./database/vid_coffee.db')
        db_cursor = db.cursor()

        db_cursor.execute("SELECT free_coffee FROM cards WHERE phone_number = ?", (phone_number,))
        current_free_coffee = db_cursor.fetchone()[0]

        if current_free_coffee >= free_coffee:
            updated_free_coffee = current_free_coffee - free_coffee
            db_cursor.execute("UPDATE cards SET free_coffee = ? WHERE phone_number = ?", (updated_free_coffee, phone_number))
            bot.send_message(message.chat.id, f"С карточки под номером {phone_number} снято {free_coffee} напитков!")
        else:
            bot.send_message(message.chat.id, f'Недостаточно онлайн-печатей для приготовления бесплатного напитка!')

        db.commit()
        db.close()