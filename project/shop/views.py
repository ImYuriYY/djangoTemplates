from django.shortcuts import render


products = [
    {
        'id': 1,
        'title': 'Costume',
        'size': 'M',
        'price': 1000,
    },
    {
        'id': 2,
        'title': 'Short',
        'size': 'M',
        'price': 300,
    },
    {
        'id': 3,
        'title': 'Cap',
        'size': 'M',
        'price': 100,
    },
    {
        'id': 4,
        'title': 'T-shirt',
        'size': 'M',
        'price': 200,
    },
    {
        'id': 5,
        'title': 'Cross',
        'size': 'M',
        'price': 500,
    },
]


def productsView(request):
    return render(request, 'shop/products.html', context={'products': products})


def product(request, id):
    product = products[id-1]
    return render(request, 'shop/product.html', context={"product": product})


def index(request):
    header = "Данные пользователя"
    langs = ['C', 'C++', 'Python', 'Java', 'JavaScript', 'Pascal']
    user = {'name': 'Alevard', 'surname': 'Levski'}
    address = ('Mira', 12, 147)

    text = "<h4>TEXTTEXTTEXTTEXT</h4>"

    data = {'header': header, 'langs': langs, 'user': user, 'address': address, 'text': text}
    return render(request, 'shop/index.html', context=data)

def about(request):
    return render(request, 'shop/about.html')

def contacts(request):
    return render(request, 'shop/contacts.html')
