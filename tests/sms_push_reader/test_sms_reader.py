from http_settings.request_models.sms_reader_req_model import sms_reader_model
from http_settings.send_clients.sms_reader_client import sms_reader
from http_settings.send_clients.api_v2_payment_client import api_v2_get_payment
from data.constants import Status


class TestSMSReader:

    def test_sms_reader(self, send_payin_h2h, order_status):

        sms_reader_model.set_amount_and_requisite(order_status.payment.amount,
                                                  order_status.payment.paymentRequisite.requisite)

        sms_reader.send(**sms_reader_model.model_dump())

        status_after_request = api_v2_get_payment.send().payment.status

        assert status_after_request == Status.SUCCESS
