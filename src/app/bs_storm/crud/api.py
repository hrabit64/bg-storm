from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.bs_storm.core.model import model
from app.bs_storm.schemas.api import updateApiRequest,createApiRequest
from app.bs_storm.utils.log import logger
from app.bs_storm.utils.exceptions.exception import NotFoundItemError

def findByAPIName(db:Session,api_name:str) -> dict:
    try:
        api = db.query(model.Api).filter(model.Api.API_NAME == api_name).first()
        assert api is not None
    except AssertionError:
        raise NotFoundItemError()

    except Exception as e:
        logger.debug(f"findBYAPIName // {str(api)}")
        return None
    return api

def findAllAPI(db:Session) -> list:
    try:
        api = db.query(model.Api).filter().all()
        assert api is not None
    except AssertionError:
        raise NotFoundItemError()
    except:
        return None

    return api

def createByAPI(db:Session,req:createApiRequest):
    try:
        newApi = model.Api(**req.dict())
        db.add(newApi)
        db.commit()
        db.refresh(newApi)

    except:
        logger.exception("createByAPI")
        return False

    return newApi

def updateByAPI(db:Session,api_name:str,req:updateApiRequest):
    try:
        api = db.query(model.Api).filter(model.Api.API_NAME == api_name).first()
        if api:
            update_api_encoded = jsonable_encoder(req)

            for var, value in update_api_encoded.items():
                setattr(api, var, value)

            db.merge(model.Api)
            db.commit()
            db.refresh(api)
        else:
            raise NotFoundItemError()
    except:
        return False

    return True

def deleteByAPIName(db:Session,api_name:str):
    try:
        api = db.query(model.Api).filter(model.Api.API_NAME == api_name).first()
        assert api
        db.delete(api)
        db.commit()
    except AssertionError:
        raise NotFoundItemError()
    except:
        return False

    return True

# async def setTable(api_name: str,table_info:dict, redis) -> bool:
#     try:
#         async with redis.client() as conn:
#             await conn.hset(api_name,table_info)
#
#     except Exception as e:
#
#         logger.error(f"{e} // createTable // raise error")
#
#         return False
#
#     logger.debug(
#             f"// setTable// {api_name} is successfully set! by {api_name} sec.")
#     return True
#
#
# async def delTable(api_name: str, redis) -> bool:
#     try:
#         async with redis.client() as conn:
#             await conn.delete(api_name)
#
#     except Exception as e:
#         logger.error(f"{e} // delTable // raise error")
#
#         return False
#
#     logger.debug(
#             f"// delTable // {api_name} is successfully del!")
#     return True
#
# async def scanTable(redis) -> bool:
#     try:
#         async with redis.client() as conn:
#             cur = b"0"  # set initial cursor to 0
#             while cur:
#                 cur, keys = await conn.scan(cur, match="key:blue-green-checker*")
#                 print("Iteration results:", keys)
#
#     except Exception as e:
#         logger.error(f"{e} // delTable // raise error")
#
#         return False
#     return True

