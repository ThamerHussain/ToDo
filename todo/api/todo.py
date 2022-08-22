from turtle import title
from ninja import Router
from ninja.security import HttpBearer
from restauth.authotization import AuthBearer
from todo.schemas import details, tododel, todoin
from todo.models import Todo
from typing import List
from config import status

todo_router = Router(tags=['todo'])

# class AuthBearer(HttpBearer):
#     def authenticate(self, request, token):
#         if token == "supersecret":
#             return token #since it a true value in python

@todo_router.get('/get_all', response = {
    200: List[todoin]
}, tags=['todo'], auth = AuthBearer())#, auth = AuthBearer())
def get_all(request):
    return 200, Todo.objects.all()

@todo_router.get('/get', response = {
    200: todoin,
    404: details
})
def get(request, todo_title):
    try:
        todo = Todo.objects.get(title = todo_title)
        return 200, todo
    except:
        return 404, {'detail': f"todo with title {todo_title} is not exist"}

@todo_router.post('/add_todo',response = {200: details, 400: details}, tags = ['todo'])
def add_todo(request, todo_in: todoin):
    try: Todo.objects.get(title = todo_in.title)
    except: 
        Todo.objects.create(
            title = todo_in.title,
            description = todo_in.description)
        return 200, {'detail': f"todo with the title '{todo_in.title}' have been created"}
    else:
        return 400, {'detail': 'ToDo with this title is exist'}

@todo_router.put('/update_todo',response = {200: details, 400: details}, tags = ['todo'])
def update_todo(request, todo_up: todoin):
    try: Todo.objects.get(title = todo_up.title)
    except: return 400, {'detail': f"ToDo with the title '{todo_up.title}' is not exist"}
    else:
        record = Todo.objects.get(title = todo_up.title)
        record.delete()
        Todo.objects.create(
            title = todo_up.title,
            description = todo_up.description)
        return 200, {'detail': f"todo with title '{todo_up.title}' have been updated"}

@todo_router.delete('/delete_todo',response = {200: details, 400: details}, tags = ['todo'])
def delete_todo(request, title):
    try: Todo.objects.get(title = title)
    except: return 400, {'detail': f"ToDo with the title '{title}' is not exist"}
    else:
        record = Todo.objects.get(title = title)
        record.delete()
        return 200, {'detail': f"todo with title '{title}' have been deleted"}