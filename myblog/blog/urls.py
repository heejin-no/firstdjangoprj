from django.urls import path
from django.urls.conf import include
from blog import views

#app_name을 쓸경우 html에서 url을 쓸때 무조건 app_name을 써야함
# ex)app_name="blog"면 html에서 url blog:~~ 라고 적어야함
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name="post_detail"), 
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
