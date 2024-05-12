select
    customerkey::int as customer_id
    , gender as customer_gender
    , name as customer_name
    , city as customer_city
    , state_code as customer_state_code
    , state as customer_state
    , zip_code as customer_zip_code
    , country as customer_country
    , continent as customer_continent
    , birthday::date as customer_birhtday
from {{ source('raw', 'customers') }}
