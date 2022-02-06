"""dj_project URL Configuration

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
from django.urls import path
from demo.views import post_list_view
from demo.views import question_list_view,user,uservalidate,dbms_question_list_view,os_question_list_view,os_storeans,Os_userans
from demo.views import final,logout
from demo.views import storeans,dbms_storeans
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list_view),
    path('users/',user),
    path('users/uservalidate', uservalidate),
    path('users/questions', question_list_view),
    path('users/dbms_questions', dbms_question_list_view),
    path('users/os_questions', os_question_list_view),
    path('users/storeans', storeans),
    path('users/dbms_storeans', dbms_storeans),
    path('users/os_storeans', os_storeans),
    path('users/final', final),
    path('users/oops/logout.html', logout),
    path('users/logout', logout),
    #path('upload', Upload)

]
