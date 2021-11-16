import requests


class DiscordWebhook:
    base_url: str = "https://discord.com/api/webhooks/"

    def __init__(self, webhook_id: str, webhook_token: str, username: str = "default_DiscordWebhook") -> None:
        self.url: str = self.base_url + webhook_id + "/" + webhook_token
        self.username_default: str = username

    def send_message(self, message: str, username: str = None) -> None:
        if username is None:
            username = self.username_default
        requests.post(self.url, data={'content': message, 'username': username})
