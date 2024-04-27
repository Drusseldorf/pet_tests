import allure
from http_settings.request_models.sms_reader_req_model import sms_reader_model
from data.constants import Status


@allure.epic('SMS reader')
class TestSMSReader:

    @allure.title('Считывание по последним 4-м цифрам реквизита')
    def test_sms_reader(self,
                        send_payin_h2h,
                        order_status,
                        prepare_sms_reader_model,
                        payment_status_client,
                        sms_reader_client):

        sms_reader_client.send(sms_reader_model)
        status_after_request = payment_status_client.send().payment.status

        assert status_after_request == Status.SUCCESS, \
            f'ORDER ID = {order_status.payment.id}'
