"""CRUD operations for check lifecycle events."""
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


def create_operation(check_id, operation_code, operation_type,
                     operation_date, related_person=None, description=None,
                     sayad_system_status=None):
    if not all((check_id, operation_code, operation_type, operation_date)):
        raise ValueError("Check, operation code, type and date are required.")
    return _execute(
        """INSERT INTO operation
           (check_id, operation_code, operation_type, operation_date,
            related_person, description, sayad_system_status)
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (check_id, operation_code, operation_type, operation_date,
         related_person, description, sayad_system_status),
        fetch="id",
    )


def get_all_operations(check_id=None):
    if check_id is None:
        return _execute(
            "SELECT * FROM operation ORDER BY operation_date DESC, operation_id DESC",
            fetch="all", dictionary=True,
        ) or []
    return _execute(
        "SELECT * FROM operation WHERE check_id=%s ORDER BY operation_date DESC, operation_id DESC",
        (check_id,), fetch="all", dictionary=True,
    ) or []


def get_operation(operation_id):
    if not operation_id:
        return None
    return _execute(
        "SELECT * FROM operation WHERE operation_id=%s",
        (operation_id,), fetch="one", dictionary=True,
    )


def update_operation(operation_id, operation_type, operation_date,
                     related_person=None, description=None,
                     sayad_system_status=None):
    if not all((operation_id, operation_type, operation_date)):
        raise ValueError("Operation ID, type and date are required.")
    return bool(_execute(
        """UPDATE operation SET operation_type=%s, operation_date=%s,
               related_person=%s, description=%s, sayad_system_status=%s
           WHERE operation_id=%s""",
        (operation_type, operation_date, related_person, description,
         sayad_system_status, operation_id),
    ))


def delete_operation(operation_id):
    if not operation_id:
        return False
    return bool(_execute(
        "DELETE FROM operation WHERE operation_id=%s", (operation_id,)
    ))


def generate_operation_code(check_id):
    if not check_id:
        raise ValueError("A check must be selected before creating an operation.")
    result = _execute(
        """SELECT COUNT(*) FROM operation WHERE check_id=%s""",
        (check_id,), fetch="one",
    )
    if result is None:
        return None
    return f"CH{int(check_id):03d}-OP{int(result[0]) + 1:03d}"


if __name__ == "__main__":
    print(get_all_operations())
