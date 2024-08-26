import unittest
from unittest.mock import patch, Mock
import requests
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.currency_exchanger import CurrencyExchanger


class TestCurrencyExchanger(unittest.TestCase):
    @patch('requests.get')
    def test_currency_exchange_thb_to_krw(self, mock_get):
        # สร้าง Mock Response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'base': 'THB', 'result': {'KRW': 38.69}}
        mock_get.return_value = mock_response

        # สร้าง instance ของ CurrencyExchanger
        exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")

        # ทดสอบการแปลงค่าเงิน
        result = exchanger.currency_exchange(1000)

        # ตรวจสอบผลลัพธ์
        self.assertEqual(result, 38690.00)

        # ตรวจสอบว่า mock_get ถูกเรียกด้วยพารามิเตอร์ที่ถูกต้อง
        mock_get.assert_called_once_with(
            "https://coc-kku-bank.com/foreign-exchange",
            params={'from': 'THB', 'to': 'KRW'}
        )

    @patch('requests.get')
    def test_currency_exchange_thb_to_usd(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'base': 'THB', 'result': {'USD': 0.029}}
        mock_get.return_value = mock_response

        exchanger = CurrencyExchanger(base_currency="THB", target_currency="USD")
        result = exchanger.currency_exchange(500)

        self.assertEqual(result, 14.50)

    @patch('requests.get')
    def test_currency_exchange_api_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException

        exchanger = CurrencyExchanger(base_currency="THB", target_currency="USD")
        result = exchanger.currency_exchange(1000)

        self.assertIsNone(result)

    def test_invalid_currency(self):
        exchanger = CurrencyExchanger(base_currency="THB", target_currency="INVALID")
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {'base': 'THB', 'result': {}}
            mock_get.return_value = mock_response

            result = exchanger.currency_exchange(1000)
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()