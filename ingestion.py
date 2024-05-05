import pandas as pd
from config import conn, path_and_table_names

dtype_map = {
    'int64': 'bigint',
    'float64': 'double precision',
    'object': 'text',
}

for path, table_name in path_and_table_names:
    df = pd.read_csv(path, encoding='latin1')
    df.columns = [col.title().replace(' ', '_').lower() for col in df.columns]

    columns = ', '.join([f"{col} {dtype_map.get(df[col].dtype.name, 'text')}" for col in df.columns]) # noqa
    query = f"DO $$ BEGIN CREATE TABLE IF NOT EXISTS {table_name} ({columns}); END; $$;" # noqa
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    for index, row in df.iterrows():
        placeholders = ', '.join(['%s'] * len(row))
        columns = ', '.join(row.index)
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, tuple(row))
        conn.commit()

cursor.close()
conn.close()
