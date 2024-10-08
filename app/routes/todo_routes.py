from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.todo_service import getAllTodos, addTodo

router = APIRouter()

templates = Jinja2Templates(directory="app/view_templates")

@router.get("/", response_class=HTMLResponse)
async def todos(request: Request):
    return templates.TemplateResponse("todo.html", {"request": request, "todoList": getAllTodos() })

@router.post("/add")
def add_item(request: Request, item: str = Form(...)):
    new_todo : str = addTodo(item)
    return templates.TemplateResponse("partials/todo/todo.html", {"request": request, "todo": new_todo})

