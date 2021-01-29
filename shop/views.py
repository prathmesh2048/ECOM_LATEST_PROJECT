from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required


def index(request):
    
    products = Product.objects.all()

    template = 'shop/index.html'
    context = {'products':products}
    return render(request,template,context)

@login_required(login_url='/accounts/login/')
def detail(request, slug_name):
    
    product = Product.objects.get(slug=slug_name)

    template = 'shop/detail.html'
    context = {'product':product}
    return render(request,template,context) 

def cart(request):
    template = 'shop/cart.html'
    context = {'product':product}
    return render(request,template,context) 

def cartHandler(request):
    if request.is_ajax() and request.method == 'POST':
        print(request.POST.get('data'))
        data = {
            'response':'response'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
