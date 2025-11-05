from django.test import TestCase
from loans.helpers import is_prime


class isPrimeTestCase(TestCase):
    def test_3_is_prime(self):
        actual_result = is_prime(3)
        self.assertTrue(actual_result)

    def test_4_is_prime(self):
        actual_result = is_prime(4)
        self.assertFalse(actual_result)
