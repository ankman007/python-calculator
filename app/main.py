import psycopg2, os

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
print("Table created successfully.")

# Inserting data into the table
insert_query = """
INSERT INTO calculations (operation, operand1, operand2, result)
VALUES (%s, %s, %s, %s);
"""
data_to_insert = ('addition', 10, 20, 30)
cur.execute(insert_query, data_to_insert)
print("Data inserted successfully.")

# Selecting data from the table
select_query = "SELECT * FROM calculations;"
cur.execute(select_query)
rows = cur.fetchall()
for row in rows:
    print(row)

# Updating data in the table
update_query = """
UPDATE calculations
SET result = %s
WHERE id = %s;
"""
cur.execute(update_query, (35, 1))
print("Data updated successfully.")

# Deleting data from the table
delete_query = """
DELETE FROM calculations
WHERE id = %s;
"""
cur.execute(delete_query, (1,))
print("Data deleted successfully.")

# Dropping the table 
drop_table_query = "DROP TABLE IF EXISTS calculations;"
cur.execute(drop_table_query)
print("Table dropped successfully.")

conn.commit()

cur.close()
conn.close()
