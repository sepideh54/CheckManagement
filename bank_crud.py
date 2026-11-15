from database import get_connection


def create_bank(bank_name):
    connection = get_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO bank_table (bank_name) VALUES (%s)",
            (bank_name,),
        )
        connection.commit()
        return cursor.lastrowid
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def get_all_banks():
    connection = get_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT bank_id, bank_name FROM bank_table ORDER BY bank_name"
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()


def get_bank(bank_id):
    connection = get_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM bank_table WHERE bank_id=%s",
            (bank_id,),
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        connection.close()


def update_bank(bank_id, bank_name):
    connection = get_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE bank_table SET bank_name=%s WHERE bank_id=%s",
            (bank_name, bank_id),
        )
        connection.commit()
        return cursor.rowcount > 0
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def delete_bank(bank_id):
    connection = get_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM bank_table WHERE bank_id=%s",
            (bank_id,),
        )
        connection.commit()
        return cursor.rowcount > 0
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    for bank in get_all_banks():
        print(bank)
