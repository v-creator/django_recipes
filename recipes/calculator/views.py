from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salatik': {
        'помидор, шт': 1,
        'огурец, шт': 2,
        'зелень, г': 100,
        'масло, г': 15,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipes(request):
    r_path = request.path.replace('/','')
    dish = DATA.get(f'{r_path}').copy()
    servings = int(request.GET.get('servings', 1))

    if servings > 1:
        for key, val in dish.items():
            dish[key] = val * servings
    
    context = {
        'recipe': dish
        }   
    
    return render(request, 'index.html', context)