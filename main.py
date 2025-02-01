from file_operations import VERSION

import file_operations

from faker import Faker

import random

fake = Faker("ru_RU")

import random

import os


if not os.path.exists("results"): 
    os.makedirs("results") 


Special_letters = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}
skills=["Стремительный прыжок","Электрический выстрел","Ледяной удар", "Стремительный удар",
        "Кислотный взгляд","Тайный побег","Ледяной выстрел","Огненный заряд"]
for number in range(1, 11):
   
    only_its_skills = random.sample(skills,3)
    replace_skills = []                                                                                                                                                   
    for skill in only_its_skills:
        for symbol in skill:
            skill = skill.replace(symbol, Special_letters[symbol])
        replace_skills.append(skill)
    Information={
    "first_name":fake.first_name(),
    "last_name":fake.last_name()  ,
    "job":fake.job(),
    "town":fake.city(),
    "strength":random.randint(3,18),
    "agility":random.randint(3,18),
    "endurance":random.randint(3,18),
    "intelligence":random.randint(3,18),
    "luck":random.randint(3,18),
    "skill_1":replace_skills[0],
    "skill_2":replace_skills[1],
    "skill_3":replace_skills[2],
}
    
    file_operations.render_template("карточка.svg", f"result/result_{number}.svg", Information)