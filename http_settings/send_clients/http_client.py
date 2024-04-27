import allure
import requests
from requests import Response
from typing import Optional

from config.base_settings import base_api_settings
from utils.logger import *


class HttpClient:
    def __init__(self, headers: Optional[dict] = None,
                 path: str = '',
                 host: str = base_api_settings.api.base_host
                 ):
        self.host = host
        self.path = path
        self.headers = headers

    def execute_request(self, method, payload=None):
        url = f'{self.host}{self.path}'
        with allure.step(f'Отправка запроса {url}'):
            response = getattr(requests, method)(url=url, headers=self.headers, json=payload)
        log.write(Level.INFO, method.upper(), url, response.status_code)
        return response

    def post(self, payload) -> Response:
        return self.execute_request('post', payload)

    def get(self) -> Response:
        return self.execute_request('get')
