from app.bs_storm.schemas.orm import OrmBaseModel
from typing import Optional
from pydantic import root_validator
from app.bs_storm.utils.exceptions.exception import PortsNotValidError, DomainNotValidError, BluePortsNotValidError, \
    GreenPortsNotValidError, APINameNotValidError, APIIndexNotValidError
import validators


class ApiBaseModel(OrmBaseModel):
    API_NAME: Optional[str]
    API_BLUE_PORT: Optional[int]
    API_GREEN_PORT: Optional[int]
    API_NGINX_DOMAIN: Optional[str]
    API_INDEX: Optional[str]

    @root_validator(pre=False)
    @classmethod
    def ports_validation(cls, values: dict) -> dict:
        if not values["API_BLUE_PORT"] == None and not values["API_GREEN_PORT"] == None:
            if values["API_BLUE_PORT"] == values["API_GREEN_PORT"]:
                raise PortsNotValidError()
        return values

    # TODO 도메인 인증 고치기
    @root_validator(pre=False)
    @classmethod
    def domain_validation(cls, values: dict) -> dict:
        if not values["API_NGINX_DOMAIN"] == None:
            if validators.url(values["API_NGINX_DOMAIN"]):
                raise DomainNotValidError()

        return values

    @root_validator(pre=False)
    @classmethod
    def blue_port_validation(cls, values: dict) -> dict:
        if not values["API_BLUE_PORT"] == None:
            if not (0 <= values["API_BLUE_PORT"] and values["API_BLUE_PORT"] <= 65535):
                raise BluePortsNotValidError()
        return values

    @root_validator(pre=False)
    @classmethod
    def green_port_validation(cls, values: dict) -> dict:
        if not values["API_GREEN_PORT"] == None:
            if not (0 <= values["API_GREEN_PORT"] and values["API_GREEN_PORT"] <= 65535):
                raise GreenPortsNotValidError()
        return values

    @root_validator(pre=False)
    @classmethod
    def api_name_validation(cls, values: dict) -> dict:
        if not values["API_NAME"] == None:
            if 49 <= len(values["API_NAME"]):
                raise APINameNotValidError()
        return values

    @root_validator(pre=False)
    @classmethod
    def index_validation(cls, values: dict) -> dict:
        if not values["API_INDEX"] == None:
            if 500 <= len(values["API_INDEX"]):
                raise APIIndexNotValidError()
        return values


class getOutApiRequest(ApiBaseModel):
    API_NAME: Optional[str]
    API_BLUE_PORT: Optional[int]
    API_GREEN_PORT: Optional[int]
    API_NGINX_DOMAIN: Optional[str]
    API_INDEX: Optional[str]


class getApiRequest(ApiBaseModel):
    API_NAME: str
    API_INDEX: Optional[str]
    API_NGINX_DOMAIN: str
    API_BLUE_PORT: int
    API_GREEN_PORT: int


class createApiRequest(ApiBaseModel):
    API_NAME: str
    API_INDEX: Optional[str]
    API_NGINX_DOMAIN: str
    API_BLUE_PORT: int
    API_GREEN_PORT: int


class updateApiRequest(ApiBaseModel):
    API_NAME: Optional[str]
    API_INDEX: Optional[str]
    API_NGINX_DOMAIN: str
    API_BLUE_PORT: int
    API_GREEN_PORT: int
