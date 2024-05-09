import pandas as pd
from config import conn, path_and_table_names

dtype_map = {
    'int64': 'bigint',
    'float64': 'double precision',
    'object': 'text',
}


def transform_date_column(df, column_name, date_format='%m/%d/%Y'):
    df[column_name] = pd.to_datetime(df[column_name], format=date_format)
    df[column_name] = df[column_name].dt.strftime('%Y/%m/%d')


for path, table_name in path_and_table_names:
    df = pd.read_csv(path, encoding='latin1')
    df.columns = [col.title().replace(' ', '_').lower() for col in df.columns]

    date_columns = [
        'birthday',
        'order_date',
        'delivery_date',
        'open_date',
        'date'
    ]
    
    for col in date_columns:
        if col in df.columns:
            transform_date_column(df, col)

    columns = ', '.join([f"{col} {dtype_map.get(df[col].dtype.name, 'text')}" for col in df.columns]) # noqa
    query = f"DO $$ BEGIN CREATE TABLE IF NOT EXISTS {table_name} ({columns}); END; $$;" # noqa
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    for index, row in df.iterrows():
        row = row.where(pd.notnull(row), None)
        placeholders = ', '.join(['%s'] * len(row))
        columns = ', '.join(row.index)
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, tuple(row))
        conn.commit()

cursor.close()
conn.close()
