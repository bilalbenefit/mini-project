select
    row_number() over () as exchange_rates_id
    , date::date as exchange_rates_date
    , currency
    , exchange
from {{ source('raw', 'exchange_rates') }}
