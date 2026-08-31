from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory  # . -> اشاره به اپ یا ماژولی که داخلش هستیم
from django.http import Http404
from django.db.models import Avg, Min, Max  # ماژول برای بدست آوردن میانگین، ماکزیمم، مینیموم و...


def product_list(request):
    # ------------------------------------------------------------------------------------------------------
    # افزودن یک دسته بندی و سپس یک محصول به آن (در هر بار اجرای برنامه ساخته میشوند)
    # console = ProductCategory(title='پلی استیشن', url_title="playstation")
    # console.save()
    # ps_4 = Product(title='play station 4', price=16000000, category=console, short_description='ps_4', rating=4)
    # ps_4.save()
    # ------------------------------------------------------------------------------------------------------

    products = Product.objects.all().order_by('-price')
    number_of_products = products.count()  # بدست آوردن تعداد کل محصولات
    avg_rating = products.aggregate(Avg("rating"))  # بدست آوردن میانگین
    return render(request, 'product_module/product_list.html', {
        'products': products,
        'total_number_of_products': number_of_products,
        'average_ratings': avg_rating
    })


def product_detail(request, slug):
    # --------------------------------------------------------------------------------
    # روش اول مدیریت عدم وجود آیتم در جدول با برگرداندن صفحه 404:
    # try:
    #     product = Product.objects.get(id=product_id) # بجای id میتونیم از pk استفاده کنیم -> get(pk=id)
    # except:
    #     raise Http404

    # روش بهتر و تمیز تر مدیریت عدم وجود آیتم در جدول با دستور get_object_or_404:
    # --------------------------------------------------------------------------------

    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product_module/product_detail.html', {
        'product': product
    })

# -------------------------------------------------------------------------------------------------------
# get_object_or_404(طرز فیلتر شدن آیتم ها براساس فیلدی مثل آیدی (کوئری), کلاس مدل):

# این دستور یا آبجکت رو بدست میاورد یا درصورت وجود نداشتن آن، صفحه 404 را برمیگرداند و کد تمیز تری هست

# -------------------------------------------------------------------------------------------------------
# count: بدست آوردن مجموع یک لیست

# aggregate: میتونیم مجموعه ای از اعمال رو براش مشخص کنیم که انجام دهد، مثلا میانگین، مینیموم و ماکزیمم
# پس میتونیم آیتم های مختلف رو در یک کوئری بصورت گروهی اعمال کنیم
# in views.py -> avg_rating = products.aggregate(Avg("rating"), Min("price"), Max("price"))
# in html file -> average rating of product ratings: {{ average_ratings }}
# in result -> average rating of product ratings: {'rating__avg': 2.6666666666666665, 'price__min': 20000, 'price__max': 6500000}
# در خروجی یک دیکشنری برمیگرداند، چون در فانکشن میتونیم آرگومان های مختلفی ارسال کنیم

# اگر خواسته باشم فقط مقدار عددی را نمایش دهد باید به این صورت در فایل ویو بنویسیم:
# average rating of product ratings: {{ average_ratings.rating__avg }}
# in result -> average rating of product ratings: 2.6666666666666665

# -------------------------------------------------------------------------------------------------------
# order_by: مرتب سازی رو نباید درون کد های پایتون انجام بدیم، یعنی نباید اول دیتاها رو لود کنیم سپس مرتب کنیم
# بلکه مرتب سازی باید در بخش دیتابیس انجام شود، یعنی بعد همان بخشی که فانکشن all رو فراخوانی کرده ایم

# order_by('price'): مرتب سازی لیست براساس قیمت محصولات بصورت صعودی
# order_by('-price'): مرتب سازی لیست براساس قیمت محصولات بصورت نزولی

# -------------------------------------------------------------------------------------------------------
