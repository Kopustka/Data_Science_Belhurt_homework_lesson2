def stud_info(student):
    if isinstance(student, dict):
        print("Информация о студенте:")
        print(f"Имя: {student.get('имя', 'Не указано')}")
        print(f"Возраст: {student.get('возраст', 'Не указано')}")
        print(f"Курс: {student.get('курс', 'Не указано')}")
    else:
        print("Ошибка: передан неверный тип данных. Ожидался словарь.")


student_info = {
    "имя": "Иван Иванов",
    "возраст": 20,
    "курс": "Программирование"
}

stud_info(student_info)