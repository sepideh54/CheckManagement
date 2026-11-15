import unittest
from unittest.mock import patch

import customer_crud
import bank_crud
import check_crud
import operation_crud


class ValidationTests(unittest.TestCase):
    def test_customer_requires_code_and_name(self):
        with self.assertRaises(ValueError):
            customer_crud.create_customer("", "Test")

    def test_customer_search_requires_criteria(self):
        with self.assertRaises(ValueError):
            customer_crud.get_customer_by_name()

    def test_bank_requires_name(self):
        with self.assertRaises(ValueError):
            bank_crud.create_bank(" ")

    def test_check_requires_fields(self):
        with self.assertRaises(ValueError):
            check_crud.create_check("CH001", "", 1, 100, "2026-01-01")

    def test_check_rejects_non_numeric_amount(self):
        with self.assertRaises(ValueError):
            check_crud.create_check("CH001", "123", 1, "abc", "2026-01-01")

    def test_check_rejects_zero_amount(self):
        with self.assertRaises(ValueError):
            check_crud.create_check("CH001", "123", 1, 0, "2026-01-01")

    def test_operation_requires_check(self):
        with self.assertRaises(ValueError):
            operation_crud.create_operation(None, "OP001", "ارسال", "2026-01-01")


if __name__ == "__main__":
    unittest.main()
