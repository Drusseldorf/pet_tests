from pydantic import BaseModel
import uuid

from config.base_settings import base_api_settings
from utils.signature import calculate_signature
from data.constants import PayInH2HConstants


class BaseRequestPayInModel(BaseModel):
    company_id: str = base_api_settings.api.company.company_id
    external_id: str = str(uuid.uuid4())
    order_number: str = str(uuid.uuid4())
    amount: int = base_api_settings.api.defoult_data.defoult_amount
    fail_url: str = PayInH2HConstants.FAIL_URL
    success_url: str = PayInH2HConstants.SUCCESS_URL
    callback_url: str = PayInH2HConstants.CALLBACK_URL
    currency: str = base_api_settings.api.defoult_data.defoult_currency
    client_id: str = str(uuid.uuid4())
    direct_method: str = base_api_settings.api.defoult_data.defoult_method
    signature: str = ''

    def __init__(self):
        super().__init__()
        self.sign()

    def sign(self):
        amount = str(self.amount)
        base_data_dict = self.model_dump(exclude_none=True)
        del base_data_dict['signature']
        base_data_dict['amount'] = amount
        token = base_api_settings.api.company.company_token
        self.signature = calculate_signature(base_data_dict, token)


base_request_pay_in_model = BaseRequestPayInModel()
