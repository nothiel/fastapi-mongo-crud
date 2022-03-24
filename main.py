from fastapi import FastAPI
from database import Database
from models import UserInSchema, UserModifySchema, UserOutSchema, UsersOutSchema
from bson import ObjectId
from starlette.responses import JSONResponse

app = FastAPI()

db = Database()

@app.get("/")
def hello_world():
    return {"Hello": "World from MONGOCRUD"}


@app.post("/users")
def create_user(user: UserInSchema):
    _id = db.create(user.dict())
    return {"Message": "User Created", "id": str(_id)}

@app.get("/user/{id}", response_model=UserOutSchema)
def find_user(id: str):
    _id = ObjectId(id)

    user = db.read(_id)

    return UserOutSchema(**user)

@app.get("/users", response_model=UsersOutSchema)
def find_users():
    users = db.read_all()
    return UsersOutSchema(users=users)


@app.put("/user/{id}")
def modify_user(id: str, update_data: UserModifySchema):
    _id = ObjectId(id)

    modified_count = db.update(_id, update_data.dict(exclude_unset=True)).modified_count
    
    if not modified_count:
        return JSONResponse({"Message": "Error while reading db"}, 404)
    return JSONResponse({"Message": "User Modified"}, 200)


@app.delete("/user/{id}")
def delete_user(id: str):
    _id = ObjectId(id)

    is_deleted = db.delete(_id)

    if not is_deleted:
        return JSONResponse({"Message": "Error while reading db"}, 404)
    return JSONResponse({"Message": "User Deleted"}, 200)
