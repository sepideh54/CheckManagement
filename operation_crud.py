from database import Database


# -----------------------
# Create Operation
# -----------------------
def create_operation(
    check_id,
    operation_type,
    operation_date,
    related_person,
    description,
    sayad_system_status
):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    INSERT INTO operation
    (
        check_id,
        operation_type,
        operation_date,
        related_person,
        description,
        sayad_system_status
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        check_id,
        operation_type,
        operation_date,
        related_person,
        description,
        sayad_system_status
    )

    cursor.execute(query, values)
    connection.commit()

    print("Operation added successfully.")

    cursor.close()
    db.close()


# -----------------------
# Read All Operations
# -----------------------
def get_all_operations():

    db = Database()
    connection = db.connect()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM operation")

    operations = cursor.fetchall()

    cursor.close()
    db.close()

    return operations


# -----------------------
# Read Operation By ID
# -----------------------
def get_operation(operation_id):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM operation
    WHERE operation_id=%s
    """

    cursor.execute(query, (operation_id,))

    operation = cursor.fetchone()

    cursor.close()
    db.close()

    return operation


# -----------------------
# Update Operation
# -----------------------
def update_operation(
    operation_id,
    operation_type,
    operation_date,
    related_person,
    description,
    sayad_system_status
):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    UPDATE operation
    SET
        operation_type=%s,
        operation_date=%s,
        related_person=%s,
        description=%s,
        sayad_system_status=%s
    WHERE operation_id=%s
    """

    values = (
        operation_type,
        operation_date,
        related_person,
        description,
        sayad_system_status,
        operation_id
    )

    cursor.execute(query, values)

    connection.commit()

    print("Operation updated successfully.")

    cursor.close()
    db.close()


# -----------------------
# Delete Operation
# -----------------------
def delete_operation(operation_id):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    DELETE FROM operation
    WHERE operation_id=%s
    """

    cursor.execute(query, (operation_id,))

    connection.commit()

    print("Operation deleted successfully.")

    cursor.close()
    db.close()


# -----------------------
# Test
# -----------------------
if __name__ == "__main__":

    operations = get_all_operations()

    for operation in operations:
        print(operation)