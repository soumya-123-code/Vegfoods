from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import get_user_model #usersignup

from .models import  Category, Product

def index(request):
    return render(request,'cart/index.html')

def about(request):
    return render(request,'cart/about.html')

def contact(request):
    return render(request,'cart/contact.html')

def blog(request):
    return render(request,'cart/blog.html')



def category(request):
    all_category=Category.objects.all()
    context={'all_category':all_category}
    return render(request,'cart/category.html',context)


def display_product(request,category_id):
    all_category=Category.objects.all()
    if(category_id == 0):
         products = Product.objects.all()
         category_name='all'
    else:
         category=Category.objects.get(pk=category_id)
         products = Product.objects.filter(category=category)
         category_name = category.category_name
        
    context={'products':products,'all_category':all_category,'category_name':category_name}
    return render(request,'cart/shop.html',context)

    

     
@csrf_exempt
def ajaxsignup(request):
     user = request.POST.get('user')
     print(user)
     email = request.POST.get('email')
     print(email)
     pwd = request.POST.get('pwd')
     print(pwd)

     rpwd = request.POST.get('rpwd')
     print(rpwd)

     user = get_user_model()(
            name=user,
            email=email,
        )
     user.set_password(pwd)
     user.save()


     return HttpResponse("Form submitted")


    