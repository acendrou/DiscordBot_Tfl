class DiscordFormat:

    def __init__(self, text: str) -> None:
        self.text: str = text

    def bold(self):
        self.text = "**" + self.text + "**"
        return self

    def italics(self):
        self.text = "*" + self.text + "*"
        return self

    def underline(self):
        self.text = "__" + self.text + "__"
        return self

    def quote(self):
        self.text = ">>> " + self.text
        return self

    def code(self):
        self.text = "```" + self.text + "```"
        return self

    # remove symbols from the text
    def clean(self):
        garbage_part = ['&#39;', '&lt;brgt;', '/&gt;', '&lt;br&lt;br']
        for g in garbage_part:
            self.text = self.text.replace(g, '')
        self.text = self.text.replace('&lt;br', ',')
        self.text = self.text.replace('&amp;', '&')
        return self
