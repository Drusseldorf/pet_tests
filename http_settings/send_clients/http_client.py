import requests
from requests import Response
from typing import Optional

from config.base_settings import base_api_settings
from utils.logger import logger


class HttpClient:
    def __init__(self, headers: Optional[dict] = None,
                 path: str = '',
                 host: str = base_api_settings.api.base_host
                 ):
        self.host = host
        self.path = path
        self.headers = headers

    def execute_request(self, method, **kwargs):
        response = getattr(requests, method)(url=f'{self.host}{self.path}', headers=self.headers, json=kwargs)
        logger.write_log('INFO', f'{method.upper()} {self.host+self.path} {response}')
        return response

    def post(self, **kwargs) -> Response:
        return self.execute_request('post', **kwargs)

    def get(self, **kwargs) -> Response:
        return self.execute_request('get', **kwargs)
