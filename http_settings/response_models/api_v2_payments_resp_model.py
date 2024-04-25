from typing import List
from pydantic import BaseModel


class PaymentMethod(BaseModel):
    code: str
    displayedName: str
    type: str
    isPopular: bool | None = None
    extraRequisiteForQr: str | None = None
    imageUrl: str | None = None


class PaymentRequisite(BaseModel):
    bankName: str
    requisite: str
    holder: str | None = None


class Payment(BaseModel):
    id: str
    status: str
    amount: int
    toBePaid: float
    companyId: str
    failUrl: str
    successUrl: str
    customerFullName: str | None = None
    customerRequisite: str | None = None
    timeLeft: int
    expiresAt: str
    createdAt: str
    declinedByClient: bool
    supportRequestId: str | None = None
    clientId: str | None = None
    paymentPageDesignId: str | None = None
    lineMethod: bool
    paymentMethod: PaymentMethod
    paymentRequisite: PaymentRequisite


class ApiV2ResponseModel(BaseModel):
    payment: Payment
    paymentMethods: List[PaymentMethod]
    success: bool
    captchaRequired: bool
    yandexMetrikaEnabled: bool
