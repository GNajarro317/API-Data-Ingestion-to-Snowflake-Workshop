# API Data Ingestion into Snowflake (Starter Template)

Welcome to the **API Data Ingestion into Snowflake** template repository! This repository is designed for workshop sessions and lab exercises focused on pulling data from REST APIs and staging it directly into Snowflake using Python in preparation for `dbt`.

---

## 🛠️ Pre-Lab Configuration

To run this repository in your GitHub Codespace and connect it to your personal Snowflake account, you must update two configuration files with your personal details.

### Step 1: Set Up GitHub Secrets for Codespaces
Ensure you have saved your Snowflake credentials as **GitHub Secrets for Codespaces** in your repository or account settings:
* `SNOWFLAKE_USER`
* `SNOWFLAKE_PASSWORD`

### Step 2: Configure your dbt Profile
Open `.dbt/profiles.yml` and update the `account` and `schema` fields with your Snowflake Account Identifier and your personal initials:

```yaml
my_dbt_project:
  outputs:
    dev:
      account: "YOUR_ACCOUNT_IDENTIFIER"  # e.g., "JCWVQMU-FKB88198"
      role: "ACCOUNTADMIN"
      user: "{{ env_var('SNOWFLAKE_USER') }}"
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
      type: snowflake
      warehouse: "WORKSHOP_WH"
      database: "WORKSHOP_DB"
      schema: "YOUR_INITIALS"               # e.g., "LK"
      threads: 1
  target: dev

```

### Step 3: Configure Infrastructure Setup DDL
Open `infrastructure_setup/01_setup_database.sql` and update the schema name to reflect your personal initials:
```sql
USE ROLE ACCOUNTADMIN;

CREATE WAREHOUSE IF NOT EXISTS WORKSHOP_WH
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 60
    AUTO_RESUME = TRUE
    INITIALLY_SUSPENDED = TRUE;

-- Create the Database and Personal Raw Schema HERE

CREATE DATABASE IF NOT EXISTS WORKSHOP_DB;
CREATE SCHEMA IF NOT EXISTS WORKSHOP_DB.YOUR_INITIALS_RAW; 
-- e.g., WORKSHOP_DB.LK_RAW
```

### Step 4: Run Infrastructure DDL
Execute `infrastructure_setup/01_setup_database.sql` in your Snowflake environment (via Worksheet or VS Code Snowflake Extension) to establish your compute warehouse, database, and isolated schema before running ingestion scripts.

---

## 📁 Repository Structure
```
.
├── .dbt/
│   └── profiles.yml                  # dbt connection profiles mapped to GitHub Secrets
├── .devcontainer/
│   └── devcontainer.json             # Codespaces container configuration & env mapping
├── infrastructure_setup/
│   └── 01_setup_database.sql         # Bootstrap DDL for Warehouse, Database, and Schema
├── ingestion_scripts/                # Python API ingestion modules
└── README.md
```