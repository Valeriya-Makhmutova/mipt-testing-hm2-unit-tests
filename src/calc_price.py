def calc_price(base_price: float, discount: float, count: int) -> float:
    """
    считает стоимость билетов с учетом скидки
    """
    if count <= 0:
        raise ValueError("Количество билетов должно быть больше 0")
    
    if discount < 0 or discount > 100:
        raise ValueError("Скидка должна быть от 0 до 100")
    
    result = ((base_price * count) * (100 - discount)) / 100
    return result

# предполагается, что скидка в процентах: 25.0 % например 
