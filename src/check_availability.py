def check_availability(event_id: int, seats_requested: int, db_getter=None) -> bool:
    # db_getter: функция для получения данных из БД (для тестирования)

    # Если не передан getter, используем реальный
    if db_getter is None:
        db_getter = get_available_seats_from_db
    
    available_seats = db_getter(event_id)
    return available_seats >= seats_requested

# Реальная функция для работы с БД
def get_available_seats_from_db(event_id: int) -> int:
    """Реальный запрос к БД"""
    print('Нет подключения к базе данных')
    pass