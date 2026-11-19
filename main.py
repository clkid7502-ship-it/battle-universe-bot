
import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Добавь BOT_TOKEN в Secrets!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🧱 The Battle Bricks")
    kb.row("📸 Альянс и боты")
    kb.row("⚔️ Битвы", "ℹ️ О боте")

    bot.send_message(
        message.chat.id,
        "🔥 BATTLE UNIVERSE 🔥\n\n"
        "Добро пожаловать!\n"
        "Выбери свою вселенную:",
        reply_markup=kb
    )

@bot.message_handler(func=lambda m: True)
def menu(message):
    text = message.text
    chat = message.chat.id

    if text == "🧱 The Battle Bricks":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb.row("👹 Боссы", "⚔️ Баттлеры")
        kb.row("📖 Главы", "💀 Секреты")
        kb.row("⬅️ Назад")

        bot.send_message(chat, "🧱 THE BATTLE BRICKS", reply_markup=kb)

    elif text == "👹 Боссы":
        bot.send_message(
            chat,
            "👹 БОССЫ THE BATTLE BRICKS\n\n"
            "🎨 Paintmaster — 1000 HP\n"
            "🚀 Jetrock — 3000 HP\n"
            "🪣 Doombringer — 8000 HP\n"
            "🔴 Terminator — альт Paintmaster\n"
            "🔥 Hellfighter — альт Jetrock\n"
            "💀 Deathbringer — финальный босс Tumor"
        )

    elif text == "⚔️ Баттлеры":
        bot.send_message(
            chat,
            "⚔️ БАТТЛЕРЫ\n\n"
            "🗡️ Battler\n"
            "🧱 Trowel\n"
            "⚔️ Sword\n"
            "🔫 Slinger\n"
            "🛡️ Shield\n"
            "🎯 Sniper\n"
            "🔥 Fire\n"
            "❄️ Ice"
        )

    elif text == "📖 Главы":
        bot.send_message(
            chat,
            "📖 ГЛАВЫ\n\n"
            "1️⃣ Chapter 1\n"
            "2️⃣ Chapter 2\n"
            "3️⃣ Chapter 3\n"
            "4️⃣ Chapter 4\n"
            "5️⃣ Chapter 5"
        )

    elif text == "💀 Секреты":
        bot.send_message(
            chat,
            "💀 СЕКРЕТЫ\n\n"
            "Здесь будут секретные боссы,\n"
            "альтернативные формы и пасхалки!"
        )

    elif text == "📸 Альянс и боты":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb.row("📷 Камерамены", "🔊 Спикермены")
        kb.row("📺 ТВ-мены", "🤖 Титаны")
        kb.row("⬅️ Назад")

        bot.send_message(chat, "📸 АЛЬЯНС И БОТЫ", reply_markup=kb)

    elif text == "📷 Камерамены":
        bot.send_message(chat, "📷 КАМЕРАМЕНЫ\n\nЗдесь будет каталог камераменов!")

    elif text == "🔊 Спикермены":
        bot.send_message(chat, "🔊 СПИКЕРМЕНЫ\n\nЗдесь будет каталог спикерменов!")

    elif text == "📺 ТВ-мены":
        bot.send_message(chat, "📺 ТВ-МЕНЫ\n\nЗдесь будет каталог ТВ-менов!")

    elif text == "🤖 Титаны":
        bot.send_message(chat, "🤖 ТИТАНЫ\n\nЗдесь будут все титаны!")

    elif text == "⚔️ Битвы":
        bot.send_message(chat, "⚔️ АРЕНА\n\nСкоро здесь появятся битвы!")

    elif text == "ℹ️ О боте":
        bot.send_message(
            chat,
            "🔥 BATTLE UNIVERSE BOT v1.0\n\n"
            "Две вселенные в одном боте!\n"
            "Создатель: clkid7502-ship-it"
        )

    elif text == "⬅️ Назад":
        start(message)

    else:
        bot.send_message(chat, "Выбери раздел в меню 👇")

print("BATTLE UNIVERSE ЗАПУЩЕН!")
bot.infinity_polling()

