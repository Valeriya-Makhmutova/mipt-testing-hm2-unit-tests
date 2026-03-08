from datetime import datetime 

def apply_promo_code(order_id: int, promo_code: str, promo_repo=None) -> bool:
    # применяет промокод к заказу, если он действителен

    if order_id < 0:
        raise ValueError('order_id не может быть отрицательным')

    if promo_repo is None:
        promo_repo = get_promo_code_from_db
    
    promo_data = promo_repo(promo_code)
    
    if not promo_data:
        return False
    
    # проверка на валидность
    is_valid, error_reason = validate_promo(promo_data)
    return is_valid


def get_promo_code_from_db(promo_code: str) -> dict | None:
    # здесь будет реальная логика запроса к БД
    pass


def validate_promo(promo_data) -> tuple[bool, str]:
    # валидация промокода
    
    # проверка активности
    if promo_data.get('is_active', False):
        return (False, "Промокод не активен")
    
    # проверка срока действия
    expires_at = promo_data.get('expires_at')
    if expires_at and isinstance(expires_at, str):
        try:
            expiry_date = datetime.strptime(expires_at, '%Y-%m-%d').date()
            current_date = datetime.now().date()
            
            if current_date > expiry_date:
                return (False, "Срок действия промокода истек")
        except (ValueError, TypeError):
            pass
    
    # проверка лимита использования
    current_usage = promo_data.get('current_usage', 0)
    usage_limit = promo_data.get('usage_limit')
    
    if usage_limit and current_usage >= usage_limit:
        return (False, "Лимит использования исчерпан")
    
    return (True, "")