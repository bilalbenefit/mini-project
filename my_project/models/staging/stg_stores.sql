select
    storekey::int as store_id
    , country as store_country
    , state as store_state
    , square_meters as store_wide
    , open_date::date as store_open_date
from {{ source('raw', 'stores') }}
