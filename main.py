from fastapi import FastAPI

app = FastAPI()

todo = ['python','fastapi']

@app.get("/")
def get_todo_list():
    return {"message":"hello, world", "data":todo}

@app.post("/create")
def create_todo():
    todo.append("pydantic")
    return {"message" : "created todo", "data":todo}

@app.delete("/delete")
def delete_todo():
    todo.pop(2)
    return {"message":"delete todo","data":todo}
