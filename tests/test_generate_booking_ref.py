import pytest
from unittest.mock import Mock
from src.generate_booking_ref import generate_booking_ref

# позитивные тесты

def test_generate_booking_ref_format():
    """Проверка формата референса"""
   
    mock_generator = Mock(return_value="ABC123")
    
    result = generate_booking_ref(123, 456, mock_generator)
    
    # Проверяем формат
    assert result == "BOOK-123-456-ABC123"
    assert result.startswith("BOOK-")
    


def test_generate_booking_ref_uniqueness():
    """Проверка уникальности при повторных вызовах"""
    # Создаем мок, который возвращает разные значения при каждом вызове
    mock_generator = Mock()
    mock_generator.side_effect = ["ABC123", "XYZ789", "DEF456"]
    
    result1 = generate_booking_ref(123, 456, mock_generator)
    result2 = generate_booking_ref(123, 456, mock_generator)
    result3 = generate_booking_ref(123, 456, mock_generator)
    
    assert result1 != result2
    assert result1 != result3
    assert result2 != result3
    


# негативные тесты

def test_generate_booking_ref_invalid_user_id_type():
    """Проверка с некорректным типом user_id"""
    mock_generator = Mock()
    
    with pytest.raises(TypeError):
        generate_booking_ref("123", 456, mock_generator)  # (user_id - строка)


def test_generate_booking_ref_negative_ids():
    """Проверка с отрицательными ID"""
    mock_generator = Mock(return_value="ABC123")
    
    # функция вызывает ошибку при отрицательных ID
    with pytest.raises(ValueError):
        result = generate_booking_ref(-1, 456, mock_generator)
        