import pytest
from unittest.mock import Mock, patch
from src.apply_promo_code import apply_promo_code

# позитивные тесты:
# промокод действителен
def test_apply_valid_promo_code():
    # мок для репозитория
    mock_repo = Mock()
    # инф-ия про промокод
    mock_repo.return_value = {
        'is_active': True,
        'expires_at': '2027-12-31',
        'usage_limit': 10,
        'current_usage': 3
    }
    
    # мок для функции валидации
    with patch('src.apply_promo_code.validate_promo', return_value=(True, "")):
        result = apply_promo_code(123, "SALE20", mock_repo)
        
        assert result == True
        mock_repo.assert_called_once_with("SALE20")


def test_apply_promo_code_overl_limit_expired():
    # промокод истек, лимит исчерпан
    mock_repo = Mock()
    mock_repo.return_value = {
        'is_active': False,
        'expires_at': '2023-12-31',
        'usage_limit': 5,
        'current_usage': 6
    }
    
    with patch('src.apply_promo_code.validate_promo', return_value=(False, "")):
        result = apply_promo_code(123, "HALFPRICE", mock_repo)
        
        assert result == False



# негативные тесты:
# order_id передан как строка, а не int
def test_apply_promo_code_invalid_order_id_type():
    mock_repo = Mock()

    with pytest.raises(TypeError):
        apply_promo_code("123", "SALE20", mock_repo) 

# отрицательный order_id
def test_apply_promo_code_negative_order_id():
    mock_repo = Mock()

    mock_repo.return_value = {
        'is_active': True,
        'expires_at': '2027-12-31',
        'usage_limit': 10,
        'current_usage': 5
    }
    
    with pytest.raises(ValueError):
        apply_promo_code(-5, "SALE20", mock_repo)


