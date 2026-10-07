with source as (
        select * from {{ source('jsonplaceholder', 'raw_posts') }}
  ),
  renamed as (
    select
       d.value:id::int as post_id
      ,d.value:userId::int as user_id
      ,d.value:title::string as post_title
      ,d.value:body::string as post_body
    from source,
      lateral flatten(input => RAW_PAYLOAD) d
  )
  select * from renamed
    