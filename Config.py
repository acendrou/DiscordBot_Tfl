import configparser
from os import environ as env

class Config:
    def __init__(self):
        self.tfl_app_key: str
        self.discordChannel_webhook_id: str
        self.discordChannel_webhook_token: str

class ConfigEnviron(Config):
    # for Heroku : the secrets (key for Tfl and Discord) are in the environment variables

    def __init__(self):
        self.tfl_app_key: str = env['tfl_key']
        self.discordChannel_webhook_id: str = env['discord_id']
        self.discordChannel_webhook_token: str = env['discord_token']


class ConfigRead(Config):
    def __init__(self, filename: str) -> None:
        self.config = configparser.ConfigParser()
        try:
            self.config.read(filename)
        except configparser.ParsingError:
            print("Parsing error")

        # Tfl API
        try:
            self.tfl_app_key: str = self.config['TFL_API']['app_key']
        except configparser.NoSectionError:
            print("TFL section not found")

        # Discord Webhook
        try:
            self.discordChannel_webhook_id: str = self.config['Discord_channel']['webhook_id']
            self.discordChannel_webhook_token: str = self.config['Discord_channel']['webhook_token']
        except configparser.NoSectionError:
            print("Discord section not found")
