import telebot
import time
from telebot import types

bot = telebot.TeleBot("781020407:AAGieeeecXl0hoscL3QWCGnXkD9FielXwG0")
owner = 458619004
counter = 0

def is_recent(m):
    return (time.time() - m.date) < 3600

def get(m):
    if is_recent(m):
        if m.text.lower().split(' ')[1] in recipes_armor and not(m.text.lower().split(' ')[2] == "knife") \
        and not(m.text.lower().split(' ')[2] == "dagger"):
            try:
                item = m.text.lower().split(' ')
                for element in recipes_armor[item[1]][item[2]]:
                    bot.send_message(m.chat.id, "/g_withdraw " + element)
                global counter
                counter = counter + 1
            except:
                bot.send_message(m.chat.id, "Wrong item")
        else:
            item = m.text.lower().split(' ')
            try:
                for element in recipes_weapon[item[1] + " " + item[2]]:
                    bot.send_message(m.chat.id, "/g_withdraw " + element)
            except:
                try:
                    for element in recipes_weapon[item[1]]:
                        bot.send_message(m.chat.id, "/g_withdraw " + element)
                    counter = counter + 1
                except:
                    bot.send_message(m.chat.id, "Wrong item")
              
def start_mes(m, flag = True):
    keyboard = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Armor", callback_data="armor")
    b2 = types.InlineKeyboardButton(text="Weapon", callback_data="weapon")
    keyboard.add(b1, b2)
    if flag:
        bot.send_message(m.chat.id, "/g", reply_markup=keyboard)
    else:
        bot.edit_message_text(chat_id=m.chat.id, message_id=m.message_id,
                              text="/g", reply_markup=keyboard)
                    
order = {
    "armor": ["r06 1", "k06 3", "33 15", "31 12", "23 9", "16 5", "28 3", "15 3"],
    "helmet": ["r07 1", "k07 3", "33 12", "31 9", "23 7", "16 3", "28 2", "15 1"],
    "boots": ["r08 1", "k08 3", "33 9", "31 7", "23 5", "16 1", "28 1", "15 3"],
    "gauntlets": ["r09 1", "k09 3", "33 9", "31 7", "23 5", "16 1", "28 1", "15 3"],
    "shield": ["r10 1", "k10 3", "33 7", "25 15", "23 7", "28 1"]
}
hunter = {
    "armor": ["r11 1", "k11 3", "20 24", "31 12", "23 9", "16 5", "28 3", "15 3"],
    "helmet": ["r12 1", "k12 3", "20 18", "31 9", "23 7", "16 3", "28 2", "15 1"],
    "boots": ["r13 1", "k13 3", "20 12", "31 7", "23 5", "16 1", "28 1"],
    "gloves": ["r14 1", "k14 3", "20 12", "31 7", "23 5", "16 1", "28 1"]
}
clarity = {
    "robe": ["r15 1", "k15 3", "20 15", "31 12", "23 9", "16 7", "28 3", "15 5"],
    "circlet": ["r16 1", "k16 3", "20 9", "31 9", "23 7", "16 5", "28 2", "15 3"],
    "shoes": ["r17 1", "k17 3", "20 7", "31 5", "23 3", "16 3", "28 1", "15 1"],
    "bracers": ["r18 1", "k18 3", "20 7", "31 5", "23 3", "16 3", "28 1", "15 1"]
}
crusader = {
    "armor": ["r33 1", "k33 5", "34 32", "31 17", "23 13", "16 15", "29 5", "15 9"],
    "helmet": ["r34 1", "k34 5", "34 27", "31 12", "23 9", "16 7", "29 3", "15 5"],
    "boots": ["r35 1", "k35 5", "34 21", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "gauntlets": ["r36 1", "k36 5", "34 21", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "shield": ["r37 1", "k37 5", "33 15", "25 27", "23 15", "29 3", "15 3", "16 7"]
}
royal = {
    "armor": ["r38 1", "k38 5", "34 32", "31 17", "23 13", "16 15", "29 5", "15 9"],
    "helmet": ["r39 1", "k39 5", "34 27", "31 12", "23 9", "16 7", "29 3", "15 5"],
    "boots": ["r40 1", "k40 5", "34 21", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "gauntlets": ["r41 1", "k41 5", "34 21", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "shield": ["r42 1", "k42 5", "33 15", "25 27", "23 15", "29 3", "15 3", "16 7"]
}
ghost = {
    "armor": ["r43 1", "k43 5", "35 18", "31 17", "23 13", "16 15", "29 5", "15 9"],
    "helmet": ["r44 1", "k44 5", "35 14", "31 12", "23 9", "16 7", "29 3", "15 5"],
    "boots": ["r45 1", "k45 5", "35 11", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "gloves": ["r46 1", "k46 5", "35 11", "31 9", "23 7", "16 3", "29 1", "15 1"]
}
lion = {
    "armor": ["r47 1", "k47 5", "35 18", "31 17", "23 13", "16 15", "29 5", "15 9"],
    "helmet": ["r48 1", "k48 5", "35 14", "31 12", "23 9", "16 7", "29 3", "15 5"],
    "boots": ["r49 1", "k49 5", "35 11", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "gloves": ["r50 1", "k50 5", "35 11", "31 9", "23 7", "16 3", "29 1", "15 1"]
}
demon = {
    "robe": ["r51 1", "k51 5", "35 11", "31 17", "23 13", "16 21", "29 5", "15 12"],
    "circlet": ["r52 1", "k52 5", "35 8", "31 12", "23 9", "16 16", "29 3", "15 9"],
    "shoes": ["r53 1", "k53 5", "35 5", "31 7", "23 7", "16 7", "29 1", "15 5"],
    "bracers": ["r54 1", "k54 5", "35 5", "31 7", "23 7", "16 7", "29 1", "15 5"]
}
divine = {
    "robe": ["r55 1", "k55 5", "35 11", "31 17", "23 13", "16 21", "29 5", "15 12"],
    "circlet": ["r56 1", "k56 5", "35 8", "31 12", "23 9", "16 16", "29 3", "15 9"],
    "shoes": ["r57 1", "k57 5", "35 5", "31 7", "23 7", "16 7", "29 1", "15 5"],
    "bracers": ["r58 1", "k58 5", "35 5", "31 7", "23 7", "16 7", "29 1", "15 5"]
}
durable = {
    "cloak": ["r60 1", "k60 3", "35 5", "31 3", "23 5", "16 3", "29 1", "15 1"]
}
storm = {
    "cloak": ["r59 1", "k59 3", "35 5", "31 3", "23 5", "16 3", "29 1", "15 1"]
}
blessed = {
    "cloak": ["r61 1", "k61 3", "35 5", "31 3", "23 5", "16 3", "29 1", "15 1"]
}

champion_sword = ["r01 1", "k01 3", "33 41", "25 27", "23 41", "27 3", "18 3", "17 1"]
trident = ["r02 1", "k02 3", "14 41", "25 27", "23 41", "27 3", "18 3", "17 1"]
hunter_bow = ["r03 1", "k03 3", "14 41", "25 27", "23 41", "27 3", "18 3", "17 1"]
war_hammer = ["r04 1", "k04 3", "33 41", "25 27", "23 41", "27 3", "18 3", "17 1"]
hunter_dagger = ["r05 1", "k05 3", "33 7", "25 15", "23 7", "27 1"]

thundersoul_sword = ["r19 1", "k19 5", "33 68", "25 33", "23 57", "18 7", "18 7", "17 3"]
doomblade_sword = ["r20 1", "k20 5", "33 72", "32 11", "23 61", "30 5", "18 9", "17 3"]
eclipse = ["r21 1", "k21 5", "33 72", "32 11", "23 61", "30 5", "18 9", "17 3"]

guards_spear = ["r22 1", "k22 5", "14 68", "25 33", "23 57", "30 5", "18 7", "17 3"]
kings_defender = ["r23 1", "k23 5", "14 72", "32 11", "23 61", "30 5", "18 9", "17 3"]
raging_lance = ["r24 1", "k24 5", "14 72", "32 11", "23 61", "30 5", "18 9", "17 3"]

composite_bow = ["25 1", "k25 5", "14 68", "25 33", "23 57", "30 5", "18 7", "17 3"]
lightning_bow = ["26 1", "k26 5", "14 72", "32 11", "23 61", "30 5", "18 9", "17 3"]
hailstorm_bow = ["27 1", "k27 5", "14 72", "32 11", "23 61", "30 5", "18 9", "17 3"]

imperial_axe = ["r28 1", "k28 5", "33 68", "25 33", "23 57", "18 7", "18 7", "17 3"]
skull_crusher = ["r29 1", "k29 5", "33 72", "32 11", "23 61", "30 5", "18 9", "17 3"]
dragon_mace = ["r30 1", "k30 5", "33 72", "32 11", "23 61", "30 5", "18 9", "17 3"]

ghost_dagger = ["r31 1", "k31 5", "33 15", "25 27", "23 15", "17 1", "18 3", "30 3"]
lion_knife = ["r32 1", "k32 5", "33 15", "25 27", "23 15", "17 1", "18 3", "30 3"]

recipes_armor = {"order": order, "hunter": hunter, "clarity": clarity, "crusader": crusader,
                 "royal": royal, "ghost": ghost, "lion": lion, "demon": demon, "divine": divine,
                 "durable": durable, "storm": storm, "blessed": blessed
                 }
recipes_weapon = {"champoin sword": champion_sword, "trident": trident, "hunter_bow": hunter_bow,
                  "war hammer": war_hammer, "hunter dagger": hunter_dagger, "thundersoul sword": thundersoul_sword,
                  "doomblade sword": doomblade_sword, "eclipse": eclipse, "guard's spear": guards_spear,
                  "king's defender": kings_defender, "raging lance": raging_lance, "composite bow": composite_bow,
                  "lightning bow": lightning_bow, "hailstorm bow": hailstorm_bow, "imperial axe": imperial_axe,
                  "skill crusher": skull_crusher, "dragon mace": dragon_mace, "ghost dagger": ghost_dagger,
                  "lion knife": lion_knife}

help_information_en = "Write \"/g ARMOR NAME\" or \"/g WEAPON NAME\" to get list of /g_withdraw commands for this item.\n\
For example: /g King's defender or /g Order Armor . \n\
Write \"/fg\" to easily find what you need for withdrawing.\n\
( All shields in armor and dagger in weapons )"

help_information = "Введите \"/g НАЗВАНИЕ БРОНИ\" или \"/g НАЗВАНИЕ ОРУЖИЯ\", что бы получить список /g_withdraw комманд для этого айтема. \n\
Например: /fwa King's defender или /fwa Order Armor . \n\
Введите \"/fg\" что бы легко найти нужный вам предмет и автоматически получить список /g_withdraw комманд\n\
( Все щиты в Броне и даггеры в Оружии )"

@bot.message_handler(commands=["fg"])
def start_button_fg(m):
    start_mes(m)

@bot.callback_query_handler(func=lambda call: True)
def first_mes(call):
    if call.data == "back":
        start_mes(call.message, False)
    elif call.data == "armor":
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Light", callback_data="light")
        b2 = types.InlineKeyboardButton(text="Robe", callback_data="robe")
        b3 = types.InlineKeyboardButton(text="Heavy", callback_data="heavy")
        b4 = types.InlineKeyboardButton(text="Back", callback_data="back")
        keyboard.add(b1, b2, b3, b4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="/g", reply_markup=keyboard)

    elif call.data == "light":
        if len(call.message.text.split(" ")) == 2:
            call.message.text = "/g"
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Hunter", callback_data="hunter")
        b2 = types.InlineKeyboardButton(text="Ghost", callback_data="ghost")
        b3 = types.InlineKeyboardButton(text="Lion", callback_data="lion")
        bb = types.InlineKeyboardButton(text="Back", callback_data="armor")
        keyboard.add(b1, b2, b3, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text, reply_markup=keyboard)

    elif call.data == "hunter" or call.data == "ghost" or call.data == "lion":
        if len(call.message.text.split(" ")) == 3:
            call.message.text = "/g " + call.message.text.split(" ")[1]
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Armor", callback_data="armor final")
        b2 = types.InlineKeyboardButton(text="Helmet", callback_data="helmet final")
        b3 = types.InlineKeyboardButton(text="Gloves", callback_data="gloves final")
        b4 = types.InlineKeyboardButton(text="Boots", callback_data="boots final")
        bb = types.InlineKeyboardButton(text="Back", callback_data="light")
        keyboard.add(b1, b2, b3, b4, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text + " " + call.data, reply_markup=keyboard)

    elif call.data == "robe":
        if len(call.message.text.split(" ")) == 2:
            call.message.text = "/g"
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Clarity", callback_data="clarity")
        b2 = types.InlineKeyboardButton(text="Demon", callback_data="demon")
        b3 = types.InlineKeyboardButton(text="Divine", callback_data="divine")
        bb = types.InlineKeyboardButton(text="Back", callback_data="armor")
        keyboard.add(b1, b2, b3, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text, reply_markup=keyboard)

    elif call.data == "clarity" or call.data == "demon" or call.data == "divine":
        if len(call.message.text.split(" ")) == 3:
            call.message.text = "/g " + call.message.text.split(" ")[1]
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Robe", callback_data="robe final")
        b2 = types.InlineKeyboardButton(text="Circlet", callback_data="circlet final")
        b3 = types.InlineKeyboardButton(text="Bracers", callback_data="bracers final")
        b4 = types.InlineKeyboardButton(text="Shoes", callback_data="shoes final")
        bb = types.InlineKeyboardButton(text="Back", callback_data="robe")
        keyboard.add(b1, b2, b3, b4, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text + " " + call.data, reply_markup=keyboard)

    elif call.data == "heavy":
        if len(call.message.text.split(" ")) == 2:
            call.message.text = "/g"
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Order", callback_data="order")
        b2 = types.InlineKeyboardButton(text="Crusader", callback_data="crusader")
        b3 = types.InlineKeyboardButton(text="Royal", callback_data="royal")
        bb = types.InlineKeyboardButton(text="Back", callback_data="armor")
        keyboard.add(b1, b2, b3, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text, reply_markup=keyboard)

    elif call.data == "order" or call.data == "crusader" or call.data == "royal":
        if len(call.message.text.split(" ")) == 3:
            call.message.text = "/g " + call.message.text.split(" ")[1]
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Armor", callback_data="armor final")
        b2 = types.InlineKeyboardButton(text="Helmet", callback_data="helmet final")
        b3 = types.InlineKeyboardButton(text="Gauntlets", callback_data="gauntlets final")
        b4 = types.InlineKeyboardButton(text="Boots", callback_data="boots final")
        b5 = types.InlineKeyboardButton(text="Shield", callback_data="shield final")
        bb = types.InlineKeyboardButton(text="Back", callback_data="heavy")
        keyboard.add(b1, b2, b3, b4, b5, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text + " " + call.data, reply_markup=keyboard)

    elif call.data == "weapon":
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Sword", callback_data="sword")
        b2 = types.InlineKeyboardButton(text="Bow", callback_data="bow")
        b3 = types.InlineKeyboardButton(text="Spear", callback_data="spear")
        b4 = types.InlineKeyboardButton(text="Blunt", callback_data="blunt")
        b5 = types.InlineKeyboardButton(text="Daggers", callback_data="dagger")
        b6 = types.InlineKeyboardButton(text="Back", callback_data="back")
        keyboard.add(b1, b2, b3, b4, b5, b6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="/g", reply_markup=keyboard)

    elif call.data == "sword":
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Champion Sword", callback_data="champion sword:final")
        b2 = types.InlineKeyboardButton(text="Thundersoul Sword", callback_data="thundersoul sword:final")
        b3 = types.InlineKeyboardButton(text="Doomblade Sword", callback_data="doomblade sword:final")
        b4 = types.InlineKeyboardButton(text="Eclipse", callback_data="eclipse:final")
        bb = types.InlineKeyboardButton(text="Back", callback_data="weapon")
        keyboard.add(b1, b2, b3, b4, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text, reply_markup=keyboard)

    elif call.data == "bow":
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Hunter Bow", callback_data="hunter bow:final")
        b2 = types.InlineKeyboardButton(text="Composite Bow", callback_data="composite bow:final")
        b3 = types.InlineKeyboardButton(text="Lightning Bow", callback_data="lightning bow:final")
        b4 = types.InlineKeyboardButton(text="Hailstorm Bow", callback_data="hailstorm bow:final")
        bb = types.InlineKeyboardButton(text="Back", callback_data="weapon")
        keyboard.add(b1, b2, b3, b4, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,
                              reply_markup=keyboard)

    elif call.data == "spear":
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Trident", callback_data="trident:final")
        b2 = types.InlineKeyboardButton(text="Guard's Spear", callback_data="guard's spear:final")
        b3 = types.InlineKeyboardButton(text="King's Defender", callback_data="king's defender:final")
        b4 = types.InlineKeyboardButton(text="Raging Lance", callback_data="raging lance:final")
        bb = types.InlineKeyboardButton(text="Back", callback_data="weapon:final")
        keyboard.add(b1, b2, b3, b4, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,
                              reply_markup=keyboard)

    elif call.data == "blunt":
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="War Hammer", callback_data="war hammer:final")
        b2 = types.InlineKeyboardButton(text="Imperial Axe", callback_data="imperial axe:final")
        b3 = types.InlineKeyboardButton(text="Skull Crusher", callback_data="skull crusher:final")
        b4 = types.InlineKeyboardButton(text="Dragon Mace", callback_data="dragon mace:final")
        bb = types.InlineKeyboardButton(text="Back", callback_data="weapon")
        keyboard.add(b1, b2, b3, b4, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,
                              reply_markup=keyboard)

    elif call.data == "dagger":
        keyboard = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="Hunter Dagger", callback_data="hunter dagger:final")
        b2 = types.InlineKeyboardButton(text="Ghost Dagger", callback_data="ghost dagger:final")
        b3 = types.InlineKeyboardButton(text="Lion Knife", callback_data="lion knife:final")
        bb = types.InlineKeyboardButton(text="Back", callback_data="weapon")
        keyboard.add(b1, b2, b3, bb)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,
                              reply_markup=keyboard)

    elif call.data.split(" ")[1] == "final":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text + " " + call.data.split(" ")[0])
        call.message.text += " " + call.data.split(" ")[0]
        get(call.message)
        
    elif call.data.split(":")[1] == "final":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.message.text + " " + call.data.split(":")[0])
        call.message.text += " " + call.data.split(":")[0]
        get(call.message)
        

@bot.message_handler(commands=['help_en'])
def help(m):
    bot.send_message(m.chat.id, help_information_en)
    

@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, help_information)
    
    
@bot.message_handler(commands=['counter'])
def count(m):
    if m.from_user.id == owner:
        bot.send_message(m.chat.id, counter)


@bot.message_handler(commands=['g'])
def get_fun(m):
    get(m)


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
