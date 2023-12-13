from telebot import types


main_menu_panel = types.ReplyKeyboardMarkup(row_width=2)
card_btn = types.KeyboardButton('/card')
get_my_id_btn = types.KeyboardButton('/id')
info_btn = types.KeyboardButton('/info')
main_menu_panel.add(card_btn, get_my_id_btn, info_btn)