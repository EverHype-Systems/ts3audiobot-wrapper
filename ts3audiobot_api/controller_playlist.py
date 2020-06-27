from urllib.parse import urlparse


def is_url(link):
    """
    Check if link is valid
    """
    try:
        result = urlparse(link)
        if all([result.scheme, result.netloc]):
            return True
    except ValueError:
        return False


class Playlist:

    def __init__(self, ts3audiobot):
        self.ts3audiobot = ts3audiobot

    def add(self, link):
        if is_url(link):
            return self.ts3audiobot.request("list/add/{}".format(link))
        else:
            return False

    def clear(self):
        return self.ts3audiobot.request("list/clear")

    def delete(self):
        return self.ts3audiobot.request("delete")

    def get(self):
        return self.ts3audiobot.request("list/get")

    def item_move(self):
        return self.ts3audiobot.request("list/item/move")

    def item_delete(self):
        return self.ts3audiobot.request("list/item/delete")

    def list(self):
        return self.ts3audiobot.request("list/list")

    def load(self):
        return self.ts3audiobot.request("list/load")

    def merge(self):
        return self.ts3audiobot.request("list/merge")

    def rename(self):
        return self.ts3audiobot.request("list/name")

    def play(self):
        return self.ts3audiobot.request("list/play")

    def play_from(self, index):
        return self.ts3audiobot.request("list/play/{}".format(index))

    def get_queue(self):
        return self.ts3audiobot.request("list/queue")

    def save(self):
        return self.ts3audiobot.request("list/save")

    def show(self):
        return self.ts3audiobot.request("list/show")

    def random(self):
        return self.ts3audiobot.request("random")

    def enable_random(self):
        return self.ts3audiobot.request("random/on")

    def disable_random(self):
        return self.ts3audiobot.request("random/off")
