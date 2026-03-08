def apply_promo_code(order_id: int, promo_code: str, promo_repo=None) -> bool:
    """
    применяет промокод к заказу, если он действителен.
    """
    if promo_repo is None:
        promo_repo = get_promo_code_from_db
    
    promo_data = promo_repo(promo_code)
    
    if not promo_data:
        return False
    
    # проверка на валидность
    is_valid, error_reason = validate_promo(promo_data)
    return is_valid


def get_promo_code_from_db(promo_code: str) -> dict | None:
    """реальный запрос к БД для получения данных о промокоде"""
    pass


def validate_promo(promo_data) -> tuple[bool, str]:
    """валидация промокода"""
    pass
