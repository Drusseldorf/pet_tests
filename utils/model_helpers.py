from pydantic import ValidationError
from requests import Response
from utils.logger import *


def change_value(model, field, new_value):
    setattr(model, field, new_value)
    if hasattr(model, 'sign') and callable(getattr(model, 'sign')):
        model.sign()


def get_validated_model(response: Response, model):
    try:
        return model.model_validate(response.json())
    except ValidationError as e:
        log.write(Level.ERROR, f'Model Validation Error:\n{e}')


def set_amount_and_requisite(model_dict: dict, amount, requisite: str):
    text = model_dict.get('text')
    model_dict['text'] = text.format(str(amount), requisite[-4:])
    model_dict['requisite'] = requisite
