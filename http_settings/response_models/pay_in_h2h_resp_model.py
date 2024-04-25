from pydantic import BaseModel


class Card(BaseModel):
    number: str | None = None
    bank_name: str | None = None
    lifetime_in_minutes: int
    holder: str | None = None
    phone: str | None = None
    qr_link: str | None = None
    qr_contract_number: str | None = None
    iban: str | None = None


class PayInH2HResponse(BaseModel):
    id: str
    external_id: str
    amount: int
    status: str
    order_number: str
    card: Card
    to_be_paid: int
    support_url: str
