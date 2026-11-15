"""CRUD operations for cheques (checks)."""
from decimal import Decimal, InvalidOperation
from database import get_connection


def _execute(query, values=(), *, fetch=None, dictionary=False):
    connection = get_connection()
    if connection is None:
        return None
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True) if dictionary else connection.cursor()
        cursor.execute(query, values)
        if fetch == "one":
            return cursor.fetchone()
        if fetch == "all":
            return cursor.fetchall()
        connection.commit()
        return cursor.lastrowid if fetch == "id" else cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def _validate_amount(amount):
    """Validate an amount against the check_table DECIMAL(18, 2) contract."""
    if amount is None or (isinstance(amount, str) and not amount.strip()):
        raise ValueError("Check amount is required.")
    try:
        numeric_amount = Decimal(str(amount).strip())
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("Check amount must be numeric.")

    if not numeric_amount.is_finite() or numeric_amount <= 0:
        raise ValueError("Check amount must be a finite value greater than zero.")
    if numeric_amount > Decimal("9999999999999999.99"):
        raise ValueError("Check amount exceeds the maximum supported value.")
    if numeric_amount != numeric_amount.quantize(Decimal("0.01")):
        raise ValueError("Check amount cannot contain more than two decimal places.")
    return numeric_amount


def create_check(check_code, sayadi_number, customer_id, amount, due_date,
                 bank_id=None, front_image=None, back_image=None,
                 description=None):
    if not all((check_code and check_code.strip(),
                sayadi_number and sayadi_number.strip(),
                customer_id, due_date)):
        raise ValueError("Check code, Sayadi number, customer and due date are required.")
    numeric_amount = _validate_amount(amount)
    return _execute(
        """INSERT INTO check_table
           (check_code, sayadi_number, customer_id, amount, due_date, bank_id,
            front_image, back_image, description, created_at)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, CURDATE())""",
        (check_code.strip(), sayadi_number.strip(), customer_id,
         numeric_amount, due_date, bank_id, front_image, back_image, description),
        fetch="id",
    )


def get_all_checks():
    return _execute(
        """SELECT c.*, cu.customer_name, b.bank_name
           FROM check_table c
           LEFT JOIN customer_table cu ON cu.customer_id=c.customer_id
           LEFT JOIN bank_table b ON b.bank_id=c.bank_id
           WHERE c.is_deleted=0 ORDER BY c.due_date, c.check_id""",
        fetch="all", dictionary=True,
    ) or []


def get_check(check_id):
    if not check_id:
        return None
    return _execute(
        """SELECT c.*, cu.customer_name, b.bank_name
           FROM check_table c
           LEFT JOIN customer_table cu ON cu.customer_id=c.customer_id
           LEFT JOIN bank_table b ON b.bank_id=c.bank_id
           WHERE c.check_id=%s AND c.is_deleted=0""",
        (check_id,), fetch="one", dictionary=True,
    )


def get_check_by_sayadi(sayadi_number):
    if not sayadi_number or not sayadi_number.strip():
        return None
    return _execute(
        """SELECT c.*, cu.customer_name, b.bank_name
           FROM check_table c
           LEFT JOIN customer_table cu ON cu.customer_id=c.customer_id
           LEFT JOIN bank_table b ON b.bank_id=c.bank_id
           WHERE c.sayadi_number=%s AND c.is_deleted=0
           ORDER BY c.check_id DESC LIMIT 1""",
        (sayadi_number.strip(),), fetch="one", dictionary=True,
    )


def update_check(check_id, check_code, sayadi_number, customer_id, amount,
                 due_date, bank_id=None, front_image=None, back_image=None,
                 description=None):
    if not all((check_id, check_code and check_code.strip(),
                sayadi_number and sayadi_number.strip(),
                customer_id, due_date)):
        raise ValueError("Required check fields are missing.")
    numeric_amount = _validate_amount(amount)
    return bool(_execute(
        """UPDATE check_table
           SET check_code=%s, sayadi_number=%s, customer_id=%s, amount=%s,
               due_date=%s, bank_id=%s, front_image=%s, back_image=%s,
               description=%s
           WHERE check_id=%s AND is_deleted=0""",
        (check_code.strip(), sayadi_number.strip(), customer_id, numeric_amount,
         due_date, bank_id, front_image, back_image, description, check_id),
    ))


def delete_check(check_id):
    if not check_id:
        return False
    return bool(_execute(
        "UPDATE check_table SET is_deleted=1 WHERE check_id=%s AND is_deleted=0",
        (check_id,),
    ))


def generate_checkinfo_code():
    result = _execute(
        """SELECT COALESCE(MAX(CAST(SUBSTRING(check_code, 3) AS UNSIGNED)), 0)
           FROM check_table WHERE check_code REGEXP '^CH[0-9]+$'""",
        fetch="one",
    )
    if result is None:
        return None
    return f"CH{int(result[0]) + 1:03d}"


if __name__ == "__main__":
    print(get_all_checks())
