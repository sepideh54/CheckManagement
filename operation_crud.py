from database import get_connection


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

    connection = get_connection()

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

    operation_id = cursor.lastrowid

    cursor.close()
  

    return operation_id

# -----------------------
# Read All Operations
# -----------------------
def get_all_operations():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM operation")

    operations = cursor.fetchall()

    cursor.close()
   

    return operations


# -----------------------
# Read Operation By ID
# -----------------------
def get_operation(operation_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM operation
    WHERE operation_id=%s
    """

    cursor.execute(query, (operation_id,))

    operation = cursor.fetchone()

    cursor.close()


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

    connection = get_connection()
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



# -----------------------
# Delete Operation
# -----------------------
def delete_operation(operation_id):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    DELETE FROM operation
    WHERE operation_id=%s
    """

    cursor.execute(query, (operation_id,))

    connection.commit()

    print("Operation deleted successfully.")

    cursor.close()
  


# -----------------------
# Test
# -----------------------
if __name__ == "__main__":

    operations = get_all_operations()

    for operation in operations:
        print(operation)