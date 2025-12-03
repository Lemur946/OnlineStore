from django.shortcuts import render


def home(request):
    """
    Контроллер для главной страницы.
    Рендерит шаблон home.html.
    """
    return render(request, 'catalog/home.html')


def contacts(request):
    """
    Контроллер для страницы контактов.
    При POST-запросе выводит данные в консоль.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефон: {phone}, Сообщение: {message}')
        # Здесь можно добавить логику отправки email или сохранения в БД

    return render(request, 'catalog/contacts.html')