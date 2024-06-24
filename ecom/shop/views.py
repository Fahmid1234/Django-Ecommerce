from django.shortcuts import render, HttpResponseRedirect, redirect
from .models  import *
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .forms import *
from datetime import datetime
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    products = Products.objects.all()
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'index.html', {'products': products, 'totalitem': totalitem})


def productdetails(request, pk):
    product = Products.objects.get(pk=pk)
    item_already_in_cart = False
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        item_already_in_cart = Cart.objects.filter(Q(product=product.id)&Q(user=request.user)).exists()
    return render(request, 'single_prod.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})

def registration(request):
    if request.method == 'POST':
        frm = usercreate(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm= usercreate()
    return render(request, 'registration.html', {'form': frm})

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login Successfully"))
            return redirect('home')
        else:
            messages.success(request, ("Login Successfully"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You have benn logged out!"))
    return redirect('home')

def add_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Products.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        Carts(user=user, product=product).save()
        return redirect('cart')
    else:
        return redirect('login')

@login_required
def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user) 
        total_amount = 0
        temp_amount = 0
        shipping_cost = 100.0
        amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        my_cart = request.POST
        totalitem = 0
        totalitem = len(Cart.objects.filter(user=request.user))
        request.session['my_cart'] = my_cart
        if cart_product:
            
            for p in cart_product:
                temp_amount = (p.quantity * p.product.price)
                amount += temp_amount
                total_amount = amount + shipping_cost
            return render(request, 'cart.html', {'cart': cart, 'total': total_amount, 'amount': amount, 'totalitem': totalitem})
        else:
            return redirect('empty_cart')
    
def emptycart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'emptycart.html', {'totalitem': totalitem})

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.quantity += 1
        c.save()
        amount = 0.0
        temp_amount = 0
        total_amount = 0.0
        shipping_cost = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.price)
                amount += temp_amount
                total_amount = amount + shipping_cost
                
    
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount,
            'temp_amount': temp_amount
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        temp_amount = 0
        total_amount = 0.0
        shipping_cost = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.price)
                amount += temp_amount
                total_amount = amount + shipping_cost
                
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount,
            'temp_amount': temp_amount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.delete()
        amount = 0.0
        temp_amount = 0
        total_amount = 0.0
        shipping_cost = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.price)
                amount += temp_amount
                total_amount = amount + shipping_cost
                
    
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount,
            'temp_amount': temp_amount

        }
        return JsonResponse(data)
@login_required
def place_order(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user) 
        totalitem = 0
        total_amount = 0
        temp_amount = 0
        shipping_cost = 100.0
        amount = 0.0
        totalitem = len(Cart.objects.filter(user=request.user))
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_product:
            
            for p in cart_product:
                temp_amount = (p.quantity * p.product.price)
                amount += temp_amount
                total_amount = amount + shipping_cost
        try:
            shipping_user = ShippingAddress.objects.get(user=request.user)
            shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        except:
            shipping_form = ShippingForm(request.POST or None)
        
        if request.method == 'POST':
            if shipping_form.is_valid():
                shipping_form.instance.user = request.user
                shipping_form.save()
        return render(request, 'place_order.html', {'form': shipping_form, 'cart': cart, 'total': total_amount, 'amount': amount, 'totalitem': totalitem})
    
@login_required
def billing_info(request):
    if request.POST:
        payment_form = PaymentForm()
        cart = Cart.objects.filter(user=request.user) 
        total_amount = 0
        temp_amount = 0
        shipping_cost = 100.0
        amount = 0.0
        totalitem = 0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_product:
            
            for p in cart_product:
                temp_amount = (p.quantity * p.product.price)
                amount += temp_amount
                total_amount = amount + shipping_cost
       
            
        else:
            return redirect('home')
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'billing_info.html', {'form': request.POST, 'cart': cart, 'total': total_amount, 'amount': amount, 'payment': payment_form, 'totalitem': totalitem})

@login_required
def process_order(request):
    if request.method == 'POST':
        payment_form = PaymentForm()
        cart = Carts.objects.filter(user=request.user)
        amount = 0.0
        temp_amount = 0
        total_amount = 0.0
        shipping_cost = 100.0
        totalitem = 0
        cart_products = Carts.objects.filter(user=request.user)
        if cart_products:
            for p in cart_products:
                
                temp_amount = (p.quantity * p.product.price)
                amount += temp_amount
                total_amount = amount + shipping_cost
        
        my_shipping = request.session.get('my_shipping')
        
        user = request.user
        full_name = my_shipping['full_name']
        email = my_shipping['email']
        amount_paid = total_amount
        shipping_address = f"{my_shipping['address1']}\n{my_shipping['address2']}\n{my_shipping['thana']}\n{my_shipping['zipcode']}\n{my_shipping['district']}\n{my_shipping['division']}\n{my_shipping['country']}"

        

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            order = Order(
                user=user,
                full_name=full_name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=amount_paid
            )
            order.save()

            for p in cart_products:
                product = p.product  # Get the product object from Cart
                product_quantity = p.quantity
                product_price = p.product.price * product_quantity

                # Create and save OrderItem object
                create_order_item = OrderItem(
                    order=order,
                    product=product,
                    user=user,
                    quantity=product_quantity,
                    price=product_price
                )
                create_order_item.save()
            Cart.objects.filter(user=user).delete()
            date = datetime.now()
            inv_num = random.randint(000000, 999999)
            
        else:
            return redirect('home')

    return render(request, 'process_order.html', {'cart': cart, 'total': total_amount, 'amount': amount, 'name': full_name, 'address1': my_shipping['address1'], 'address2':my_shipping['address2'], 'email': my_shipping['email'], 'date': date, 'invoice': inv_num, 'totalitem': totalitem})

def about(req):
    totalitem = 0
    if req.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=req.user))
    return render(req, 'about.html', {'totalitem': totalitem})

def homePage(req):
    totalitem = 0
    if req.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=req.user))
    products = Products.objects.all()
    sw = Products.objects.filter(category='Smartwatch')
    pb = Products.objects.filter(category='Power Bank')
    fan = Products.objects.filter(category='Fan')
    ka = Products.objects.filter(category='Kitchen Accesories')
    return render(req, 'home.html', {'product': products, 'totalitem': totalitem, 'sw': sw, 'pb': pb, 'fan': fan, 'ka': ka})

def fanPage(req):
    fan = Products.objects.filter(category='Fan')
    return render(req, 'fan.html', {'fan': fan})

def powerbankPage(req):
    totalitem = 0
    if req.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=req.user))
    powerbank = Products.objects.filter(category='Power Bank')
    return render(req, 'powerbank.html', {'powerbank': powerbank, 'totalitem': totalitem})

def smartwatchPage(req):
    totalitem = 0
    if req.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=req.user))
    smartwatch = Products.objects.filter(category='Smartwatch')
    return render(req, 'smartwatch.html', {'smartwatch': smartwatch, 'totalitem': totalitem})