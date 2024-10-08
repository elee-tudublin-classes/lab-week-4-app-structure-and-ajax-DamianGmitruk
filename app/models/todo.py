from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    details: str
    completed: bool = False
    userID: int = 0

