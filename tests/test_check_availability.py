import pytest
from unittest.mock import Mock
from src.check_availability import check_availability

# позитивные тесты:
# при наличии билетов
def test_check_availability_is_available():
    mock_generator = Mock(return_value=5)

    result = check_availability(1, 2, mock_generator)
    assert result == True


def test_check_availability_is_not_available():
    mock_generator = Mock(return_value=0)

    result = check_availability(5, 2, mock_generator)
    assert result == False


# негативные тесты:
# некорректное seats_requested
def test_check_availability_seats_requested_seats_requested_is_negative():
    mock_generator = Mock(return_value=5)

    with pytest.raises(ValueError):
        check_availability(5, -2, mock_generator)

# некорреткное event_id
def test_check_availability_seats_requested_id_is_not_int():
    mock_generator = Mock(return_value=5)

    with pytest.raises(TypeError):
        check_availability('5', 2, mock_generator)
