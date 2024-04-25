from requests import Response


def change_value(model, field, new_value):
    setattr(model, field, new_value)
    if hasattr(model, 'sign') and callable(getattr(model, 'sign')):
        model.sign()


def get_validated_model(response: Response, model):
    return model.model_validate(response.json())
