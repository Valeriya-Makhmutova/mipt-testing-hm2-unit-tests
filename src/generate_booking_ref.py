def generate_booking_ref(user_id: int, event_id: int, ref_generator=None) -> str:
    """
    генерирует уникальный код бронирования.
    """
    if ref_generator is None:
        ref_generator = generate_unique_suffix
    
    suffix = ref_generator()
    return f"BOOK-{user_id}-{event_id}-{suffix}"


def generate_unique_suffix() -> str:
    """генерирует уникальный суффикс."""
    # здесь будет реальная логика генерации
    pass