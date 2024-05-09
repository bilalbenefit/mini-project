select
    productkey::number as product_id
    , product_name
    , brand as brand_name
    , color as product_color
    , unit_cost_usd as product_cost
    , unit_price_usd as product_price
    , subcategorykey::number as subcategory_id
    , subcategory as product_subcategory
    , categorykey::number as category_id
    , category as product_category
from {{ source('raw', 'products') }}
