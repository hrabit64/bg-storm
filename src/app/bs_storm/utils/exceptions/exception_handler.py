from app.bs_storm.utils.exceptions.exception import PortsNotValidError, DomainNotValidError, BluePortsNotValidError, \
    GreenPortsNotValidError, APINameNotValidError, APIIndexNotValidError, NotFoundItemError
from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import DataError

def include_exception(app):
    app.add_exception_handler(NotFoundItemError, Not_found_item_error_exception_handler)
    app.add_exception_handler(PortsNotValidError, PortsNotValidError_exception_handler)
    app.add_exception_handler(DomainNotValidError, DomainNotValidError_exception_handler)
    app.add_exception_handler(BluePortsNotValidError, BluePortsNotValidError_exception_handler)
    app.add_exception_handler(GreenPortsNotValidError, GreenPortsNotValidError_error_exception_handler)
    app.add_exception_handler(APINameNotValidError, APINameNotValidError_error_exception_handler)
    app.add_exception_handler(APIIndexNotValidError, APIIndexNotValidError_error_exception_handler)
    app.add_exception_handler(DataError, DataError_error_exception_handler)

async def Not_found_item_error_exception_handler(request: Request, exc: NotFoundItemError):
    return JSONResponse(
        status_code=404,
        content={"message": f"NotFoundItemError - Not Found item"},
    )

async def PortsNotValidError_exception_handler(request: Request, exc: PortsNotValidError):
    return JSONResponse(
        status_code=400,
        content={"message": "PortsNotValidError - Let's check blue and green ports. They are same. You can't use same port"},
    )

async def DomainNotValidError_exception_handler(request: Request, exc: DomainNotValidError):
    return JSONResponse(
        status_code=400,
        content={"message": "DomainNotValidError - Let's check Nginx domain. It's not valid domain."},
    )

async def BluePortsNotValidError_exception_handler(request: Request, exc: BluePortsNotValidError):
    return JSONResponse(
        status_code=400,
        content={"message": "BluePortsNotValidError - Let's check blue port. port can be 0~65535"},
    )

async def GreenPortsNotValidError_error_exception_handler(request: Request, exc: GreenPortsNotValidError):
    return JSONResponse(
        status_code=400,
        content={"message": "GreenPortsNotValidError - Let's check green port. port can be 0~65535"},
    )

async def APINameNotValidError_error_exception_handler(request: Request, exc: APINameNotValidError):
    return JSONResponse(
        status_code=400,
        content={"message": "APINameNotValidError - Let's check Api name. name's max lenght is 50"},
    )

async def APIIndexNotValidError_error_exception_handler(request: Request, exc: APIIndexNotValidError):
    return JSONResponse(
        status_code=400,
        content={"message": "APIIndexNotValidError - Let's check Api index. index's max len is 500"},
    )

async def DataError_error_exception_handler(request: Request, exc: DataError):
    return JSONResponse(
        status_code=400,
        content={"message": "DataError - cannot add your request, check your database"},
    )