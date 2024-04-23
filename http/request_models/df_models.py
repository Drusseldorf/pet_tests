from pydantic import BaseModel
from utils.signature import calculate_signature


# class BaseRequestModel(BaseModel):
#     company_id: str = PayInData.DEFAULT_COMPANY_ID
#     external_id: Optional[str] = None
#     order_number: str = PayInData.ORDER_NUMBER
#     amount: int = 10000
#     fail_url: str = PayInData.PAYMENT_FAILURE_URL
#     success_url: str = PayInData.PAYMENT_SUCCESS_URL
#     callback_url: str = PayInData.CALLBACK_URL
#     direct_method: str | None = None
#     currency: str = Currencies.KZT
#     client_id: str = PayInData.CLIENT_ID
#     customer_requisite: str = "4111111111111111"
#     signature: str = ""
#
#     def sign(self, token: str) -> None:
#         pay_in_dict = self.model_dump(exclude_none=True)
#         del pay_in_dict["signature"]
#         self.signature = calculate_signature(pay_in_dict, token)
