from http_settings.send_clients.http_client import HttpClient
from config.base_settings import base_api_settings
from data.constants import SMSReaderConstants


class SmsReaderClient(HttpClient):
    def __init__(self):
        super().__init__(path=base_api_settings.api.paths.sms_reader_path,
                         headers=SMSReaderConstants.HEADERS)

    def send(self, **kwargs):
        self.post(**kwargs)


sms_reader = SmsReaderClient()
