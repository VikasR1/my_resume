from fastapi import APIRouter
from webapps.general_page import route_page



api_router = APIRouter()
api_router.include_router(route_page.router, prefix="", tags=["home-webapp"])