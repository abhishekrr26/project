from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Banner, Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    banners = Banner.objects.filter(enabled=True)
    products = Product.objects.filter(enabled=True)[:4]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'banners': banners, 'products': products, 'categories': categories
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'store/profile.html')
