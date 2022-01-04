from typing import Optional
from fastapi import APIRouter, Response, status, HTTPException
from fastapi.param_functions import Body
from ..schemas import Post
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


while True:
    try:
        conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password="Compassion123",cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Successful connected to database")
        break
    except Exception as error:
        print("Database connection failed") 
        print("Error: " , error)
        time.sleep(2)



@router.get("/")
def get_posts():
    cursor.execute("""SELECT * from posts""")
    posts = cursor.fetchall()
    return {"data": posts}



@router.post("/", status_code= status.HTTP_201_CREATED)
def create_post(post: Post, response: Response): 
    
    cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s, %s, %s) RETURNING * """, 
    (post.title, post.content, post.published))

    new_post = cursor.fetchone()
    conn.commit()

    return {"message": new_post}



@router.get("/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
        detail= f"Post with id {id} not found")
 
    return {"data": post}



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s returning * """, (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post of id {id} not found")

    return {"message": "Post was successfully deleted"}



@router.put("/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s returning * """, 
    (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()

    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post of id {id} not found")


    return {"data": updated_post}


