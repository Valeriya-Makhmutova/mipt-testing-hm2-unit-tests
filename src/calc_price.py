def calc_price(base_price: float, discount: float, count: int) -> float:
    return ((base_price * count) * (100 - discount)) / 100

# предполагается, что скидка в процентах: 25.0 % например 
