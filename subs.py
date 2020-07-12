from random import sample, randint, choice
import pyautogui
from time import sleep

emote_repeat_chance = 50
emote_change_chance = 10
msg_limit = 260
bot_time_min, bot_time_max = 60, 300
bot_names = ["fanfic.bot"]

emote_list = ["4Head", "KappaWealth", "KonCha", "Kreygasm", 
              "ANELE", "KappaPride", "LUL", "LesbianPride",
              "ArgieB8", "KappaClaus", "MaxLOL", "NotLikeThis",
              "ArsonNoSexy", "Keepo", "PJSalt", "SeriousSloth",
              "AsianGlow", "Kappa", "TearGlove", "VoHiYo",
              "AsexualPride", "KappaRoss", "riPepperonis",
              "BabyRage", "ItsBoshyTime", ":)", ":(", ":o", ":z",
              "BibleThump", "GivePLZ", "B)", ":\\", ";)", ";p", 
              "BrokeBack", "FrankerZ", ":p", "R)", "o_O", ":D",
              "ChefFrank", "DarkMode", ">(", "CorgiDerp"]

bots = {}
screenWidth, screenHeight = pyautogui.size()

for b in range(0, len(bot_names)):
    f = open(bot_names[b], "r")
    bots[b] = list(dict.fromkeys(f.read().split("\n")))
    f.close()


def spice_msg(msg):
    emote = choice(emote_list)
    spam = " "
    while randint(0, 100) < emote_repeat_chance:
        spam += emote + " "
        if randint(0, 100) < emote_change_chance:
            emote = choice(emote_list)
    return msg + spam


def get_msg(base):
    msg = sample(base, 1)[0].strip()
    if len(msg) >= msg_limit:
        msgs = msg.split(".")
        msgs = [m for m in msgs if len(m) > 2]
        msg = sample(msgs, 1)[0].strip()

    msg = msg.strip("\"").rstrip("\"")
    return spice_msg(msg)


def select_bot(bot_id, num_bots, msg):
    chorinho = screenWidth//10
    chat_position_x = (screenWidth//num_bots)*bot_id + chorinho
    chat_position_y = screenHeight - 70
    pyautogui.moveTo(chat_position_x, chat_position_y)
    pyautogui.click()
    pyautogui.write(msg)


while True:
	who = randint(0,len(bots)-1)
	time_to_talk = randint(bot_time_min, bot_time_max)
	sleep(time_to_talk)
	select_bot(who, len(bots), get_msg(bots[who]))
	pyautogui.press('enter')
