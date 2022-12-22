from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "general_pages/index.html",{"request":request}
        )