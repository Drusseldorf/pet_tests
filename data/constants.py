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
    DEVICE_ID: str = 'f2f7a6a4c66195e652e17673'
    TEXT: str = 'Перевод на сумму {} по карте {}'
    HEADERS: dict = {'Content-Type': 'application/json'}


class Status:
    SUCCESS: str = 'success'
