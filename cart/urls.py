from django.urls import path

from . import views

app_name ='cart'


urlpatterns = [
    path('', views.index,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('blog',views.blog,name="blog"),
    path('signup',views.ajaxsignup,name="signup"),
  
    path('category',views.category,name="category"),
    path('products/<int:category_id>',views.display_product,name="display_product")
    
   
   
    

]
