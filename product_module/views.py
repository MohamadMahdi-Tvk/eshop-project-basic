from django.shortcuts import render, get_object_or_404
from .models import Product  # . -> اشاره به اپ یا ماژولی که داخلش هستیم
from django.http import Http404


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_module/product_list.html', {
        'products': products
    })


def product_detail(request, product_id):
    # روش اول مدیریت عدم وجود آیتم در جدول با برگرداندن صفحه 404:
    # try:
    #     product = Product.objects.get(id=product_id) # بجای id میتونیم از pk استفاده کنیم -> get(pk=id)
    # except:
    #     raise Http404

    # روش بهتر و تمیز تر مدیریت عدم وجود آیتم در جدول با دستور get_object_or_404:
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_module/product_detail.html', {
        'product': product
    })

# -------------------------------------------------------------------------------------------------------
# get_object_or_404(طرز فیلتر شدن آیتم ها براساس فیلدی مثل آیدی (کوئری), کلاس مدل):

# این دستور یا آبجکت رو بدست میاورد یا درصورت وجود نداشتن آن، صفحه 404 را برمیگرداند و کد تمیز تری هست

# -------------------------------------------------------------------------------------------------------