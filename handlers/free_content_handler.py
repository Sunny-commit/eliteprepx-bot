def register_free_handlers(bot):
    @bot.message_handler(func=lambda m: m.text and m.text.lower().strip() in ["📘 gate", "📗 jee", "📕 neet", "🤖 ai/ml", "💻 interview kits"])
    def send_free_content(msg):
        content_links = {
            "📘 gate": "https://your-gate-link",
            "📗 jee": "https://your-jee-link",
            "📕 neet": "https://your-neet-link",
            "🤖 ai/ml": "https://your-ml-link",
            "💻 interview kits": "https://your-interview-link",
        }
        bot.reply_to(msg, content_links[msg.text.lower().strip()])
