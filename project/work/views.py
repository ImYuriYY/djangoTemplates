from django.shortcuts import render





def index(request):
    data = {'education': 'Alabuga', 'group': 'Python-2', 'specialization':'Programming', 'wantBecome':'Game programmist'}
    return render(request, 'work/index.html', context=data)


def about(request):
    data = {'surname':"Yurin", 'name': 'Yuri', 'lastname': 'Yurievich', 'height': 170, 'age': 18}
    return render(request, 'work/about.html', context=data)


def contacts(request):
    contacts = {'Номер телефона':'89520190024', 'Телеграмм тег': '@Bad1l1'}
    return render(request, 'work/contacts.html', context={'contacts': contacts})
