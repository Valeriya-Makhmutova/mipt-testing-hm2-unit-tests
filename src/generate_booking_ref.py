def generate_booking_ref(user_id: int, event_id: int, ref_generator=None) -> str:
    # генерирует уникальный код бронирования.
    
    if not isinstance(user_id, int):
        raise TypeError("user_id должно быть числом (int)")

    if not isinstance(event_id, int):
        raise TypeError("event_id должно быть числом (int)")

    if user_id < 0:
        raise ValueError("user_id не может быть отрицательным")
    
    if event_id < 0:
        raise ValueError("event_id не может быть отрицательным")

    if ref_generator is None:
        ref_generator = generate_unique_suffix
    
    suffix = ref_generator()
    return f"BOOK-{user_id}-{event_id}-{suffix}"


def generate_unique_suffix() -> str:
    # генерирует уникальный суффикс
    # здесь будет реальная логика генерации
    pass