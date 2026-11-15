"""Database operations for customers.

All SQL values are parameterized. Functions return stable values and always
release their cursor and connection.
"""
from database import get_connection


def _run(query, values=(), *, fetch=None, dictionary=False):
    connection = get_connection()
    if connection is None:
        return None
    cursor = None
    try:
        cursor = connection.cursor(dictionary=dictionary) if dictionary else connection.cursor()
        cursor.execute(query, values)
        if fetch == "one":
            result = cursor.fetchone()
        elif fetch == "all":
            result = cursor.fetchall()
        else:
            connection.commit()
            result = cursor.lastrowid if fetch == "id" else cursor.rowcount
        return result
    except Exception:
        connection.rollback()
        raise
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def create_customer(customer_code, customer_name, organization_name=None,
                    customer_phone=None, customer_mobile=None,
                    customer_address=None):
    if not customer_code or not customer_name or not customer_name.strip():
        raise ValueError("Customer code and name are required.")
    return _run(
        """INSERT INTO customer_table
           (customer_code, customer_name, organization_name, customer_phone,
            customer_mobile, customer_address)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (customer_code.strip(), customer_name.strip(),
         organization_name or None, customer_phone or None,
         customer_mobile or None, customer_address or None),
        fetch="id",
    )


def get_all_customers():
    return _run(
        """SELECT customer_id, customer_code, customer_name, organization_name,
                  customer_phone, customer_mobile, customer_address
           FROM customer_table ORDER BY customer_name, customer_id""",
        fetch="all", dictionary=True,
    ) or []


def get_customer(customer_id):
    if not customer_id:
        return None
    return _run(
        "SELECT * FROM customer_table WHERE customer_id=%s",
        (customer_id,), fetch="one", dictionary=True,
    )


def get_customer_by_name(customer_name=None, organization_name=None):
    if not customer_name and not organization_name:
        raise ValueError("Enter a customer name or organization name.")
    clauses, values = [], []
    if customer_name:
        clauses.append("customer_name LIKE %s")
        values.append(f"%{customer_name.strip()}%")
    if organization_name:
        clauses.append("organization_name LIKE %s")
        values.append(f"%{organization_name.strip()}%")
    return _run(
        "SELECT * FROM customer_table WHERE " + " AND ".join(clauses)
        + " ORDER BY customer_id LIMIT 1",
        tuple(values), fetch="one", dictionary=True,
    )


def update_customer(customer_id, customer_name, organization_name=None,
                    customer_phone=None, customer_mobile=None,
                    customer_address=None):
    if not customer_id or not customer_name or not customer_name.strip():
        raise ValueError("Customer ID and name are required.")
    return bool(_run(
        """UPDATE customer_table
           SET customer_name=%s, organization_name=%s, customer_phone=%s,
               customer_mobile=%s, customer_address=%s
           WHERE customer_id=%s""",
        (customer_name.strip(), organization_name or None,
         customer_phone or None, customer_mobile or None,
         customer_address or None, customer_id),
    ))


def delete_customer(customer_id):
    if not customer_id:
        return False
    return bool(_run(
        "DELETE FROM customer_table WHERE customer_id=%s", (customer_id,)
    ))


def generate_customer_code():
    result = _run(
        """SELECT COALESCE(MAX(CAST(SUBSTRING(customer_code, 2) AS UNSIGNED)), 0)
           FROM customer_table WHERE customer_code REGEXP '^C[0-9]+$'""",
        fetch="one",
    )
    if result is None:
        return None
    return f"C{int(result[0]) + 1:03d}"


if __name__ == "__main__":
    print(get_all_customers())
