from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('add-blog/', views.add_blog, name="add_blog"),
    path('blog_detail/<slug>', views.blog_detail, name="blog_detail"),
    path('see_blog/', views.see_blog, name="see_blog"),
    path('blog_delete/<id>', views.blog_delete, name="blog_delete")
]           