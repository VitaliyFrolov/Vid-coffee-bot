from telebot import types


worker_menu_panel = types.ReplyKeyboardMarkup(row_width=3)
add_card_btn = types.KeyboardButton('/add_card')
remove_card_btn = types.KeyboardButton('/remove_card')
check_card_list_btn = types.KeyboardButton('/check_card')
add_coffee_point_btn = types.KeyboardButton('/add_coffee_point')
make_free_coffee = types.KeyboardButton('/make_free_coffee')
worker_menu_panel.add(add_card_btn, remove_card_btn, check_card_list_btn, add_coffee_point_btn, make_free_coffee)