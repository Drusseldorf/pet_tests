from http_settings.clients.http_client import HttpClient
from config.base_settings import base_api_settings
from data.constants import SMSReaderConstants


class SmsReaderClient(HttpClient):
    def __init__(self):
        super().__init__(path=base_api_settings.api.paths.sms_reader_path,
                         headers=SMSReaderConstants.HEADERS)

    def send(self, payload):
        self.post(payload)
