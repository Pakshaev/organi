from django.shortcuts import render
from .models import Product, Department, Colors
from django.views.generic import DetailView


from django.shortcuts import render
from .models import Product, Department, Colors

def catalog(request):
    # Получаем параметры из GET-запроса
    query = request.GET.get('q')
    department_name = request.GET.get('department')
    color = request.GET.get('color')
    size = request.GET.get('size')
    sort_price = request.GET.get('sort_price')

    # Формируем начальный QuerySet
    products = Product.objects.all()

    # Фильтрация по отделу
    if department_name:
        try:
            department = Department.objects.get(name=department_name)
            products = products.filter(department=department)
        except Department.DoesNotExist:
            # Если отдел не существует, выполнить редирект на shop-grid.html
            return render(request, 'products/shop-grid.html', {'products': products})

    # Фильтрация по поиску
    if query:
        # Фильтрация продуктов по названию, регистронезависимо
        products = products.filter(name__icontains=query)

    # Фильтрация по цвету (с приведением к нижнему регистру)
    if color:
        try:
            color_instance = Colors.objects.get(name__iexact=color)
            products = products.filter(color=color_instance)
        except Colors.DoesNotExist:
            # Если цвет не существует, игнорируем фильтрацию по цвету
            pass

    # Фильтрация по размеру
    if size:
        products = products.filter(size__iexact=size)

    # Сортировка по цене
    if sort_price == 'low':
        products = products.order_by('price')
    elif sort_price == 'high':
        products = products.order_by('-price')

    # Получаем все цвета из базы данных
    colors = Colors.objects.all()

    # Отправляем отфильтрованный и отсортированный список, а также цвета в контекст шаблона
    context = {'products': products, 'colors': colors}
    return render(request, 'products/shop-grid.html', context)



def contact(request):

    return render(request, 'products/contact.html')


def sort_by_price(request):
    sort_price = request.GET.get('sort_price', '')
    if sort_price == 'low':
        products = Product.objects.all().order_by('price')
    elif sort_price == 'high':
        products = Product.objects.all().order_by('-price')
    else:
        products = Product.objects.all()

    return render(request, 'products/shop-grid.html', {'products': products})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/shop-details.html'
    context_object_name = 'products'
