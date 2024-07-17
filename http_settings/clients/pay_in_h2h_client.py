from http_settings.clients.http_client import HttpClient
from config.base_settings import base_api_settings
from data.constants import PayInH2HConstants
from http_settings.response_models.pay_in_h2h_resp_model import PayInH2HResponse
from utils.model_helpers import get_validated_model


class PayInH2HClient(HttpClient):
    def __init__(self):
        super().__init__(path=base_api_settings.api.paths.pay_in_h2h_path,
                         headers=PayInH2HConstants.HEADERS)

    def send(self, payload) -> PayInH2HResponse:
        response = self.post(payload)
        return get_validated_model(response, PayInH2HResponse)
