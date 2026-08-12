import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# MILESTONE 3 — EXECUTIVE REPORT
# ============================================================

# ------------------------------------------------------------
# 1. Load Analysis Results
# ------------------------------------------------------------
from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parent / 'reports'

executive_kpis = pd.read_csv(REPORTS_DIR / "executive_kpis.csv")

product_performance = pd.read_csv(REPORTS_DIR / "product_performance.csv"
)

product_profitability = pd.read_csv(REPORTS_DIR /"product_profitability.csv"
)

loss_making_products = pd.read_csv(REPORTS_DIR/"loss_making_products.csv"
)

customer_value = pd.read_csv(REPORTS_DIR / "customer_value.csv"
)

regional_performance = pd.read_csv(
    REPORTS_DIR / "regional_performance.csv"
)

segment_performance = pd.read_csv(
    REPORTS_DIR / "segment_performance.csv"
)

payment_performance = pd.read_csv(
    REPORTS_DIR / "payment_performance.csv"
)

monthly_performance = pd.read_csv(
    REPORTS_DIR / "monthly_performance.csv"
)

revenue_concentration = pd.read_csv(
    REPORTS_DIR / "revenue_concentration.csv"
)

product_rank_comparison = pd.read_csv(
    REPORTS_DIR / "product_rank_comparison.csv"
)

regional_segment = pd.read_csv(
    REPORTS_DIR / "regional_segment.csv"
)

monthly_windows = pd.read_csv(
    REPORTS_DIR / "monthly_windows.csv"
)


# ============================================================
# 2. Business Findings
# ============================================================

most_profitable_product = (
    product_profitability
    .sort_values("Total_Profit", ascending=False)
    .iloc[0]
)

worst_product = (
    product_profitability
    .sort_values("Total_Profit")
    .iloc[0]
)

top_revenue_product = (
    product_performance
    .sort_values("Total_Revenue", ascending=False)
    .iloc[0]
)

top_region = (
    regional_performance
    .sort_values("Total_Profit", ascending=False)
    .iloc[0]
)

top_segment = (
    segment_performance
    .sort_values("Total_Revenue", ascending=False)
    .iloc[0]
)

top_payment_method = (
    payment_performance
    .sort_values("Total_Profit", ascending=False)
    .iloc[0]
)


print("\n================================================")
print("EXECUTIVE BUSINESS FINDINGS")
print("================================================")

print(
    f"\nTop revenue product: "
    f"{top_revenue_product['Product Name']} "
    f"(${top_revenue_product['Total_Revenue']:,.2f})"
)

print(
    f"\nMost profitable product: "
    f"{most_profitable_product['Product Name']} "
    f"(${most_profitable_product['Total_Profit']:,.2f})"
)

print(
    f"\nWorst product by profit: "
    f"{worst_product['Product Name']} "
    f"(${worst_product['Total_Profit']:,.2f})"
)

print(
    f"\nBest region by profit: "
    f"{top_region['Region']} "
    f"(${top_region['Total_Profit']:,.2f})"
)

print(
    f"\nLargest customer segment by revenue: "
    f"{top_segment['Customer Segment']} "
    f"(${top_segment['Total_Revenue']:,.2f})"
)

print(
    f"\nMost profitable payment method: "
    f"{top_payment_method['Payment Method']} "
    f"(${top_payment_method['Total_Profit']:,.2f})"
)


# ============================================================
# 3. Monthly Revenue Chart
# ============================================================

plt.figure(figsize=(9, 5))

sns.lineplot(
    data=monthly_performance,
    x="Month",
    y="Total_Revenue",
    marker="o"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(
    REPORTS_DIR / "monthly_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 4. Top Products Chart
# ============================================================

top_products = (
    product_performance
    .head(10)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=top_products,
    x="Total_Revenue",
    y="Product Name"
)

plt.title("Top Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    REPORTS_DIR / "top_products_by_revenue.png",
    dpi=150
)

plt.close()


# ============================================================
# 5. Regional Profit Chart
# ============================================================

plt.figure(figsize=(9, 5))

sns.barplot(
    data=regional_performance,
    x="Region",
    y="Total_Profit"
)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig(
    REPORTS_DIR / "profit_by_region.png",
    dpi=150
)

plt.close()


# ============================================================
# 6. Product Profitability Chart
# ============================================================

plt.figure(figsize=(10, 6))

sns.barplot(
    data=product_profitability,
    x="Total_Profit",
    y="Product Name"
)

plt.title("Product Profitability")
plt.xlabel("Total Profit")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    REPORTS_DIR /"product_profitability.png",
    dpi=150
)

plt.close()


# ============================================================
# 7. Executive Excel Workbook
# ============================================================

with pd.ExcelWriter(
    REPORTS_DIR / "executive_report.xlsx",
    engine= "openpyxl"
) as writer:

    executive_kpis.to_excel(
        writer,
        sheet_name="Executive KPIs"
    )

    product_performance.to_excel(
        writer,
        sheet_name="Product Performance",
        index=False
    )

    product_profitability.to_excel(
        writer,
        sheet_name="Product Profitability",
        index=False
    )

    loss_making_products.to_excel(
        writer,
        sheet_name="Loss Making Products",
        index=False
    )

    customer_value.to_excel(
        writer,
        sheet_name="Customer Value",
        index=False
    )

    regional_performance.to_excel(
        writer,
        sheet_name="Regional Performance",
        index=False
    )

    segment_performance.to_excel(
        writer,
        sheet_name="Segments",
        index=False
    )

    payment_performance.to_excel(
        writer,
        sheet_name="Payment Methods",
        index=False
    )

    monthly_performance.to_excel(
        writer,
        sheet_name="Monthly Performance",
        index=False
    )

    revenue_concentration.to_excel(
        writer,
        sheet_name="Revenue Concentration",
        index=False
    )

    product_rank_comparison.to_excel(
        writer,
        sheet_name="Product Rank Gap",
        index=False
    )

    regional_segment.to_excel(
        writer,
        sheet_name="Regional Segment",
        index=False
    )

    monthly_windows.to_excel(
        writer,
        sheet_name="Monthly Windows",
        index=False
    )


# ============================================================
# 8. Executive Summary Text File
# ============================================================

with open(
    REPORTS_DIR / "executive_summary.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write("SHOPIFY SALES ANALYTICS — EXECUTIVE SUMMARY\n")
    file.write("=" * 55 + "\n\n")

    file.write(
        f"Top revenue product: "
        f"{top_revenue_product['Product Name']} "
        f"(${top_revenue_product['Total_Revenue']:,.2f})\n"
    )

    file.write(
        f"Most profitable product: "
        f"{most_profitable_product['Product Name']} "
        f"(${most_profitable_product['Total_Profit']:,.2f})\n"
    )

    file.write(
        f"Worst product by profit: "
        f"{worst_product['Product Name']} "
        f"(${worst_product['Total_Profit']:,.2f})\n"
    )

    file.write(
        f"Best region by profit: "
        f"{top_region['Region']} "
        f"(${top_region['Total_Profit']:,.2f})\n"
    )

    file.write(
        f"Largest customer segment: "
        f"{top_segment['Customer Segment']} "
        f"(${top_segment['Total_Revenue']:,.2f})\n"
    )

    file.write(
        f"Most profitable payment method: "
        f"{top_payment_method['Payment Method']} "
        f"(${top_payment_method['Total_Profit']:,.2f})\n"
    )


print("\nMilestone 3 completed successfully.")
print("Executive report generated in the reports/ folder.")