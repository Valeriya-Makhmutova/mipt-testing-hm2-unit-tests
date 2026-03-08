def check_availability(event_id: int, seats_requested: int, db_getter=None) -> bool:
    
    if not isinstance(seats_requested, int):
        raise TypeError("seats_requested должно быть числом (int)")

    if not isinstance(event_id, int):
        raise TypeError("event_id должно быть числом (int)")

    if seats_requested <= 0:
        raise ValueError("seats_requested не может быть отрицательным или равным нулю")
    
    if event_id < 0:
        raise ValueError("event_id не может быть отрицательным")

    if db_getter is None:
        db_getter = get_available_seats_from_db
    
    available_seats = db_getter(event_id)
    return available_seats >= seats_requested

# реальная функция для работы с БД
def get_available_seats_from_db(event_id: int) -> int:
    # здесь будет реальная логика проверки
    pass