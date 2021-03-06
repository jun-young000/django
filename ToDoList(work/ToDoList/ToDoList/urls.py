"""ToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('my_to_do_app.urls')), #my_to_do_app.urls.py 파일을 생성해야 함
    #http://127.0.0.1:8000으로 시작하는 모든 요청은 my_to_do_app.urls 로 전달
    path('admin/', admin.site.urls), # 장고가 제공하는 관리자 사이트의 URL-완성이므로 필요하면 사용하면 됨
    #http://127.0.0.1/admin/ : 현재 파일에서 매칭
]
