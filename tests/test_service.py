from temp_soap_service.service import (
    fahrenheit_to_celsius,
    celsius_to_fahrenheit,
)


def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(98.6), 2) == 37.00


def test_celsius_to_fahrenheit():
    assert round(celsius_to_fahrenheit(37), 2) == 98.60
