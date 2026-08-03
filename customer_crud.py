from validators import is_persian_text
from database import get_connection


# -----------------------
# Create Customer
# -----------------------
def create_customer(
    customer_code,
    customer_name,
    organization_name,
    customer_phone,
    customer_mobile,
    customer_address
):

    conn = get_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    query = """
    INSERT INTO customer_table
    (
        customer_code,
        customer_name,
        organization_name,
        customer_phone,
        customer_mobile,
        customer_address
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        customer_code,
        customer_name,
        organization_name,
        customer_phone,
        customer_mobile,
        customer_address
    )

    cursor.execute(query, values)

    conn.commit()

    print("Customer added successfully.")

    cursor.close()
    conn.close()


# -----------------------
# Read All Customers
# -----------------------
def get_all_customers():

    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM customer_table"
    )

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return customers


# -----------------------
# Read Customer By ID
# -----------------------
def get_customer(customer_id):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM customer_table
        WHERE customer_id=%s
        """,
        (customer_id,)
    )

    customer = cursor.fetchone()

    cursor.close()
    conn.close()

    return customer


# -----------------------
# Search Customer
# -----------------------
def get_customer_by_name(customer_name=None, organization_name=None):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM customer_table
    WHERE 1=1
    """

    values = []


    if customer_name:
        query += """
        AND customer_name LIKE %s
        """
        values.append(f"%{customer_name}%")


    if organization_name:
        query += """
        AND organization_name LIKE %s
        """
        values.append(f"%{organization_name}%")


    cursor.execute(query, values)

    customer = cursor.fetchone()

    cursor.close()
    conn.close()

    return customer



# -----------------------
# Update Customer
# -----------------------
def update_customer(
    customer_id,
    customer_name,
    organization_name,
    customer_phone,
    customer_mobile,
    customer_address
):

    conn = get_connection()

    cursor = conn.cursor()


    query = """
    UPDATE customer_table
    SET
        customer_name=%s,
        organization_name=%s,
        customer_phone=%s,
        customer_mobile=%s,
        customer_address=%s

    WHERE customer_id=%s
    """


    values = (
        customer_name,
        organization_name,
        customer_phone,
        customer_mobile,
        customer_address,
        customer_id
    )


    cursor.execute(query, values)

    conn.commit()


    print("Customer updated successfully.")


    cursor.close()
    conn.close()



# -----------------------
# Delete Customer
# -----------------------
def delete_customer(customer_id):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM customer_table
        WHERE customer_id=%s
        """,
        (customer_id,)
    )


    conn.commit()


    print("Customer deleted successfully.")


    cursor.close()
    conn.close()



# -----------------------
# Generate Customer Code
# -----------------------
def generate_customer_code():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT customer_code
        FROM customer_table
        ORDER BY customer_id DESC
        LIMIT 1
        """
    )


    result = cursor.fetchone()


    if not result:

        new_code = "C001"


    else:

        last_code = result[0]


        try:

            number = int(last_code[1:]) + 1

            new_code = f"C{number:03d}"


        except ValueError:

            new_code = "C001"


    cursor.close()
    conn.close()


    return new_code

# -----------------------
# Get All Customers
# -----------------------
def get_all_customers():

    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT customer_id, customer_name
        FROM customer_table
        ORDER BY customer_name
    """)

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return customers
# -----------------------
# Test
# -----------------------
if __name__ == "__main__":


    customers = get_all_customers()


    for customer in customers:

        print(customer)