from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# =========================================
# НАЛАШТУВАННЯ
# =========================================

TOKEN = "8699125376:AAFkgEplkoxNNACGH7xNRLT1TZxIb_i8fQ8"
ADMIN_ID = 123456789  # <-- вставь свой Telegram ID

# =========================================
# КНОПКИ
# =========================================

main_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📚 Курси"), KeyboardButton("💰 Ціна")],
        [KeyboardButton("✂️ З нуля"), KeyboardButton("📝 Запис")],
        [KeyboardButton("❓ Підвищення"), KeyboardButton("📞 Адміністратор")],
    ],
    resize_keyboard=True
)

courses_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("✂️ Повний курс")],
        [KeyboardButton("🎨 Колористика"), KeyboardButton("✂️ Стрижки")],
        [KeyboardButton("🔥 Підвищення кваліфікації")],
        [KeyboardButton("⬅️ Назад у меню")],
    ],
    resize_keyboard=True
)

# =========================================
# ДОПОМОГА: НАДІСЛАТИ АДМІНУ
# =========================================

async def send_to_admin(context: ContextTypes.DEFAULT_TYPE, text: str):
    try:
        await context.bot.send_message(chat_id=ADMIN_ID, text=text)
    except Exception as e:
        print("Помилка надсилання адміну:", e)

# =========================================
# /start
# =========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"Привіт, {user.first_name} 💛\n\n"
        "Хочеш стати перукарем чи прокачати навички?\n"
        "Я допоможу підібрати курс 😊",
        reply_markup=main_keyboard
    )

# =========================================
# ОБРОБКА КНОПОК
# =========================================

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Курси":
        await update.message.reply_text(
            "Ось наші курси 💛\n\n"
            "1. ✂️ Повний курс з нуля — 18 занять\n"
            "2. 🎨 Колористика — 9 занять\n"
            "3. ✂️ Стрижки — 8 занять\n"
            "4. 🔥 Підвищення кваліфікації\n\n"
            "Що тебе цікавить? 😊",
            reply_markup=courses_keyboard
        )

    elif text == "💰 Ціна":
        await update.message.reply_text(
            "💰 Ось актуальні ціни:\n\n"
            "✂️ Повний курс — 20 000 грн\n"
            "🎨 Колористика — 10 000 грн\n"
            "✂️ Стрижки — 10 000 грн"
        )

    elif text == "✂️ З нуля":
        await update.message.reply_text(
            "Тоді тобі підійде повний курс ✂️\n"
            "18 занять, практика, групи до 6 людей"
        )

    elif text == "📝 Запис":
        await update.message.reply_text(
            "📝 Щоб забронювати місце — потрібно внести передоплату 10% 💛\n\n"
            "XXXX XXXX XXXX XXXX"
        )

    elif text == "❓ Підвищення":
        await update.message.reply_text(
            "🔥 Підвищення кваліфікації\n\n"
            "• AirTouch\n"
            "• Вихід з чорного\n"
            "• Складні техніки"
        )

    elif text == "📞 Адміністратор":
        await update.message.reply_text(
            "Добре 💛 Адміністратор скоро з вами зв’яжеться 😊"
        )

    elif text == "✂️ Повний курс":
        await update.message.reply_text(
            "✂️ Повний курс з нуля\n\n"
            "• 18 занять\n"
            "• Практика на моделях\n"
            "• Міні-групи до 6 людей\n"
            "💰 20 000 грн"
        )

    elif text == "🎨 Колористика":
        await update.message.reply_text(
            "🎨 Базова колористика\n\n"
            "• 9 занять\n"
            "💰 10 000 грн"
        )

    elif text == "✂️ Стрижки":
        await update.message.reply_text(
            "✂️ Базові стрижки\n\n"
            "• 8 занять\n"
            "💰 10 000 грн"
        )

    elif text == "🔥 Підвищення кваліфікації":
        await update.message.reply_text(
            "🔥 Підвищення кваліфікації\n"
            "Вартість уточнюється індивідуально"
        )

    elif text == "⬅️ Назад у меню":
        await update.message.reply_text(
            "Повертаю в головне меню 💛",
            reply_markup=main_keyboard
        )

# =========================================
# ЗАПУСК
# =========================================

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()