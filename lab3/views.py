from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Головна сторінка',
        'content': 'Вітаю! Це головна сторінка лабораторної роботи №3.',
        'is_home': True, # Цей прапорець скаже шаблону показати посилання на інші сторінки
    }
    return render(request, 'lab3/dynamic_page.html', context)

def page1_view(request):
    context = {
        'title': 'Перша сторінка',
        'content': 'Тут знаходиться контент першої додаткової сторінки. Наприклад, інформація про фізичні явища чи програмування.',
        'is_home': False, # Прапорець False - показуємо кнопку "Назад"
    }
    return render(request, 'lab3/dynamic_page.html', context)

def page2_view(request):
    context = {
        'title': 'Друга сторінка',
        'content': 'А це друга сторінка. Весь цей текст передається через контекст!',
        'is_home': False,
    }
    return render(request, 'lab3/dynamic_page.html', context)