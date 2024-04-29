import allure
from assertpy import assert_that
from http_settings.response_models.pay_in_h2h_resp_model import PayInH2HResponse


@allure.epic('PayInH2H')
class TestPayIn:

    @allure.title('Соответствие модели ответа PayInH2H')
    def test_pay_in_h2h_response(self, pay_in_h2h, pay_in_req_model):

        pay_in_h2h_response = pay_in_h2h.send(pay_in_req_model)

        assert_that(pay_in_h2h_response).is_instance_of(PayInH2HResponse)
