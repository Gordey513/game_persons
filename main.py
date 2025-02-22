import file_operations
from faker import Faker
import random


if __name__ == '__main__':
    special_letters = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' '
    }

    Information = {
        "first_name": "",
        "last_name": "",
        "job": "",
        "town": "",
        "strength": "",
        "agility": "",
        "endurance": "",
        "intelligence": "",
        "luck": "",
        "skill_1": "",
        "skill_2": "",
        "skill_3": ""
    }

    skills = [
        "Стремительный прыжок",
        "Электрический выстрел",
        "Ледяной удар",
        "Стремительный удар",
        "Кислотный взгляд",
        "Тайный побег",
        "Ледяной выстрел",
        "Огненный заряд"
    ]

    fake = Faker("ru_RU")

    my_skills = random.sample(skills, 8)
    new_skills = []
    for skill in my_skills:
        a = skill
        for i in a:
            a = a.replace(i, special_letters[i])
        new_skills.append(a)

    for i in range(10):
        Information["first_name"] = fake.first_name()
        Information["last_name"] = fake.last_name()
        Information["job"] = fake.job()
        Information["town"] = fake.city()
        Information["strength"] = random.randint(3, 18)
        Information["agility"] = random.randint(3, 18)
        Information["endurance"] = random.randint(3, 18)
        Information["intelligence"] = random.randint(3, 18)
        Information["luck"] = random.randint(3, 18)
        Information["skill_1"] = random.choice(new_skills)
        Information["skill_2"] = random.choice(new_skills)
        Information["skill_3"] = random.choice(new_skills)
        result = "result/result{}.svg".format(i)
        file_operations.render_template("карточка.svg", result, Information )
