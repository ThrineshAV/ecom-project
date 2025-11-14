# Synthetic E-Commerce Data Project (Cursor IDE + SQLite)

This project demonstrates how to:

1. Generate synthetic e-commerce data using Cursor AI
2. Store generated CSVs (5 files)
3. Ingest the CSV files into a SQLite database
4. Run advanced SQL queries joining multiple tables

This entire project can be completed inside **Cursor IDE**.

---

## 📁 Project Structure

```
ecommerce-synthetic-project/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── payments.csv
│
├── load_to_sqlite.py
├── queries.sql
└── README.md
```

---

## 📌 Step 1 — Generate Synthetic Data (Cursor Prompt)

Use this prompt inside Cursor:

> Generate 5 synthetic e-commerce CSV files with realistic relational structure.  
> Each CSV must contain **200–300 rows**.
>
> Files required:  
> - customers.csv — customer_id, name, email, gender, signup_date  
> - products.csv — product_id, product_name, category, price  
> - orders.csv — order_id, customer_id, order_date, status  
> - order_items.csv — item_id, order_id, product_id, quantity  
> - payments.csv — payment_id, order_id, amount, payment_method, payment_date  
>
> Ensure foreign keys match properly.  
> Save them to `data/` folder.

---

## 📌 Step 2 — Load Data into SQLite

Run the script:

```
python load_to_sqlite.py
```

This creates:

- `ecommerce.db`
- 5 relational tables
- Inserts all CSV data automatically

---

## 📌 Step 3 — Run SQL Queries

Load SQLite database:

```
sqlite3 ecommerce.db
.read queries.sql
```

OR copy-paste queries manually.

---

## 📌 Step 4 — SQL Reports Included

The `queries.sql` file contains:

- Total revenue per customer
- Product sales summary
- Order breakdown
- Payment method analysis
- Monthly revenue report

---

## ✔️ Project Is Ready for GitHub Upload

Just push this folder into your repo:

```
git init
git add .
git commit -m "Initial commit: synthetic ecommerce project"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

---

## 🏁 Done!

You now have a complete AI-generated SDLC workflow:
- Data generation
- ETL ingestion
- SQL analytics
- Full GitHub-ready structure
