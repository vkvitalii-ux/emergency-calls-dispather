from src.my_project.database import init_db, add_call


def classify_call(symptoms: str) -> tuple[str, str]:
    """
    Функция принимает список симптомов и возвращает приоритет и профиль бригады.
    """
    symptoms_lower = symptoms.lower()

    if symptoms_lower == "103":
        return "Экстренный", "Скорая помощь"

    if "не дышит" in symptoms_lower or "остановка дыхания" in symptoms_lower:
        return "Критический (0 минут).", "Реанимационная бригада"

    elif "боль в груди" in symptoms_lower or "давит" in symptoms_lower:
        return "Экстренный (до 20 минут)", "Кардиологическая бригада"

    elif "острое нарушение речи" in symptoms_lower or "отнялась рука" in symptoms_lower:
        return "Экстренный (до 20 минут)", "Неврологическая бригада"

    elif "дтп" in symptoms_lower or "падение с высоты" in symptoms_lower:
        return "Экстренный (до 20 минут)", "Врачебная/Линейная бригада"

    elif "температура" in symptoms_lower or "высокое давление" in symptoms_lower:
        return "Неотложный (в порядке очереди)", "Фельдшерская бригада"

    else:
        return "ТРЕБУЕТСЯ УТОЧНЕНИЕ ДИСПЕТЧЕРА", "Линейная бригада"


if __name__ == "__main__":
    print("--- СИСТЕМА АВТОМАТИЗАЦИИ СКОРОЙ ПОМОЩИ ---")
    print("(Для завершения работы программы введите: выход)\n")
    init_db()

    while True:
        user_input = input("Введите жалобы пациента: ")

        if user_input.lower().strip() == "выход":
            print("Работа программы завершена. До свидания")
            break

        if not user_input.strip():
            continue

        priority, team_type = classify_call(user_input)

        # СОХРАНЕНИЕ В БАЗУ ДАННЫХ
        add_call(user_input, priority, team_type)

        print("\n[РЕЗУЛЬТАТ АВТОМАТИЗАЦИИ]:")
        print(f"Приоритет вызова: {priority}")
        print(f"Направлена бригада {team_type}")
        print("-" * 40)

# Тестовый комментарий для диплома
