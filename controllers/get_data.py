import sqlite3


class Get_data():
    def check_my_card(bot, message):
        db = sqlite3.connect('./database/vid_coffee.db')
        db_cursor = db.cursor()
        
        db_cursor.execute("SELECT coffee_point, free_coffee FROM cards WHERE tg_id = ?", (message.from_user.id,))
        
        row = db_cursor.fetchone()
        
        db.close()
        
        if row:
            coffee_point = row[0]
            free_coffee = row[1]
            message_table = f'<b><u>Карточка гостя vid coffee на имя: {message.from_user.first_name}</u></b>\n\nОнлайн печатей: {coffee_point}\nБеспталных напитков: {free_coffee}'
            return bot.send_message(message.chat.id, message_table, parse_mode="HTML")
        else:
            return bot.send_message(message.chat.id, 'У вас еще нет карточки, вам необходимо ее завести.')
        
    def check_card(bot, message, phone_number):
        db = sqlite3.connect('./database/vid_coffee.db')
        db_cursor = db.cursor()

        db_cursor.execute("SELECT coffee_point, free_coffee FROM cards WHERE phone_number = ?", (phone_number,))

        row = db_cursor.fetchone()

        db.close()

        if row:
            coffee_point = row[0]
            free_coffee = row[1]

            message_table = f'<b><u>Карточка гостя vid coffee на номер: {phone_number}</u></b>\n\nОнлайн печатей: {coffee_point}\nБеспталных напитков: {free_coffee}'
            return bot.send_message(message.chat.id, message_table, parse_mode="HTML")
        else:
            return bot.send_message(message.chat.id, 'Карточки с указанным номером телефона не существует')
        
    def check_workers_list(bot, message):
        db = sqlite3.connect('./database/vid_coffee.db', check_same_thread=False)
        db_cursor = db.cursor()

        db_cursor.execute("SELECT tg_id FROM workers")
        worker_ids = db_cursor.fetchall()

        for worker_id in worker_ids:
            bot.send_message(message.chat.id, worker_id)

        db.close()

    def check_all_users(bot, message):
        db = sqlite3.connect('./database/vid_coffee.db', check_same_thread=False)
        db_cursor = db.cursor()

        db_cursor.execute("""SELECT COUNT(*) FROM cards""")
        count = db_cursor.fetchone()[0]

        db.close()

        return bot.send_message(message.chat.id, f'Общее кол-во пользователей: {count}')