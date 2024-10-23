import psycopg2, os
from loguru import logger

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "calculator_db"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASS", "password")
    )

    cur = conn.cursor()

    # Creating a new table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS calculations (
        id SERIAL PRIMARY KEY,
        operation VARCHAR(255),
        operand1 NUMERIC,
        operand2 NUMERIC,
        result NUMERIC,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cur.execute(create_table_query)
    logger.info("Table created successfully.")

    # Inserting data into the table
    insert_query = """
    INSERT INTO calculations (operation, operand1, operand2, result)
    VALUES (%s, %s, %s, %s);
    """
    data_to_insert = ('addition', 10, 20, 30)
    data_to_insert = ('subtract', 1, 1, 0)
    data_to_insert = ('mutiply', 2, 3, 6)
    data_to_insert = ('division', 10, 5, 2)
    cur.execute(insert_query, data_to_insert)
    logger.info("Data inserted successfully.")

    # Selecting data from the table
    select_query = "SELECT * FROM calculations;"
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        logger.info("Row: "+row)

    # Updating data in the table
    update_query = """
    UPDATE calculations
    SET result = %s
    WHERE id = %s;
    """
    cur.execute(update_query, (35, 1))
    logger.info("Data updated successfully.")

    # Deleting data from the table
    delete_query = """
    DELETE FROM calculations
    WHERE id = %s;
    """
    cur.execute(delete_query, (1,))
    logger.info("Data deleted successfully.")

    # Dropping the table 
    drop_table_query = "DROP TABLE IF EXISTS calculations;"
    cur.execute(drop_table_query)
    logger.info("Table dropped successfully.")

    conn.commit()

except psycopg2.Error as error:
    logger.error(f"Database error occured: {error}")

except Exception as error:
    logger.error(f"An occured when connecting to database: {error}")
    
finally:
    if conn:
        cur.close()
        conn.close()
        logger.info("Database connected closed.")
