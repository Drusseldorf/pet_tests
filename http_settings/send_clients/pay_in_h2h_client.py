from http_settings.send_clients.http_client import HttpClient
from http_settings.request_models.base_reqest_model import base_request_pay_in_model
from config.base_settings import base_api_settings
from data.constants import PayInH2HConstants
from http_settings.response_models.pay_in_h2h_resp_model import PayInH2HResponse
from utils.model_helpers import get_validated_model


class PayInH2HClient(HttpClient):
    def __init__(self):
        super().__init__(path=base_api_settings.api.paths.pay_in_h2h_path,
                         headers=PayInH2HConstants.HEADERS)

    def send(self, **kwargs) -> PayInH2HResponse:
        response = self.post(**kwargs)
        return get_validated_model(response, PayInH2HResponse)


pay_in_h2h = PayInH2HClient()

print(pay_in_h2h.send(json=base_request_pay_in_model.model_dump()))
