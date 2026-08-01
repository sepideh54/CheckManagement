from database import get_connection
# ----------------------------
# Create
# ----------------------------
def create_check(
    check_code,
    sayadi_number,
    customer_id,
    amount,
    due_date,
    bank_id,
    front_image,
    back_image,
    description
):

    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    query = """
    INSERT INTO check_table
    (
        check_code,
        sayadi_number,
        customer_id,
        amount,
        due_date,
        bank_id,
        front_image,
        back_image,
        description,
        created_at
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,CURDATE())
    """

    values = (
        check_code,
        sayadi_number,
        customer_id,
        amount,
        due_date,
        bank_id,
        front_image,
        back_image,
        description
    )

    cursor.execute(query, values)

    conn.commit()

    check_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return check_id

# ----------------------------
# Read All
# ----------------------------
def get_all_checks():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM check_table")

    checks = cursor.fetchall()

    cursor.close()
    conn.close()

    return checks


# ----------------------------
# Read By Sayadi Number
# ----------------------------
def get_check_by_sayadi(sayadi_number):

    conn = get_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    query = """
    SELECT *
    FROM check_table
    WHERE sayadi_number=%s
    """

    cursor.execute(query, (sayadi_number,))

    check = cursor.fetchone()

    cursor.close()
    conn.close()

    return check


# ----------------------------
# Update
# ----------------------------
def update_check(
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

    conn = get_connection()

    if conn is None:
        return False

    cursor = conn.cursor()

    query = """
    UPDATE check_table
    SET
        customer_id=%s,
        amount=%s,
        due_date=%s,
        bank_id=%s,
        issuer_name=%s,
        front_image=%s,
        back_image=%s,
        description=%s
    WHERE sayadi_number=%s
    """

    values = (
        customer_id,
        amount,
        due_date,
        bank_id,
        issuer_name,
        front_image,
        back_image,
        description,
        sayadi_number
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    return True


# ----------------------------
# Delete
# ----------------------------
def delete_check(sayadi_number):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM check_table
    WHERE sayadi_number=%s
    """

    cursor.execute(query, (sayadi_number,))

    conn.commit()

    print("Check deleted successfully.")

    cursor.close()
    conn.close()


## -----------------------
# Generate Check Code
# -----------------------
def generate_checkinfo_code():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT check_code
        FROM check_table
        ORDER BY check_id DESC
        LIMIT 1
        """
    )

    result = cursor.fetchone()

    if not result:

        new_code = "CH001"

    else:

        last_code = result[0]

        try:

            number = int(last_code[2:]) + 1

            new_code = f"CH{number:03d}"

        except ValueError:

            new_code = "CH001"


    cursor.close()
    conn.close()

    return new_code
 
# ----------------------------
# Test
# ----------------------------
if __name__ == "__main__":

    checks = get_all_checks()

    for check in checks:
        print(check)