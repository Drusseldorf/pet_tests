from config.base_settings import base_api_settings


class PayInH2HConstants:
    FAIL_URL: str = 'https://example.com'
    SUCCESS_URL: str = 'https://example.com'
    CALLBACK_URL: str = 'https://example.com'
    HEADERS: dict = {'SECRET-TOKEN': base_api_settings.api.company.company_token,
                     'Content-Type': 'application/json'}


class SMSReaderConstants:
    ID: str = '123321'
    SENDER: str = 'some_sender'
    DEVICE_ID: str = '123123123'
    TEXT: str = 'Перевод на сумму {} по карте {}'
