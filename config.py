from dataclasses import dataclass
import os


ENV_BOT_TOKEN = "BOT_TOKEN"


@dataclass
class BotConfig:
    """Базовая конфигурация бота."""

    token: str


def load_config() -> BotConfig:
    """Загружает конфигурацию бота из переменных окружения."""

    token = os.getenv(ENV_BOT_TOKEN)
    if not token:
        raise ValueError(
            "Не удалось найти токен бота. Убедитесь, что переменная окружения "
            f"{ENV_BOT_TOKEN} задана."
        )

    return BotConfig(token=token)
