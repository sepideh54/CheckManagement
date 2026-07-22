from database import Database


# ----------------------------
# Create
# ----------------------------
def create_check(
    sayadi_number,
    customer_id,
    amount,
    due_date,
    bank_id,
    issuer_name,
    front_image,
    back_image,
    description
):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    INSERT INTO check_table
    (
        sayadi_number,
        customer_id,
        amount,
        due_date,
        bank_id,
        issuer_name,
        front_image,
        back_image,
        description
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        sayadi_number,
        customer_id,
        amount,
        due_date,
        bank_id,
        issuer_name,
        front_image,
        back_image,
        description
    )

    cursor.execute(query, values)
    connection.commit()

    print("Check added successfully.")

    cursor.close()
    db.close()


# ----------------------------
# Read All
# ----------------------------
def get_all_checks():

    db = Database()
    connection = db.connect()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM check_table")

    checks = cursor.fetchall()

    cursor.close()
    db.close()

    return checks


# ----------------------------
# Read By Sayadi Number
# ----------------------------
def get_check_by_sayadi(sayadi_number):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM check_table
    WHERE sayadi_number=%s
    """

    cursor.execute(query, (sayadi_number,))

    check = cursor.fetchone()

    cursor.close()
    db.close()

    return check


# ----------------------------
# Update
# ----------------------------
def update_check(
    sayadi_number,
    amount,
    due_date,
    issuer_name,
    description
):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    UPDATE check_table
    SET
        amount=%s,
        due_date=%s,
        issuer_name=%s,
        description=%s
    WHERE sayadi_number=%s
    """

    values = (
        amount,
        due_date,
        issuer_name,
        description,
        sayadi_number
    )

    cursor.execute(query, values)

    connection.commit()

    print("Check updated successfully.")

    cursor.close()
    db.close()


# ----------------------------
# Delete
# ----------------------------
def delete_check(sayadi_number):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    DELETE FROM check_table
    WHERE sayadi_number=%s
    """

    cursor.execute(query, (sayadi_number,))

    connection.commit()

    print("Check deleted successfully.")

    cursor.close()
    db.close()


# ----------------------------
# Test
# ----------------------------
if __name__ == "__main__":

    checks = get_all_checks()

    for check in checks:
        print(check)