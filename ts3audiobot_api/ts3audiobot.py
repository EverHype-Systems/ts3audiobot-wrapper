from ts3audiobot_api.ts3commandcaller import CommandCaller
import base64
import requests


def generate_base64(string):
    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


class TS3AudioBot:
    """
    creates the node connection
    """

    def __init__(self, ip, api_token, port=58913, timeout=5):
        """
        Initialization of Node Class
        :param api_token: string
        :param ip:
        :param port:
        :param timeout:
        """

        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.api_token = api_token
        self.username = api_token.split(":")[0]
        self.access_token = api_token.split(":")[1]
        self.commandExecutor = CommandCaller(self)
        self.bot_id = 0

        self.base.raw = "http://{ip}:{port}/api/{endpoint}".format(ip=ip, port=port)
        self.base.normal = "http://{ip}:{port}/api/bot/use/{bot_id}/{endpoint}".format(ip=ip, port=port)

    def generate_header(self):
        return "Basic {username}:{access_token}".format(username=generate_base64(self.username),
                                                        access_token=generate_base64(self.access_token))

    def request(self, endpoint):

        r = requests.get(self.base.normal.format(endpoint=endpoint), headers={
            "Authorization": self.generate_header(),
        }, timeout=self.timeout)

        return r.json()

    def raw_request(self, endpoint):

        r = requests.get(self.base.raw.format(endpoint=endpoint), headers={
            "Authorization": self.generate_header(),
        }, timeout=self.timeout)

        return r.json()

    def get_command_executor(self):
        return self.commandExecutor

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_current_id(self):
        return self.bot_ids

