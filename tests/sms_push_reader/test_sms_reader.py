import allure
from assertpy import assert_that

from data.constants import Status


@allure.epic('SMS reader')
class TestSMSReader:

    @allure.title('Считывание по последним 4-м цифрам реквизита')
    def test_sms_reader(self,
                        send_payin_h2h,
                        order_status,
                        prepare_sms_reader_model,
                        payment_status_client,
                        sms_reader_client,
                        sms_reader_model):

        sms_reader_client.send(sms_reader_model)
        status_after_request = payment_status_client.send().payment.status

        assert_that(status_after_request).\
            described_as(f'ORDER ID = {order_status.payment.id}').\
            is_equal_to(Status.SUCCESS)
