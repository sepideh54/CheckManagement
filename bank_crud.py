from database import Database


# -----------------------
# Create Bank
# -----------------------
def create_bank(bank_name):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    INSERT INTO bank_table (bank_name)
    VALUES (%s)
    """

    cursor.execute(query, (bank_name,))
    connection.commit()

    print("Bank added successfully.")

    cursor.close()
    db.close()


# -----------------------
# Read All Banks
# -----------------------
def get_all_banks():

    db = Database()
    connection = db.connect()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM bank_table")

    banks = cursor.fetchall()

    cursor.close()
    db.close()

    return banks


# -----------------------
# Read Bank By ID
# -----------------------
def get_bank(bank_id):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM bank_table
    WHERE bank_id=%s
    """

    cursor.execute(query, (bank_id,))

    bank = cursor.fetchone()

    cursor.close()
    db.close()

    return bank


# -----------------------
# Update Bank
# -----------------------
def update_bank(bank_id, bank_name):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    UPDATE bank_table
    SET bank_name=%s
    WHERE bank_id=%s
    """

    cursor.execute(query, (bank_name, bank_id))

    connection.commit()

    print("Bank updated successfully.")

    cursor.close()
    db.close()


# -----------------------
# Delete Bank
# -----------------------
def delete_bank(bank_id):

    db = Database()
    connection = db.connect()

    cursor = connection.cursor()

    query = """
    DELETE FROM bank_table
    WHERE bank_id=%s
    """

    cursor.execute(query, (bank_id,))

    connection.commit()

    print("Bank deleted successfully.")

    cursor.close()
    db.close()


# -----------------------
# Test
# -----------------------
if __name__ == "__main__":

    banks = get_all_banks()

    for bank in banks:
        print(bank)