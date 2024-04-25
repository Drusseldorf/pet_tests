from pathlib import Path
from pydantic import BaseModel
from pydantic_settings_yaml import YamlBaseSettings

import warnings

warnings.filterwarnings("ignore")


PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_DIR = PROJECT_ROOT.joinpath('config')

config_file = CONFIG_DIR.joinpath('base_project_config.yaml')
env_file = CONFIG_DIR.joinpath('local.env')


class Operators(BaseModel):
    operator_token: str


class Company(BaseModel):
    company_token: str
    company_id: str


class DefoultData(BaseModel):
    defoult_method: str
    defoult_currency: str
    defoult_amount: int


class Paths(BaseModel):
    sms_reader_path: str
    push_reader_path: str
    pay_in_h2h_path: str
    api_v2_payment: str


class ApiSettings(BaseModel):
    base_host: str
    operators: Operators
    company: Company
    paths: Paths
    defoult_data: DefoultData


class BaseAPISettings(YamlBaseSettings):
    api: ApiSettings

    class Config:
        yaml_file = config_file
        env_file = env_file
        env_prefix = "ENV__"
        env_nested_delimiter = "__"


base_api_settings = BaseAPISettings()
