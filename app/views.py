from django.db.models import Count
from django.shortcuts import render
from django.views import View
from app.models import Product
from app.forms import CustomerRegistrationForm, AuthenticationForm, UsernameField,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def Home(request):
    context ={}
    return render(request,'app/home.html',context)


def about(request):
    context ={}
    return render(request,'app/about.html',context)


def contact(request):
    context ={}
    return render(request,'app/contact.html',context)


class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,'app/category.html', locals())



class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,'app/category.html', locals())


class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html', locals())




class LoginForm(AuthenticationForm):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html', locals())
    


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html', locals())
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulation User Register Successfully !')
        else:
            messages.warning(request,'Invalid Input Data !')
        return render(request,'app/customerregistration.html', locals())
           
            

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html', locals())
    
    def post(self,request):
        return render(request,'app/profile.html', locals())

            

class AddressView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/address.html', locals())
    
 