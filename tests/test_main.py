import pytest
from src.my_project.main import classify_call
from src.my_project.database import init_db, add_call

def test_critical_urgency():
    # 1. Проверяем остановку дыхания
    priority, team = classify_call("у него остановка дыхания")
    assert "Критический" in priority
    assert "Реанимационная" in team


def test_cardio_urgency():
    priority, team = classify_call("сильно давит в груди")
    assert "Экстренный" in priority
    assert "Кардиологическая" in team


def test_stroke_urgency():
    priority, team = classify_call("острое нарушение речи, плохо")
    assert "Экстренный" in priority
    assert "Неврологическая" in team


def test_trauma_urgency():
    priority, team = classify_call("пострадавший в дтп")
    assert "Экстренный" in priority
    assert "Врачебная" in team or "Линейная" in team

def test_line_urgency():
    priority, team = classify_call("высокая температура")
    assert "Неотложный" in priority
    assert "Фельдшерская" in team

# Проверяем работу с Крупным шрифтом (защита от ошибок диспетчера)
def test_caps_lock_protection():
    priority, team = classify_call("БОЛЬ В ГРУДИ")
    assert "Экстренный" in priority
    assert "Кардиологическая" in team


def test_unknown_symptoms():
    # 3. Негативный тест: проверка неопределенной жалобы
    priority, team = classify_call("кашель и насморк")
    assert "ТРЕБУЕТСЯ" in priority
    assert "Линейная" in team

# Фикстура, которая подготавливает базу данных перед тестом
@pytest.fixture()
def setup_database():
    db = init_db()
    yield db


# Сам тест, который теперь правильно использует фикстуру
def test_database_integration(setup_database):
    try:
        add_call(
            symptoms="тестовые симптомы проверки бд",
            priority= "Тест-Приоритет",
            team_type="Тест-Бригада"
        )
        db_status = True
    except RuntimeError:
        db_status = False
    assert db_status is True


# БЛОК НЕГАТИВНЫХ ТЕСТИРОВАНИЯ ОШИБОК

def test_classify_call_wrong_type_error():
    """Негативный тест: передача числа вместо строки должна вызывать ошибку AttributeError."""
    # Мы ожидаем, что метод .lower() у числа вызовет AttributeError
    with pytest.raises(AttributeError):
        classify_call(12345)  # type: ignore


def test_database_error_handling(setup_database):
    """Негативный тест: проверка правильной обработки сбоя в базе данных."""
    try:
        add_call(
            symptoms=None,  # type: ignore
            priority="Тест-Приоритет",
            team_type="Тест-Бригада"
        )
        db_status = True
    except (RuntimeError, TypeError, Exception):
        db_status = False

    assert db_status is False





