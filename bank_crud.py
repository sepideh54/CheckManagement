"""CRUD operations for the bank lookup table."""
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


def create_bank(bank_name):
    name = (bank_name or "").strip()
    if not name:
        raise ValueError("Bank name is required.")
    if len(name) > 120:
        raise ValueError("Bank name cannot exceed 120 characters.")
    return _execute(
        "INSERT INTO bank_table (bank_name) VALUES (%s)", (name,), fetch="id"
    )


def get_all_banks():
    return _execute(
        "SELECT bank_id, bank_name FROM bank_table ORDER BY bank_name",
        fetch="all", dictionary=True,
    ) or []


def get_bank(bank_id):
    if not bank_id:
        return None
    return _execute(
        "SELECT bank_id, bank_name FROM bank_table WHERE bank_id=%s",
        (bank_id,), fetch="one", dictionary=True,
    )


def update_bank(bank_id, bank_name):
    name = (bank_name or "").strip()
    if not bank_id or not name:
        raise ValueError("Bank ID and name are required.")
    if len(name) > 120:
        raise ValueError("Bank name cannot exceed 120 characters.")
    return bool(_execute(
        "UPDATE bank_table SET bank_name=%s WHERE bank_id=%s",
        (name, bank_id),
    ))


def delete_bank(bank_id):
    if not bank_id:
        return False
    return bool(_execute(
        "DELETE FROM bank_table WHERE bank_id=%s", (bank_id,)
    ))
