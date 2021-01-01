menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
]

for meal in menu:
    if meal.count('spam') == 0:
        print(meal)
        continue

    sortedMeal = sorted(meal)
    firstSpam = sortedMeal.index('spam')

    lastSpam = sortedMeal.rindex('spam')

    del sortedMeal[firstSpam:lastSpam]

    print(sortedMeal)
