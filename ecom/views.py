from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Cat, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# from .forms import UserForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def loginuser(request):
    categories = Cat.objects.all()
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 

        else:
            messages.error(request, 'username or password does not exist')  
    context = {'categories':categories}
    return render(request, 'login.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    items = Item.objects.filter(Q(categorie__cat_name__icontains=q) |
            Q(name__icontains = q))
    categories = Cat.objects.all()
    context = {'items': items, 'categories':categories,}
    return render(request, 'home.html',context)

def logoutuser(request):
    logout(request)
    return redirect('home')


def createuser(request):
    categories = Cat.objects.all()
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user = authenticate(username = username, password=password)
            user = form.save(commit = False)
            user.username = user.username.lower() 
            user.save()
            login(request, user)
            return redirect('home')
    context = {'form':form, 'categories':categories}
    return render(request, 'create-user.html', context)


def go_to_item(request, pk):
    items = Item.objects.all()
    item = None
    for i in items:
        if i.name == str(pk):
            item = i
    categories = Cat.objects.all()
    context = {'categories':categories,'item':item}
    return render(request, 'go_to_item.html', context) 

@login_required(login_url = 'login')
def add_to_cart(request, item_name):
    item = Item.objects.get(name = item_name)
    cart_item, created = CartItem.objects.get_or_create(item = item)
    cart_item.quantity +=1
    cart_item.save()
    return redirect(home)  

@login_required(login_url = 'login')
def view_cart(request):
    items = CartItem.objects.all()
    total_price = sum(item.item.price * item.quantity for item in items)
    # if total_price==0:
    #     return HttpResponse('Your cart is empty') 
    categories = Cat.objects.all()
    context = {'items':items, 'total_price':total_price, 'categories':categories}
    return render(request, 'view-cart.html',context)


def user_page(request, pk):
    items = Item.objects.all()
    user_items = []
    for i in items:
        if i.user.username == str(pk):
            item = i
            user_items.append(i)
    context ={'user_items':user_items} 
        
    return render(request, 'user_page.html', context)

@login_required(login_url = 'login')
def minus_item(request, item_id):
    if CartItem.objects.count() == 0:
        return HttpResponse('Your cart is already empty')
    else:
        items = CartItem.objects.all()
        for item in items:
            if item.quantity <=0:
                item.delete()
                return HttpResponse('This item is not in your cart')
            else:
                item = CartItem.objects.get(id = item_id)
                item.quantity -=1
                item.save()
    return redirect(home)

@login_required(login_url = 'login')
def empty_cart(request):
    items = CartItem.objects.all()
    for item in items:
        item.delete()
    context ={} 
    return redirect('view_cart')


# def remove_from_cart(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id)
#     cart_item.delete()
#     return redirect(home)


def about(request):
    categories = Cat.objects.all()
    context = {'categories':categories,}
    return render(request, 'about.html',context)


def help(request):
    categories = Cat.objects.all()
    context = {'categories':categories,}
    return render(request, 'help.html',context)


def more(request):
    categories = Cat.objects.all()
    context = {'categories':categories,}
    return render(request, 'more.html',context)


def contacts(request):
    categories = Cat.objects.all()
    context = {'categories':categories,}
    return render(request, 'contacts.html',context)

