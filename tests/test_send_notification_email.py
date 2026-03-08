import pytest
from unittest.mock import Mock, patch
from src.send_notification_email import send_notification_email

# позитивные тесты
# письмо успешно отправлено
def test_send_notification_email_success():
    # создаем мок для mail_sender, который возвращает True
    mock_mail_sender = Mock(return_value=True)
    
    # данные бронирования
    booking_details = {
        'booking_ref': 'BOOK-123-456-ABC123',
        'event_name': 'Концерт',
        'seats': 2,
        'total_price': 2000.0
    }
    
    # вызываем функцию с моком
    result = send_notification_email('test@example.com', booking_details, mock_mail_sender)
    
    # проверяем результат
    assert result == True
    

# сервер недоступен, функция возвращает False
def test_send_notification_email_server_unavailable():
    mock_mail_sender = Mock(side_effect=ConnectionError("SMTP server unavailable"))
    booking_details = {'booking_ref': 'BOOK-123-456-ABC123'}
    
    result = send_notification_email('test@example.com', booking_details, mock_mail_sender)
    
    assert result == False


# негативные тесты
# невалидный формат email 
def test_send_notification_email_invalid_email_format():
    mock_mail_sender = Mock()
    booking_details = {'booking_ref': 'BOOK-123-456-ABC123'}
    
    with pytest.raises(ValueError):
        send_notification_email('email', booking_details, mock_mail_sender)

# в деталях бронирования нет booking_ref
def test_send_notification_email_missing_booking_ref():

    mock_mail_sender = Mock()
    booking_details = {'event': 'Концерт'}  # нет обязательного поля
    
    with pytest.raises(KeyError):
        send_notification_email('test@example.com', booking_details, mock_mail_sender)