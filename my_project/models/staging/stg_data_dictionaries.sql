select
    row_number() over () as data_dictionary_id
    , table_name
    , field as table_field
    , description as table_description
from {{ source('raw', 'data_dictionary') }}
