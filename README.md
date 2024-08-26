# LAB9-SQA
# Currency Exchanger

Currency Exchanger เป็นโปรแกรม Python สำหรับแปลงค่าเงินระหว่างสกุลเงินต่างๆ โดยใช้อัตราแลกเปลี่ยนจริงจาก API ของธนาคาร

## คุณสมบัติ

- แปลงค่าเงินระหว่างสกุลเงินต่างๆ
- ใช้อัตราแลกเปลี่ยนจริงจาก API ของธนาคาร
- รองรับการทดสอบด้วย unittest และ mock

## การติดตั้ง

1. โคลนโปรเจคนี้:
   ```
   git clone https://github.com/yourusername/currency-exchanger.git
   cd currency-exchanger
   ```

2. ติดตั้ง dependencies:
   ```
   pip install requests
   ```

## การใช้งาน

```python
from currency_exchanger import CurrencyExchanger

# สร้าง instance ของ CurrencyExchanger
exchanger = CurrencyExchanger(base_currency="THB", target_currency="USD")

# แปลงค่าเงิน
result = exchanger.currency_exchange(1000)
print(f"1000 THB = {result} USD")
```

## การทดสอบ

รันการทดสอบด้วยคำสั่ง:

```
python -m unittest test_currency_exchanger.py
```

## โครงสร้างโปรเจค

- `currency_exchanger.py`: ไฟล์หลักที่มี class CurrencyExchanger
- `test_currency_exchanger.py`: ไฟล์ทดสอบสำหรับ CurrencyExchanger
- `README.md`: ไฟล์นี้

## การสนับสนุน

หากคุณพบปัญหาหรือมีคำแนะนำ กรุณาเปิด issue ในโปรเจคนี้
