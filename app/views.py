from django.db.models import Count
from django.shortcuts import render,redirect   
from django.views import View
from app.models import Product,Customer
from app.forms import CustomerRegistrationForm, AuthenticationForm, UsernameField,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
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
        # return redirect('home')
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
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulation Customer Profile Save Successfully !')
        else:
            messages.warning(request,'Invalid Input Data !')
        return render(request,'app/profile.html', locals())

            

def Address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'app/address.html', locals())
    

class UpdateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'app/updateAddress.html', locals())
    
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            
            add.save()
            messages.success(request,'Congratulation Customer Profile Save Successfully !')
        else:
            messages.warning(request,'Invalid Input Data !')
        return redirect('address')
    
    
def logout_view(request):
    logout(request)
    messages.success(request,'Logout Successfully !')
    return redirect('login')
   
   
def add_to_cart(request):
    return render(request,'app/addToCart.html', locals())


def show_cart(request):
    return render(request,'app/showcart.html', locals())