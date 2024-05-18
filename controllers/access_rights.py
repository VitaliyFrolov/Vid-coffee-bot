import sqlite3
import os
from views.states.admin_state import Admin_state
from views.states.worker_state import Worker_state

class Access_rights():
    def check_worker(tg_id):
        db = sqlite3.connect('./database/vid_coffee.db', check_same_thread=False)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM workers WHERE tg_id = ?", (tg_id,))
        result = cursor.fetchone()

        if result:
            Worker_state.worker_status = True
        else:
            Worker_state.worker_status = False

        db.close()

    def check_admin(tg_id):
        admin_id = os.getenv('ADMIN_ID')
        if int(tg_id) == int(admin_id):
            Admin_state.admin_status = True
        else:
            Admin_state.admin_status = False