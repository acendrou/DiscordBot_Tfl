from Config import ConfigEnviron
from TflApi import TflApi
from DiscordWebhook import DiscordWebhook
from DiscordFormat import DiscordFormat


def air_quality(tfl: TflApi, discord_tfl: DiscordWebhook) -> None:
    summaries, texts = tfl.air_quality()
    for summary, text in zip(summaries, texts):
        discord_tfl.send_message(DiscordFormat(summary).quote().italics().text, "AirQuality")
        discord_tfl.send_message(DiscordFormat(text).clean().bold().text, "AirQuality")


def arrival_time(tfl: TflApi, discord_tfl: DiscordWebhook) -> None:
    mess: str = tfl.find_next_arrival_by_tube("")
    discord_tfl.send_message(mess, "Arrival")


def main():
    #config_data = ConfigRead('config.ini')
    config_data = ConfigEnviron()

    discord_tfl = DiscordWebhook(config_data.discordChannel_webhook_id, config_data.discordChannel_webhook_token)
    discord_tfl.send_message("Start", username="tfl-api")

    tfl = TflApi(config_data.tfl_app_key)

    air_quality(tfl, discord_tfl)

    #arrival_time(tfl, discord_tfl)

    discord_tfl.send_message("Stop", username="tfl-api")

if __name__ == '__main__':
    main()
