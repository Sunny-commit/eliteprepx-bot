from telebot import types

def register_start_handler(bot):
    @bot.message_handler(commands=['start'])
    def start(msg):
        user = msg.from_user
        with open("data/users.txt", "a") as f:
            f.write(f"{user.first_name} (@{user.username}) - {user.id}\n")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("📘 GATE", "📗 JEE", "📕 NEET")
        markup.row("🤖 AI/ML", "💻 Interview Kits")
        markup.row("💎 Get Premium Access")

        bot.send_message(
            msg.chat.id,
            "👋 *Welcome to ElitePrepX!*\n\nSelect a category to get started 👇",
            parse_mode="Markdown",
            reply_markup=markup
        )
