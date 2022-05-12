from app.bs_storm.crud.api import *
import pytest
from conftest import tmp_api_info
from fastapi.encoders import jsonable_encoder
from app.bs_storm.crud.api import deleteByAPIName
@pytest.mark.asyncio
async def test_api_NotFoundItemError(fastapi_client,tmp_db):
    '''
        test NotFoundItemError error, So Accese to nonexistent item. it will raise NotFoundItemError

        given //  nonexistent in DB, API name

        when // get /api/v1/api/test_item

        then // get status_code 404
                get json "message": "NotFoundItemError - Not Found item"
    '''
    #given
    test_item = "is_nonexistent_item"

    #when
    response = fastapi_client.get(f"/api/v1/api/{test_item}")

    #then
    assert response.status_code == 404
    assert response.json() == {"message": "NotFoundItemError - Not Found item"}



@pytest.mark.asyncio
async def test_api_PortsNotValidError(fastapi_client,tmp_db):
    '''
        test PortsNotValidError, I will give error information, it will raise PortsNotValidError

        given //  api information. that blue port and green port is same

        when // post /api/v1/api/

        then // get status_code 400
                get json "PortsNotValidError - Let's check blue and green ports. They are same. You can't use same port"
    '''
    #given
    test_item = tmp_api_info.copy()
    # port is same
    test_item["API_BLUE_PORT"] = "6565"
    test_item["API_GREEN_PORT"] = "6565"
    logger.debug(f"test info {str(test_item)}")
    #when
    response = fastapi_client.post("/api/v1/api/",json=jsonable_encoder(test_item))

    #then
    assert response.status_code == 400
    assert response.json() == {"message": "PortsNotValidError - Let's check blue and green ports. They are same. You can't use same port"}

# TODO 도메인 인증 오류 고치기 / 도메인 길이 제한
@pytest.mark.asyncio
async def test_api_DomainNotValidError(fastapi_client,tmp_db):
    '''
        test DomainNotValidError, I will give error information, it will raise DomainNotValidError

        given //  api information. that domain format is wrong

        when // post /api/v1/api/

        then // get status_code 400
                get json "DomainNotValidError - Let's check Nginx domain. It's not valid domain."
    '''

    #given
    test_item = tmp_api_info.copy()
    # domain format is wrong
    test_item["API_NGINX_DOMAIN"] = "hosisgodgame"
    logger.debug(f"test info {str(test_item)}")

    #when
    response = fastapi_client.post("/api/v1/api/",json=jsonable_encoder(test_item))

    #then
    assert response.status_code == 400
    assert response.json() == {"message": "DomainNotValidError - Let's check Nginx domain. It's not valid domain."}



@pytest.mark.asyncio
async def test_api_BluePortsNotValidError(fastapi_client,tmp_db):
    '''
        test BluePortsNotValidError, I will give error information, it will raise BluePortsNotValidError

        given //  api information. that blue port's range is wrong

        when // post /api/v1/api/

        then // get status_code 400
                get json "BluePortsNotValidError - Let's check blue port. port can be 0~65535"
    '''
    #given
    test_item = tmp_api_info.copy()
    # blue port's range is wrong
    test_item["API_BLUE_PORT"] = "656565656565"
    logger.debug(f"test info {str(test_item)}")

    #when
    response = fastapi_client.post("/api/v1/api/",json=jsonable_encoder(test_item))

    #then
    assert response.status_code == 400
    assert response.json() == {"message": "BluePortsNotValidError - Let's check blue port. port can be 0~65535"}



@pytest.mark.asyncio
async def test_api_GreenPortsNotValidError(fastapi_client,tmp_db):
    '''
        test GreenPortsNotValidError, I will give error information, it will raise GreenPortsNotValidError

        given //  api information. that Green port's range is wrong

        when // post /api/v1/api/

        then // get status_code 400
                get json "GreenPortsNotValidError - Let's check green port. port can be 0~65535"
    '''
    #given
    test_item = tmp_api_info.copy()
    # green port's range is wrong
    test_item["API_GREEN_PORT"] = "656565656565"
    logger.debug(f"test info {str(test_item)}")

    #when
    response = fastapi_client.post("/api/v1/api/",json=jsonable_encoder(test_item))

    #then
    assert response.status_code == 400
    assert response.json() == {"message": "GreenPortsNotValidError - Let's check green port. port can be 0~65535"}


@pytest.mark.asyncio
async def test_api_APINameNotValidError(fastapi_client,tmp_db):
    '''
        test APINameNotValidError, I will give error information, it will raise APINameNotValidError

        given //  api information. that api name is too long (over 50)

        when // post /api/v1/api/

        then // get status_code 400
                get json "APINameNotValidError - Let's check Api name. name's max lenght is 50"
    '''
    #given
    test_item = tmp_api_info.copy()
    # too long name
    test_item["API_NAME"] = "l"+"o"*50+"ng"
    logger.debug(f"test info {str(test_item)}")
    #when
    response = fastapi_client.post("/api/v1/api/",json=jsonable_encoder(test_item))

    #then
    assert response.status_code == 400
    assert response.json() == {"message": "APINameNotValidError - Let's check Api name. name's max lenght is 50"}

@pytest.mark.asyncio
async def test_api_APIIndexNotValid(fastapi_client,tmp_db):
    '''
        test APIIndexNotValid, I will give error information, it will raise APIIndexNotValid

        given //  api information. that api name is too long (over 65534)

        when // post /api/v1/api/

        then // get status_code 400
                get json "APIIndexNotValidError - Let's check Api index. index's max len is 500"
    '''
    #given
    test_item = tmp_api_info.copy()
    # too long index
    test_item["API_INDEX"] = "w"+"o"*500+"w"
    logger.debug(f"test info {str(test_item)}")

    #when
    response = fastapi_client.post("/api/v1/api/",json=jsonable_encoder(test_item))

    #then
    assert response.status_code == 400
    assert response.json() == {"message": "APIIndexNotValidError - Let's check Api index. index's max len is 500"}