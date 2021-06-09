import unittest
from datetime import timedelta
from payment_calc import PaymentCalc

payment_calc = PaymentCalc("../work_info.txt")


class TestPaymentCalc(unittest.TestCase):

    def test_to_pay_per_hour(self):
        day = "SU"
        worked_hours = timedelta(hours=3)
        hours_range = (0, 9)
        self.assertEqual(
            payment_calc.to_pay_per_hour(day, worked_hours, hours_range), 90)


if __name__ == '__main__':
    unittest.main()
