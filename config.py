from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    database_user: SecretStr
    database_password: SecretStr
    database_host: SecretStr
    database_port: SecretStr
    database_name: SecretStr
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

config = Settings()
