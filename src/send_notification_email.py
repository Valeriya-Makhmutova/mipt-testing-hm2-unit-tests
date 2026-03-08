def send_notification_email(email: str, booking_details: dict, mail_sender=None) -> bool:
    """
    отправляет уведомление на почту при успешном бронировании/оплате
    """
    if mail_sender is None:
        mail_sender = send_email_via_smtp
    
    try:
        # формируем содержимое письма
        subject = f"Подтверждение бронирования #{booking_details.get('booking_ref', '')}"
        body = format_email_body(booking_details)
        
        # отправляем письмо
        result = mail_sender(email, subject, body)
        return result
        
    except Exception:
        return False


def send_email_via_smtp(to_email: str, subject: str, body: str) -> bool:
    """
    реальная отправка письма через SMTP
    """
    # здесь будет код подключения к SMTP серверу
    pass


def format_email_body(booking_details: dict) -> str:
    """
    форматирует тело письма из деталей бронирования
    """
    # здесь будет форматирование текста письма
    pass