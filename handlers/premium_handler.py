import json
import os

ADMIN_ID = int(os.getenv("ADMIN_ID"))

def register_premium_handlers(bot):
    @bot.message_handler(func=lambda m: m.text and "premium" in m.text.lower())
    def show_premium(msg):
        with open("config/premium_config.json") as f:
            prices = json.load(f)

        response = "💎 *ElitePrepX Premium Access*\n\n"
        for subject, price in prices.items():
            response += f"📘 {subject} – ₹{price}\n"
        response += "\n💰 UPI ID: `patetichandu@oksbi`\n📸 Send payment screenshot after transfer."
        bot.reply_to(msg, response, parse_mode="Markdown")

    @bot.message_handler(content_types=['photo', 'document'])
    def handle_payment_screenshot(msg):
        user = msg.from_user
        caption = msg.caption if msg.caption else "No caption"
        bot.forward_message(chat_id=ADMIN_ID, from_chat_id=msg.chat.id, message_id=msg.message_id)
        bot.send_message(ADMIN_ID, f"📸 Screenshot by @{user.username or 'NoUsername'} ({user.id})\n📝 {caption}")
        bot.reply_to(msg, "✅ Screenshot received! We'll verify and send your content soon.")
