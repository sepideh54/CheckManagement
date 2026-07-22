from database import Database


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

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

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
        customer_name,
        organization_name,
        customer_phone,
        customer_mobile,
        customer_address,
        customer_code
    )

    cursor.execute(query, values)
    connection.commit()

    print("Customer added successfully.")

    cursor.close()
    db.close()


# -----------------------
# Read All
# -----------------------
def get_all_customers():

    db = Database()
    connection = db.connect()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customer_table")

    customers = cursor.fetchall()

    cursor.close()
    db.close()

    return customers


# -----------------------
# Read By ID
# -----------------------
def get_customer(customer_id):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM customer_table WHERE customer_id=%s",
        (customer_id,)
    )

    customer = cursor.fetchone()

    cursor.close()
    db.close()

    return customer

# -----------------------
# Read By Name
# -----------------------

def get_customer_by_name(customer_name):

    db = Database()
    connection = db.connect()
    cursor = connection.cursor()

    query = """
        SELECT *
        FROM customer_table
        WHERE customer_name = %s
    """

    cursor.execute(query, (customer_name,))

    return cursor.fetchall()

# -----------------------
# Update
# -----------------------
def update_customer(
    customer_id,
    customer_name,
    organization_name,
    phone,
    mobile,
    address
):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    UPDATE customer_table
    SET
        customer_name=%s,
        organization_name=%s,
        phone=%s,
        mobile=%s,
        address=%s
    WHERE customer_id=%s
    """

    values = (
        customer_name,
        organization_name,
        phone,
        mobile,
        address,
        customer_id
    )

    cursor.execute(query, values)
    connection.commit()

    print("Customer updated successfully.")

    cursor.close()
    db.close()


# -----------------------
# Delete
# -----------------------
def delete_customer(customer_id):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM customer_table WHERE customer_id=%s",
        (customer_id,)
    )

    connection.commit()

    print("Customer deleted successfully.")

    cursor.close()
    db.close()

# -----------------------
# Generate code
# -----------------------
def generate_customer_code():

    db = Database()
    connection = db.connect()
    cursor = connection.cursor()

    query = """
        SELECT customer_code
        FROM customer_table
        ORDER BY customer_id DESC
        LIMIT 1
    """

    cursor.execute(query)
    result = cursor.fetchone()

    if result is None:
        return "C0001"

    last_code = result[0]      # مثال: C0042
    number = int(last_code[1:]) + 1

    return f"C{number:04d}"
# -----------------------
# Test
# -----------------------
if __name__ == "__main__":

    customers = get_all_customers()

    for customer in customers:
        print(customer)