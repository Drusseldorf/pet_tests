import pytest

from http_settings.request_models.sms_reader_req_model import sms_reader_model
from http_settings.send_clients.pay_in_h2h_client import PayInH2HClient
from http_settings.request_models.base_reqest_model import base_request_pay_in_model
from http_settings.send_clients.api_v2_payment_client import ApiV2PaymentClient
from http_settings.send_clients.sms_reader_client import SmsReaderClient
from utils.model_helpers import set_amount_and_requisite


@pytest.fixture(scope='function')
def send_payin_h2h():
    pay_in_h2h = PayInH2HClient()
    return pay_in_h2h.send(base_request_pay_in_model)


@pytest.fixture(scope='function')
def order_status(send_payin_h2h, payment_status_client):
    return payment_status_client.send(send_payin_h2h.id)


@pytest.fixture(scope='function')
def prepare_sms_reader_model(order_status):
    set_amount_and_requisite(sms_reader_model, order_status.payment.amount,
                             order_status.payment.paymentRequisite.requisite)


@pytest.fixture(scope='function')
def payment_status_client():
    return ApiV2PaymentClient()


@pytest.fixture(scope='function')
def sms_reader_client():
    return SmsReaderClient()
