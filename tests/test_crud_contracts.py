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

    def test_customer_code_length_matches_schema(self):
        with self.assertRaises(ValueError):
            customer_crud.create_customer("C" * 21, "Test")

    def test_customer_name_length_matches_schema(self):
        with self.assertRaises(ValueError):
            customer_crud.create_customer("C001", "N" * 151)

    def test_customer_optional_field_length_is_checked(self):
        with self.assertRaises(ValueError):
            customer_crud.create_customer(
                "C001", "Test", organization_name="O" * 201
            )

    def test_bank_name_length_matches_schema(self):
        with self.assertRaises(ValueError):
            bank_crud.create_bank("B" * 121)

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


    def test_check_amount_accepts_two_decimal_places(self):
        self.assertEqual(
            check_crud._validate_amount("1250.50"),
            check_crud.Decimal("1250.50"),
        )

    def test_check_amount_rejects_more_than_two_decimal_places(self):
        with self.assertRaises(ValueError):
            check_crud._validate_amount("10.001")

    def test_check_amount_rejects_nan_and_infinity(self):
        for value in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    check_crud._validate_amount(value)

    def test_check_amount_rejects_value_above_decimal_18_2(self):
        with self.assertRaises(ValueError):
            check_crud._validate_amount("10000000000000000.00")

    def test_check_update_uses_same_amount_validation(self):
        with self.assertRaises(ValueError):
            check_crud.update_check(
                1, "CH001", "123", 1, "10.999", "2026-01-01"
            )

    def test_operation_requires_check(self):
        with self.assertRaises(ValueError):
            operation_crud.create_operation(None, "OP001", "ارسال", "2026-01-01")


if __name__ == "__main__":
    unittest.main()
