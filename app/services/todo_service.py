from app.data_access.todos import dataGetTodoList, dataAddTodo

def getAllTodos():
    return dataGetTodoList()

def addTodo(item : str):
    new_todo = dataAddTodo(item)

    return new_todo


