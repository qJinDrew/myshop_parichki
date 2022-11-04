from django.shortcuts import render


# при переходе на гл.страницу будет вызвана данная функция
def index(request):
    data = {
        'title': 'Главная страница',

    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


