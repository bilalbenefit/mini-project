import psycopg2

path_and_table_names = [
    ('global_electronics_dataset/stores.csv', 'stores'),
    ('global_electronics_dataset/customers.csv', 'customers'),
    ('global_electronics_dataset/data_dictionary.csv', 'data_dictionary'),
    ('global_electronics_dataset/exchange_rates.csv', 'exchange_rates'),
    ('global_electronics_dataset/products.csv', 'products'),
    ('global_electronics_dataset/sales.csv', 'sales')
]

conn = psycopg2.connect(
    host='localhost',
    database='dataset',
    user='miniproject',
    password='myminiproject'
)
