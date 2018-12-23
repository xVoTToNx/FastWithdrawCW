import telebot

bot = telebot.TeleBot("781020407:AAGieeeecXl0hoscL3QWCGnXkD9FielXwG0")
owner = 458619004

order = {
    "armor":     ["r06 1", "k06 3", "33 15", "31 12", "23 9", "16 5", "28 3", "15 3"],
    "helmet":    ["r07 1", "k07 3", "33 12", "31 9", "23 7", "16 3", "28 2", "15 1"],
    "boots":     ["r08 1", "k08 3", "33 9", "31 7", "23 5", "16 1", "28 1", "15 3"],
    "gauntlets": ["r09 1", "k09 3", "33 9", "31 7", "23 5", "16 1", "28 1", "15 3"],
    "shield":    ["r10 1", "k10 3", "33 7", "25 15", "23 7", "28 1"]
        }
hunter = {
    "armor":     ["r11 1", "k11 3", "20 24", "31 12", "23 9", "16 5", "28 3", "15 3"],
    "helmet":    ["r12 1", "k12 3", "20 18", "31 9", "23 7", "16 3", "28 2", "15 1"],
    "boots":     ["r13 1", "k13 3", "20 12", "31 7", "23 5", "16 1", "28 1"],
    "gloves":    ["r14 1", "k14 3", "20 12", "31 7", "23 5", "16 1", "28 1"]
        }
clarity = {
    "robe":      ["r15 1", "k15 3", "20 15", "31 12", "23 9", "16 7", "28 3", "15 5"],
    "circlet":   ["r16 1", "k16 3", "20 9", "31 9", "23 7", "16 5", "28 2", "15 3"],
    "shoes":     ["r17 1", "k17 3", "20 7", "31 5", "23 3", "16 3", "28 1", "15 1"],
    "bracers":   ["r18 1", "k18 3", "20 7", "31 5", "23 3", "16 3", "28 1", "15 1"]
        }
crusader = {
    "armor":     ["r33 1", "k33 5", "34 32", "31 17", "23 13", "16 15", "29 5", "15 9"],
    "helmet":    ["r34 1", "k34 5", "34 27", "31 12", "23 9", "16 7", "29 3", "15 5"],
    "boots":     ["r35 1", "k35 5", "34 21", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "gauntlets": ["r36 1", "k36 5", "34 21", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "shield":    ["r37 1", "k37 5", "33 15", "25 27", "23 15", "29 3", "15 3", "16 7"]
        }
royal = {
    "armor":     ["r38 1", "k38 5", "34 32", "31 17", "23 13", "16 15", "29 5", "15 9"],
    "helmet":    ["r39 1", "k39 5", "34 27", "31 12", "23 9", "16 7", "29 3", "15 5"],
    "boots":     ["r40 1", "k40 5", "34 21", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "gauntlets": ["r41 1", "k41 5", "34 21", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "shield":    ["r42 1", "k42 5", "33 15", "25 27", "23 15", "29 3", "15 3", "16 7"]
        }
ghost = {
    "armor":     ["r43 1", "k43 5", "35 18", "31 17", "23 13", "16 15", "29 5", "15 9"],
    "helmet":    ["r44 1", "k44 5", "35 14", "31 12", "23 9", "16 7", "29 3", "15 5"],
    "boots":     ["r45 1", "k45 5", "35 11", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "gloves":    ["r46 1", "k46 5", "35 11", "31 9", "23 7", "16 3", "29 1", "15 1"]
        }
lion = {
    "armor":     ["r47 1", "k47 5", "35 18", "31 17", "23 13", "16 15", "29 5", "15 9"],
    "helmet":    ["r48 1", "k48 5", "35 14", "31 12", "23 9", "16 7", "29 3", "15 5"],
    "boots":     ["r49 1", "k49 5", "35 11", "31 9", "23 7", "16 3", "29 1", "15 1"],
    "gloves":    ["r50 1", "k50 5", "35 11", "31 9", "23 7", "16 3", "29 1", "15 1"]
        }
demon = {
    "robe":      ["r51 1", "k51 5", "35 11", "31 17", "23 13", "16 21", "29 5", "15 12"],
    "circlet":   ["r52 1", "k52 5", "35 8", "31 12", "23 9", "16 16", "29 3", "15 9"],
    "shoes":     ["r53 1", "k53 5", "35 5", "31 7", "23 7", "16 7", "29 1", "15 5"],
    "bracers":   ["r54 1", "k54 5", "35 5", "31 7", "23 7", "16 7", "29 1", "15 5"]
        }
divine = {
    "robe":      ["r55 1", "k55 5", "35 11", "31 17", "23 13", "16 21", "29 5", "15 12"],
    "circlet":   ["r56 1", "k56 5", "35 8", "31 12", "23 9", "16 16", "29 3", "15 9"],
    "shoes":     ["r57 1", "k57 5", "35 5", "31 7", "23 7", "16 7", "29 1", "15 5"],
    "bracers":   ["r58 1", "k58 5", "35 5", "31 7", "23 7", "16 7", "29 1", "15 5"]
        }
durable = {
    "cloak":     ["r60 1", "k60 3", "35 5", "31 3", "23 5", "16 3", "29 1", "15 1"]
        }
storm = {
    "cloak":     ["r59 1", "k59 3", "35 5", "31 3", "23 5", "16 3", "29 1", "15 1"]
        }
blessed = {
    "cloak":     ["r61 1", "k61 3", "35 5", "31 3", "23 5", "16 3", "29 1", "15 1"]
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

recipes_armor = {"order":order, "hunter":hunter, "clarity":clarity, "crusader":crusader,
                 "royal":royal, "ghost":ghost, "lion":lion, "demon":demon, "divine":divine,
                 "durable":durable, "storm":storm, "blessed": blessed
                 }
recipes_weapon = {"champoin sword":champion_sword, "trident":trident, "hunter_bow":hunter_bow,
                  "war hammer":war_hammer, "hunter dagger":hunter_dagger, "thundersould sword":thundersoul_sword,
                  "doomblade sword":doomblade_sword, "eclipse":eclipse, "guard's spear":guards_spear,
                  "king's defender":kings_defender, "raging lance":raging_lance, "composite bow":composite_bow,
                  "lightning bow":lightning_bow, "hailstorm bow":hailstorm_bow, "imperial axe":imperial_axe,
                  "skill crusher":skull_crusher, "dragon mace":dragon_mace, "ghost dagger":ghost_dagger,
                  "lion knife":lion_knife}

@bot.message_handler(commands=['fwa'])
def fwa(m):
    item = m.text.split(' ').lower()
    for element in recipes_armor[item[1]][item[2]]:
        bot.send_message(m.chat.id, "/g_receive " + element)


@bot.message_handler(commands=['fww'])
def fww(m):
    item = m.text.split(' ').lower()
    if item[2]:
        for element in recipes_weapon[item[1] + " " + item[2]]:
            bot.send_message(m.chat.id, "/g_receive " + element)
    else:
        for element in recipes_weapon[item[1]]:
            bot.send_message(m.chat.id, "/g_receive " + element)

@bot.message_handler(content_types=['text'])
def sdfs(m):
    bot.send_message(m.chat.id, m.text)
    item = u'' + m.text.split(' ').lower()
    bot.send_message(m.chat.id, item)

def main():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()
