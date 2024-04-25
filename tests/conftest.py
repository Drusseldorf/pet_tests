import pytest

from http_settings.send_clients.pay_in_h2h_client import pay_in_h2h
from http_settings.request_models.base_reqest_model import base_request_pay_in_model
from http_settings.send_clients.api_v2_payment_client import api_v2_get_payment


@pytest.fixture(scope='function')
def send_payin_h2h():
    response_h2h = pay_in_h2h.send(**base_request_pay_in_model.model_dump())
    return response_h2h


@pytest.fixture(scope='function')
def order_status(send_payin_h2h):
    return api_v2_get_payment.send(send_payin_h2h.id)
