select
    order_number::int as order_number
    , line_item::int as line_item
    , order_date::date as order_date
    , delivery_date::date as delivery_date
    , customerkey::int as customer_id
    , storekey::int as store_id
    , productkey::int as product_id
    , quantity::int as order_qty
    , currency_code as order_currency_code
from {{ source('raw', 'sales') }}
