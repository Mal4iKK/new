import asyncio

from telegram import Bot, Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes
from credits import bot_token

bot = Bot(token=bot_token)

class MyBot:
    def __init__(self, bot_token):
        self.application = Application.builder().token(bot_token).build()

        # Регистрируем обработчики команд
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("info", self.info))
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        print(user.mention_html())
        await update.message.reply_text(
            f"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    async def info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(text="я начинающий разраб из шыма.")


if __name__ == "__main__":
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    bot = MyBot(bot_token=bot_token)