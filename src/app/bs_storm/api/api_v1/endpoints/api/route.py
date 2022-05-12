from fastapi import APIRouter, Depends
from app.bs_storm.core.database import get_db
from sqlalchemy.orm import Session
from app.bs_storm.schemas.api import updateApiRequest, createApiRequest, getOutApiRequest
from app.bs_storm.crud.api import findByAPIName, findAllAPI, createByAPI, updateByAPI, deleteByAPIName

api_route = APIRouter(prefix="/api")


@api_route.get("/{api_name}", response_model=getOutApiRequest)
async def get_api(api_name: str, db=Depends(get_db)):
    """
    get single api's information from api table

    :param api_name: api's name
    :param db: db Session
    :return: getOutApiRequest - single api's information

    getOutApiRequest:
        API_NAME: Optional[str]
        BLUE_PORT: Optional[str]
        GREEN_PORT: Optional[str]
        NGINX_DOMAIN: Optional[str]
        API_INDEX: Optional[str]
    """
    res = findByAPIName(db, api_name)

    return res


@api_route.get("/", response_model=list[getOutApiRequest])
async def get_api_all(db: Session = Depends(get_db)):
    """
    get Multi api's information from api table

    :param db: db Session
    :return: list[getOutApiRequest] - Multi api's information

    getOutApiRequest:
        API_NAME: Optional[str]
        BLUE_PORT: Optional[str]
        GREEN_PORT: Optional[str]
        NGINX_DOMAIN: Optional[str]
        API_INDEX: Optional[str]
    """
    res = findAllAPI(db)
    return res


@api_route.post("/", response_model=createApiRequest)
async def create_api(req: createApiRequest, db : Session = Depends(get_db)):
    """
    create new api information to api table

    :param req: createApiRequest
    :param db: db Session
    :return: createApiRequest - user's new api information

    createApiRequest:
        API_NAME: str
        API_INDEX: Optional[str]
        NGINX_DOMAIN: str
        BLUE_PORT: int
        GREEN_PORT: int

    """
    res = createByAPI(db, req)
    return req


@api_route.put("/{api_name}", response_model=updateApiRequest)
async def update_api(api_name: str, req: updateApiRequest, db: Session =Depends(get_db)):
    """
    update single api's information from api table

    :param api_name: target api's name
    :param req: updateApiRequest
    :param db: db Session
    :return: updateApiRequest

    updateApiRequest:
        API_NAME: Optional[str]
        API_INDEX: Optional[str]
        NGINX_DOMAIN: str
        BLUE_PORT: int
        GREEN_PORT: int
    """
    res = updateByAPI(db, api_name, req)
    return req


@api_route.delete("/{api_name}")
async def del_api(api_name: str, db: Session =Depends(get_db)):
    """
    delete single api information from api table

    :param api_name:
    :param db: db Session
    :return None
    """
    res = deleteByAPIName(db, api_name)
