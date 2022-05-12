from fastapi import APIRouter
from app.bs_storm.api.api_v1.endpoints.api.route import api_route

api_v1_route = APIRouter(prefix="/api/v1")
api_v1_route.include_router(api_route)