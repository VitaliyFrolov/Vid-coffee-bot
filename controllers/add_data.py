import sqlite3


class Add_data():
    def add_new_card(bot, message, messages):
        data = messages.split()
        phone_number = data[0].replace(',', '')
        tg_id = data[1]
         
        db = sqlite3.connect('./database/vid_coffee.db', check_same_thread=False)
        db_cursor = db.cursor()
        
        db_cursor.execute("SELECT * FROM cards WHERE phone_number=?", (phone_number,))
        card = db_cursor.fetchone()
        
        if card:
            bot.send_message(message.chat.id, 'Карта с таким номером уже существует')
        else:
            db_cursor.execute("INSERT INTO cards (phone_number, tg_id) VALUES (?, ?)", (phone_number, tg_id))
            bot.send_message(message.chat.id, f'Карточка на номер "{phone_number}" успешно зарегистрирована!')
        
        db.commit()
        db.close()

    def add_worker(bot, message, worker_id):
        db = sqlite3.connect('./database/vid_coffee.db', check_same_thread=False)
        db_cursor = db.cursor()

        db_cursor.execute("SELECT * FROM workers WHERE tg_id=?", (worker_id,))
        worker = db_cursor.fetchone()

        if worker:
            bot.send_message(message.chat.id, 'Такой сотрудник уже существует!')
        else:
            db_cursor.execute("INSERT INTO workers (tg_id) VALUES (?)", (worker_id,))
            bot.send_message(message.chat.id, 'Сотрудник успешно добавлен!')

        db.commit()
        db.close()

    def add_coffee_point(bot, message, messages):
        data = messages.split()
        phone_number = data[0].replace(',', '')
        quantity_coffee_points = int(data[1])

        db = sqlite3.connect('./database/vid_coffee.db', check_same_thread=False)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM cards WHERE phone_number=?", (phone_number,))
        row = cursor.fetchone()

        if row:
            new_coffee_points = row[3] + quantity_coffee_points
            cursor.execute("UPDATE cards SET coffee_point=? WHERE phone_number=?", (new_coffee_points, phone_number))
            db.commit()
            bot.send_message(message.chat.id, f'Количество онлайн-печатей для пользователя с номером "{phone_number}" успешно увеличено на "{quantity_coffee_points}"')
        else:
            bot.send_message(message.chat.id, f'Карточка с номером {phone_number} не найдена')

        db.close()