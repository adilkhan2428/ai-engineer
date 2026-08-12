
# Shopify Sales Analytics — Pandas Capstone

A realistic e-commerce sales analytics project built with **Python and Pandas**.

The project takes raw order and product data, processes and enriches it, performs business analytics, and produces executive-level reports.

## What the Project Does

The project is organized into three main stages:

### 1. Data Pipeline

* Loads raw `orders.csv` and `products.csv`
* Inspects and cleans the data
* Converts data types
* Filters completed orders
* Validates business data
* Cleans the product master
* Merges orders with product data
* Detects unmatched products
* Calculates:

  * Total Cost
  * Profit
  * Profit Margin
* Creates time-based features
* Calculates customer and segment revenue contributions
* Produces a data-quality summary
* Saves the processed dataset as CSV and Parquet

### 2. Business Analytics

Analyzes the processed sales data across multiple business dimensions:

* Executive KPIs
* Product performance
* Product profitability
* Loss-making products
* Customer value
* Regional performance
* Customer segment performance
* Payment-method performance
* Monthly performance
* Revenue concentration
* Revenue vs. profit ranking
* Regional and customer-segment analysis
* Monthly window-based analysis

### 3. Executive Reporting

Converts the analysis results into executive-friendly outputs:

* Business findings
* Monthly revenue visualization
* Top-product visualization
* Regional profit visualization
* Product profitability visualization
* Executive Excel workbook
* Executive summary text report

## Technologies Used

* **Python**
* **Pandas** — data cleaning, transformation, aggregation, analysis, and reporting
* **NumPy** — numerical operations and data validation
* **Matplotlib** — data visualization
* **Seaborn** — statistical/business visualizations
* **PyArrow** — Parquet data storage
* **OpenPyXL** — Excel workbook generation
* **Pathlib** — project paths and file management

## Project Flow

```text
Raw Orders + Product Data
          ↓
    Data Pipeline
          ↓
    Cleaned Dataset
          ↓
  Business Analytics
          ↓
   Analysis Results
          ↓
 Executive Reporting
          ↓
CSV / Parquet / Charts / Excel / Summary
```

## Project Output

The final project produces a processed sales dataset, business analysis datasets, visualizations, and an executive reporting package from the original raw e-commerce data.

Yes. Add a concise **Concepts Used** section. Based on the capstone we built, I’d write it like this:

## Concepts Used

### Pandas

* DataFrame and Series
* `read_csv()`
* Data inspection with `shape`, `head()`, `info()`
* Missing-value handling with `isna()` / `notna()`
* Duplicate detection
* Data type conversion with `to_numeric()` and `to_datetime()`
* String cleaning with `.str`
* Boolean filtering and `.query()`
* Column selection
* `groupby()`
* `.agg()`
* Aggregation functions: `sum()`, `mean()`, `count()`, `nunique()`
* `transform()`
* `merge()`
* Merge validation with `validate="many_to_one"`
* Sorting with `sort_values()`
* Ranking with `.rank()`
* Derived/calculated columns
* Datetime features with `.dt`
* `shift()`
* Rolling/window-style calculations
* Cumulative calculations
* CSV export with `to_csv()`
* Parquet export with `to_parquet()`
* Excel export with `ExcelWriter`

### NumPy

* `np.nan`
* Numerical validation and missing-value representation

### Matplotlib

* Line charts
* Bar charts
* Figure creation
* Titles and axis labels
* `tight_layout()`
* `savefig()`
* `close()`
* Figure sizing and DPI

### Seaborn

* `lineplot()`
* `barplot()`
* DataFrame-based visualization

### Python

* Functions and variables
* Lists
* Dictionaries
* Loops
* Conditional logic
* f-strings
* File handling
* `pathlib.Path`
* `isinstance()`

### Other Tools / Libraries

* **PyArrow** — Parquet file support
* **OpenPyXL** — Excel workbook generation
* **Pathlib** — project path and directory management
