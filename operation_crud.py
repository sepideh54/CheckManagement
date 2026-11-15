"""CRUD operations for check lifecycle events."""
from datetime import date
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


def _validate_operation_fields(operation_code, operation_type, operation_date,
                               related_person, sayad_system_status):
    code = (operation_code or "").strip()
    kind = (operation_type or "").strip()
    if not code or not kind or not operation_date:
        raise ValueError("Operation code, type and date are required.")
    if len(code) > 40 or len(kind) > 100:
        raise ValueError("Operation code or type exceeds the supported length.")
    try:
        parsed_date = date.fromisoformat(str(operation_date))
    except (TypeError, ValueError):
        raise ValueError("Operation date must use the YYYY-MM-DD format.")
    if parsed_date.isoformat() != str(operation_date):
        raise ValueError("Operation date must use the YYYY-MM-DD format.")

    person = (str(related_person).strip() or None) if related_person is not None else None
    status = (str(sayad_system_status).strip() or None) if sayad_system_status is not None else None
    description = (str(description_value).strip() or None) if (description_value := None) else None
    if person is not None and len(person) > 150:
        raise ValueError("Related person cannot exceed 150 characters.")
    if status is not None and len(status) > 100:
        raise ValueError("Sayad system status cannot exceed 100 characters.")
    return code, kind, parsed_date.isoformat(), person, status


def create_operation(check_id, operation_code, operation_type,
                     operation_date, related_person=None, description=None,
                     sayad_system_status=None):
    try:
        check_identifier = int(check_id)
    except (TypeError, ValueError):
        raise ValueError("Check ID must be a positive integer.")
    if check_identifier <= 0:
        raise ValueError("Check ID must be a positive integer.")
    code, kind, event_date, person, status = _validate_operation_fields(
        operation_code, operation_type, operation_date,
        related_person, sayad_system_status,
    )
    if description is not None:
        description = str(description).strip() or None
    return _execute(
        """INSERT INTO operation
           (check_id, operation_code, operation_type, operation_date,
            related_person, description, sayad_system_status)
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (check_identifier, code, kind, event_date,
         person, description, status),
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
    try:
        identifier = int(operation_id)
    except (TypeError, ValueError):
        raise ValueError("Operation ID must be a positive integer.")
    if identifier <= 0:
        raise ValueError("Operation ID must be a positive integer.")
    existing = _validate_operation_fields(
        "EXISTING", operation_type, operation_date,
        related_person, sayad_system_status,
    )
    _, kind, event_date, person, status = existing
    if description is not None:
        description = str(description).strip() or None
    return bool(_execute(
        """UPDATE operation SET operation_type=%s, operation_date=%s,
               related_person=%s, description=%s, sayad_system_status=%s
           WHERE operation_id=%s""",
        (kind, event_date, person, description,
         status, identifier),
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
