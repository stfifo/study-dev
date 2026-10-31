from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#서버 실행
@app.get("/")
def root_handler():
    return {"message": "hello fastAPI"}

@app.get("/login")
def login_handler():
    return{"message": "login page"}

@app.get("/users/{users_id}")
def read_user_handler(user_id: int):
    return {"user_id": user_id, "message": f"사용자 {user_id} 조회"}

@app.get("/items")
def read_items_handler(max_price: int | None = None):
    return {"max_price": max_price}

class Item(BaseModel):
    name: str
    price: int
    in_stock: bool = True

@app.post("/items")
def create_item_handler(item: Item):
    return {
        "message": f"{item.name}이 추가됨",
        "price": item.price,
        "item": item
        }

@app.put("/items/{item_id}")
def update_item_handler(item_id: int, assignee: str, item: Item):
    return {
        "item_id": item_id,
        "assignee": assignee,
        "message": f"{item.name} 가격: {item.price}"
    }