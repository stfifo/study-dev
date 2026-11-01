from fastapi import FastAPI, status
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

@app.get("/items_1")
def read_items_handler(max_price: int | None = None):
    return {"max_price": max_price}

class Item(BaseModel):
    name: str
    price: int
    in_stock: bool = True

@app.post("/items_2")
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

@app.post("/items_3", response_model=Item, status_code=status.HTTP_201_CREATED)
# response body에 pydantic model 활용하려면 decorator에서 response_model 옵션 지정
def create_item_handler2(item: Item):
    return item

# 90p self check
class order_response(BaseModel):
    order_id: int
    pick_up: bool | None = None

@app.get("/orders/{order_id}", response_model=order_response)
def order_handler(order_id: int, pickup: bool | None = None):
    return {
        "order_id": order_id,
        "pickup": pickup
    }

@app.post("/orders_2/{order_id}", response_model=order_response)
def order_handler(item: order_response):
    return item