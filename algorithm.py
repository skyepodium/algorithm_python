fruits = [
    {
        'id': 1,
        'name': 'banana',
    },
    {
        'id': 2,
        'name': 'apple',
    },
    {
        'id': 3,
        'name': 'orange',
    }
]

selected_fruits = []

for fruit in fruits:
    if (fruit['name'] == 'banana') == 0:
        selected_fruits.append(fruit)

print(selected_fruits)
# name이 banana인 row 제외하고 조회
# [{'id': 2, 'name': 'apple'}, {'id': 3, 'name': 'orange'}]
