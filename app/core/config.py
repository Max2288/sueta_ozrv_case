from pydantic_settings import BaseSettings


class GlobalConfig(BaseSettings):
    DESCRIPTION: str = "Monitoring system"
    DEBUG: bool = False
    SERVICE_NAME: str = "Monitoring system"
    API_V1_STR: str = "/api/v1"
    PORT: int = 5000
    BASE_URL: str = f'http://127.0.0.1:{PORT}{API_V1_STR}'



config = GlobalConfig()
