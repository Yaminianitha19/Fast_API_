from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import  randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating : Optional[int] =    None

my_posts = [{"title": "title of post 1", "content": "content of post 1","id": 1},{"title":"favo foods","content":"i like pizza","id":2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

    return None



@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}
@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}


@app.get("/posts/{id}")
def get_post(id : int):
    
    
    post = find_post(id)
    print(post)
    return{"post_detail":post}



