import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from config import load_config


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает команду /start."""

    if update.message is None:
        logger.debug("Получено событие без сообщения на /start")
        return

    await update.message.reply_text("Привет! Я echo-бот. Отправь мне что-нибудь, и я повторю.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет пользователю ответ с тем же текстом."""

    if update.message is None or update.message.text is None:
        logger.debug("Получено событие без текста для echo")
        return

    await update.message.reply_text(update.message.text)


def main() -> None:
    """Точка входа для запуска бота."""

    config = load_config()

    application = Application.builder().token(config.token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("Бот запущен. Ожидание сообщений...")
    application.run_polling()


if __name__ == "__main__":
    main()
