-- Set context
USE ROLE ACCOUNTADMIN;

CREATE WAREHOUSE IF NOT EXISTS WORKSHOP_WH
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 60            -- Automatically suspends after 1 minute of inactivity
    AUTO_RESUME = TRUE           -- Automatically wakes up when a query runs
    INITIALLY_SUSPENDED = TRUE;  -- Starts suspended to save credits

-- Create the Database and Schema
CREATE DATABASE IF NOT EXISTS WORKSHOP_DB;
CREATE SCHEMA IF NOT EXISTS WORKSHOP_DB.LK_RAW;