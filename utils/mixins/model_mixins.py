import hashlib

from config.base_settings import base_api_settings


class SugnatureMixin:
    def __init__(self):
        self.sign()

    def sign(self):
        amount = str(self.amount)
        base_data_dict = self.model_dump(exclude_none=True)
        del base_data_dict['signature']
        base_data_dict['amount'] = amount
        token = base_api_settings.api.company.company_token
        self.signature = self.calculate_signature(base_data_dict, token)

    @staticmethod
    def calculate_signature(json_body: dict, token: str) -> str:
        sorted_dict_values = ''.join(str(value) for _, value in sorted(json_body.items()))
        signature = hashlib.sha512((sorted_dict_values + token).encode('utf-8')).hexdigest()
        return signature
