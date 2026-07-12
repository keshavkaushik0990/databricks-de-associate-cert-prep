# Databricks Certified Data Engineer Associate — Certification Study Notebooks

![Databricks Certified](https://img.shields.io/badge/Databricks-Certified_Data_Engineer_Associate-FF3621?style=flat&logo=databricks&logoColor=white)
![Status](https://img.shields.io/badge/Status-Passed_July_2026-1D9E75?style=flat)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-003366?style=flat&logo=databricks&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)

Hands-on notebooks written during preparation for the **Databricks Certified Data Engineer Associate** exam (passed July 2026).

These notebooks cover every major topic in the exam syllabus — from Delta Lake internals and Structured Streaming to Lakeflow Jobs, Lakeflow Spark Declarative Pipelines, and Unity Catalog security. Each folder maps directly to a core exam domain.

---

## Repository Structure

```
databricks-de-associate-cert-prep/
│
├── A_introduction-to-notebooks/          # Databricks workspace fundamentals
│   ├── 1. Notebook_Introduction.py
│   ├── 2-0. Magic_Commands.py
│   ├── 2-1. Environment_Variables_and_Functions.py
│   ├── 3. Databricks_Utilities.py
│   └── 4. Debugging Notebooks.py
│
├── B_introduction-to-unity-catalog/      # Unity Catalog setup & cloud storage access
│   ├── 1. Introduction to Unity Catalog.py
│   └── 2. Configure Access to Cloud Storage via Unity Catalog.py
│
├── C_ETL-with-apache-spark/              # Full ETL project using PySpark + Spark SQL
│   └── Gizmobox-ETL-Project/
│       ├── 01-09  → Extract phase (JSON, CSV, External Tables, JDBC, Images)
│       ├── 10-17  → Transform phase (Customers, Payments, Orders, Addresses)
│       ├── 18-19  → Gold layer (Joins, Monthly Summaries)
│       └── 20-21  → Advanced SQL (UDFs, Higher Order Functions)
│
├── D_ETL-with-apache-spark-streaming/    # Structured Streaming + Auto Loader
│   └── Gizmobox-ETL-Project-Streaming/
│       ├── 01. Ingest Customers Stream.py
│       ├── 02. Ingest Customers Auto Loader.py
│       ├── 03. Ingest Customers Auto Loader File Options.py
│       └── 04. Ingest Customers Auto Loader Schema Evolution.py
│
├── E_delta-lake/                         # Delta Lake internals & operations
│   ├── 01. Transaction Log.sql
│   ├── 02. History and Time Travel.sql
│   ├── 03. Create Table - Table & Column Properties.sql
│   ├── 04. Create or Replace & CTAS.sql
│   ├── 05. Insert Overwrite.sql
│   ├── 06. COPY INTO And MERGE Commands.sql
│   ├── 07. OPTIMIZE and ZORDER - Compaction.sql
│   └── 08. VACUUM - Remove unused files.sql
│
├── F_databricks-jobs/                    # Lakeflow Jobs — Bronze/Silver/Gold pipeline
│   ├── 01. bronze_companies.sql
│   ├── 02. silver_companies.sql
│   └── 03. gold_companies.sql
│
├── G_lakeflow-spark-declarative-pipelines/  # SDP (formerly Delta Live Tables)
│   ├── 01. Set-up Project Environment.sql
│   ├── 02. Process Customers Data.sql
│   ├── 03. Process Addresses Data.py
│   ├── 04. Process Orders Data.sql
│   └── 05. Create Customer Order Summary.sql
│
└── H_data-security/                      # Unity Catalog — Data Level Security
    ├── 01. Dynamic Views for Data Level Security.sql
    ├── 02. Row Filters and Column Masks.sql
    └── 03. ABAC Policies with Governed Tags.sql
```

---

## Key Concepts Covered

**Delta Lake**
- ACID transactions, transaction log internals
- Time Travel (`VERSION AS OF`, `TIMESTAMP AS OF`)
- `OPTIMIZE`, `ZORDER`, `VACUUM` for performance tuning
- `MERGE INTO` for upserts, `COPY INTO` for idempotent batch loads
- Schema evolution with `mergeSchema` and `overwriteSchema`

**Apache Spark & PySpark ETL**
- Reading multiple file formats: JSON (complex/nested), CSV, Parquet, Images
- Transformations: `withColumn`, `filter`, `groupBy`, `agg`, `join`
- Advanced SQL: CTEs, Window Functions, UDFs, Higher Order Functions
- Data Profiling and validation patterns

**Structured Streaming & Auto Loader**
- `readStream` / `writeStream` with Delta as sink
- Auto Loader (`cloudFiles`) for incremental file ingestion from cloud storage
- Checkpointing and fault tolerance
- Schema inference and schema evolution in Auto Loader

**Lakeflow Jobs (Databricks Workflows)**
- Multi-task job orchestration: Bronze → Silver → Gold
- Job clusters vs all-purpose clusters
- Retry logic, alerting, and job monitoring

**Lakeflow Spark Declarative Pipelines (formerly Delta Live Tables)**
- `CREATE OR REFRESH STREAMING TABLE` syntax
- Data quality expectations
- Pipeline development and monitoring
- Medallion Architecture (Bronze → Silver → Gold) implementation

**Governance & Security**
- Unity Catalog: 3-level namespace (catalog → schema → table)
- Dynamic Views for row and column level access control
- Row Filters and Column Masks
- ABAC (Attribute-Based Access Control) with Governed Tags

---

## Tools & Technologies

![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat&logo=databricks&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-003366?style=flat&logo=databricks&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=flat&logo=apachespark&logoColor=white)

- **Platform:** Databricks Community Edition (Serverless Compute)
- **Storage:** Databricks File System (DBFS) / Unity Catalog Volumes
- **Languages:** Python, PySpark, Spark SQL
- **Format:** Delta Lake

---

## How to Use These Notebooks

1. Log in to your **Databricks Community Edition** account at `community.cloud.databricks.com`
2. Go to **Workspace** → **Import**
3. Import individual `.py` or `.sql` files, or import the full folder
4. Attach to a **Serverless** cluster
5. Run cells sequentially — each notebook has numbered steps

> **Note:** Notebooks referencing Azure ADLS (`abfss://`) paths require an Azure-connected Databricks workspace. Running on Databricks Community Edition → replace with `/FileStore/` DBFS paths for local testing.

---

## About

**Keshav Kaushik** — Data Engineer with 3+ years of production experience at Maruti Suzuki India Limited (MSIL).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/keshav-kaushik-599162363/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/keshavkaushik0990)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:keshavkaushik0990@gmail.com)

---

*These notebooks were written as part of certification exam preparation. Course content credit: Ramesh Retnasamy — Databricks Certified Data Engineer Associate Ultimate Prep (Udemy).*
