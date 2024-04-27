import hashlib


def calculate_signature(json_body: dict, token: str) -> str:
    sorted_dict_values = ''.join(str(value) for _, value in sorted(json_body.items()))
    signature = hashlib.sha512((sorted_dict_values + token).encode('utf-8')).hexdigest()
    return signature
