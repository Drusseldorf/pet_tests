from pydantic import BaseModel

from data.constants import SMSReaderConstants
from config.base_settings import base_api_settings


class SmsReaderModel(BaseModel):
    id: str = SMSReaderConstants.ID
    sender: str = SMSReaderConstants.SENDER
    device_id: str = SMSReaderConstants.DEVICE_ID
    text: str = SMSReaderConstants.TEXT
    operator_token: str = base_api_settings.api.operators.operator_token
    requisite: str

    def set_amount_and_requisite(self, amount: str, requisite: str):
        self.text = self.text.format(amount, requisite[-4:])
        self.requisite = requisite


sms_reader_model = SmsReaderModel()
