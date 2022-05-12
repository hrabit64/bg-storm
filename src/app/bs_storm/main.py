from fastapi import FastAPI
import uvicorn
from app.bs_storm.api.api_v1.route import api_v1_route
from app.bs_storm.utils.exceptions.exception_handler import include_exception
app = FastAPI()

app.include_router(api_v1_route)
include_exception(app)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=18000,log_level="debug")

