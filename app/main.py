from fastapi import FastAPI,Response,status,HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import  randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    published : bool = True

while True:
    try:
        conn = psycopg2.connect(host='localhost',database ='fastapi',user='postgres',password='2004', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was successful")
        break
    except Exception as error:
        print("connection to database failed")
        print("Error", error)
        time.sleep(2)
    



my_posts = [{"title": "title of post 1", "content": "content of post 1","id": 1},{"title":"favo foods","content":"i like pizza","id":2}]



def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

    return None



@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!!!"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):

    posts =db.query(models.Post).all()
    
    print(posts)
    return{"data": "successfully"}



@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = 1""")
    # posts= cursor.fetchall()
     posts =db.query(models.Post).all()
     return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    # (post.title, post.content, post.published))
    # new_post = cursor.fetchone()

    # conn.commit()
   
    new_post =models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}



    
@app.get("/posts/{id}")
def get_post(id : int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """,(str(id)))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id:{id} was not found ")
       
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT )
def delete_post(id:str, db: Session = Depends(get_db)):

    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """,(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    post.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id : int, post: Post, db: Session = Depends(get_db)):
    #  cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,(post.title, post.content, post.published, str(id)))
    #  updated_post = cursor.fetchone()
    #  conn.commit()
    post_query= db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    db.commit()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    post_query.update(post.model_dump(),synchronize_session=False)
    
    db.commit()
    return {'data': post_query.first()}

