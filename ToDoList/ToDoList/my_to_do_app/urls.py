# my_to_do_app.urls  > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),  #찍혔어요
    # root url conf에 의해서 http://127.0.0.1:8000의 요청이 전달되면
    # views.py 파일의 index 함수 코드를 실행
    # http://127.0.0.1:8000 url의 별명은 'index'
    path('createToDo/')
    ]
