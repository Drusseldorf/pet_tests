from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings_yaml import YamlBaseSettings
from pydantic_settings_yaml.base_settings import YamlConfigSettingsSource

PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_DIR = PROJECT_ROOT.joinpath("config")

config_path = CONFIG_DIR.joinpath("base_project_settings.yaml")


class Operators(BaseModel):
    user_name: str
    operator_token: str


class ApiSettings(BaseModel):
    base_host: str
    operators: Operators


class ProjectSettings(YamlBaseSettings):
    api: ApiSettings

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: BaseSettings,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            dotenv_settings,
            env_settings,
            YamlConfigSettingsSource(settings_cls),
            file_secret_settings,
            init_settings
        )

    class Config:
        default_yaml_file_path = config_path
        yaml_file = default_yaml_file_path
        secrets_dir = PROJECT_ROOT.joinpath('config', 'secrets')
        env_file = PROJECT_ROOT.joinpath('config', 'local.env')
        env_prefix = "ENV__"
        env_nested_delimiter = "__"


project_settings = ProjectSettings()
