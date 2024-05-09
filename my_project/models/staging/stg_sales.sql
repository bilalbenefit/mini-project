select
    order_number::number as order_number
    , line_item::number as line_item
    , order_date::date as order_date
    , delivery_date::date as delivery_date
    , customerkey::number as customer_id
    , storekey::number as store_id
    , productkey::number as product_id
    , quantity::number as order_qty
    , currency_code as order_currency_code
from {{ source('raw', 'sales') }}
