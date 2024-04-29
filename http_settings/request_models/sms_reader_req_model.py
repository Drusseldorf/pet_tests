from pydantic import BaseModel

from data.constants import SMSReaderConstants
from config.base_settings import base_api_settings


class SmsReaderModel(BaseModel):
    id: str = SMSReaderConstants.ID
    sender: str = SMSReaderConstants.SENDER
    device_id: str = SMSReaderConstants.DEVICE_ID
    text: str = SMSReaderConstants.TEXT
    operator_token: str = base_api_settings.api.operators.operator_token
    requisite: str | None = None
