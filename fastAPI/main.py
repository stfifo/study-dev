from fastapi import FastAPI

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