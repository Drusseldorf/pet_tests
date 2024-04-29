import random as r
from pydantic import BaseModel
import uuid

from config.base_settings import base_api_settings
from utils.mixins.model_mixins import SugnatureMixin
from data.constants import PayInH2HConstants


class BaseRequestPayInModel(BaseModel, SugnatureMixin):
    def __init__(self):
        super().__init__()
        self.external_id = str(uuid.uuid4())
        self.order_number = str(uuid.uuid4())
        self.client_id = str(uuid.uuid4())
        self.amount = r.randint(300, 50000) * 100
        self.sign()

    company_id: str = base_api_settings.api.company.company_id
    amount: int = base_api_settings.api.defoult_data.defoult_amount
    fail_url: str = PayInH2HConstants.FAIL_URL
    success_url: str = PayInH2HConstants.SUCCESS_URL
    callback_url: str = PayInH2HConstants.CALLBACK_URL
    currency: str = base_api_settings.api.defoult_data.defoult_currency
    direct_method: str = base_api_settings.api.defoult_data.defoult_method
    external_id: str | None = None
    order_number: str | None = None
    client_id: str | None = None
    signature: str = ''
