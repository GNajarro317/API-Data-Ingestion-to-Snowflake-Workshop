-- Set context
USE ROLE ACCOUNTADMIN;
USE DATABASE WORKSHOP_DB;
USE SCHEMA GN_RAW;

-- Create landing tables with the 2-column pattern

CREATE OR REPLACE TABLE RAW_POSTS (
    INGESTED_AT TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
    RAW_PAYLOAD VARIANT
);

-- On your own, make two more: raw_comments and raw_users

-- create raw comments table

-- create raw users table