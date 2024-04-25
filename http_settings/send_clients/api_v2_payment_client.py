from config.base_settings import base_api_settings
from http_settings.send_clients.http_client import HttpClient
from http_settings.response_models.api_v2_payments_resp_model import ApiV2ResponseModel
from utils.model_helpers import get_validated_model


class ApiV2Payment(HttpClient):
    def __init__(self):
        super().__init__(path=base_api_settings.api.paths.api_v2_payment)

    def send(self, order_id) -> ApiV2ResponseModel:
        self.path += order_id
        response = self.get()
        return get_validated_model(response, ApiV2ResponseModel)


api_v2 = ApiV2Payment()
