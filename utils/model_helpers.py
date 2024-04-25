from pydantic import ValidationError
from requests import Response
from utils.logger import logger


def change_value(model, field, new_value):
    setattr(model, field, new_value)
    if hasattr(model, 'sign') and callable(getattr(model, 'sign')):
        model.sign()


def get_validated_model(response: Response, model):
    try:
        return model.model_validate(response.json())
    except ValidationError as e:
        logger.write_log('ERROR', f'ValidationError: {e}')
