from telebot import types


admin_menu_panel = types.ReplyKeyboardMarkup(row_width=3)
add_worker_btn = types.KeyboardButton('/add_worker')
remove_worker_btn = types.KeyboardButton('/remove_worker')
worker_list_btn = types.KeyboardButton('/worker_list')
statistics_btn = types.KeyboardButton('/statistics')
admin_menu_panel.add(add_worker_btn, remove_worker_btn, worker_list_btn, statistics_btn)