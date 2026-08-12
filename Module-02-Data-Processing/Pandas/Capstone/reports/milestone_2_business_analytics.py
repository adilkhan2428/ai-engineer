import pandas as pd


# ============================================================
# MILESTONE 2 — BUSINESS ANALYTICS
# ============================================================
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
REPORTS_DIR = PROJECT_ROOT / "reports"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)

completed_orders = pd.read_csv(
    "Module-02-Data-Processing\\Pandas\\Capstone\\data\\completed_orders.csv"
)

completed_orders["Order Date"] = pd.to_datetime(
    completed_orders["Order Date"]
)


# ============================================================
# 1. Executive KPI Summary
# ============================================================

profitability_orders = completed_orders[
    completed_orders["Total Cost"].notna()
]

total_revenue = completed_orders["Revenue"].sum()

total_units_sold = completed_orders["Units Sold"].sum()

number_of_orders = completed_orders["Order ID"].nunique()

total_cost = profitability_orders["Total Cost"].sum()

total_profit = profitability_orders["Profit"].sum()

average_order_value = (
    total_revenue / number_of_orders
)

profit_margin = (
    total_profit
    / profitability_orders["Revenue"].sum()
    * 100
)

executive_kpis = pd.Series({
    "Total Revenue": total_revenue,
    "Total Units Sold": total_units_sold,
    "Number of Orders": number_of_orders,
    "Average Order Value": average_order_value,
    "Total Cost": total_cost,
    "Total Profit": total_profit,
    "Profit Margin %": profit_margin
})

print("\n================ EXECUTIVE KPIs ================")
print(executive_kpis)


# ============================================================
# 2. Product Performance
# ============================================================

product_performance = (
    completed_orders
    .groupby(
        ["Product Name", "Category"],
        as_index=False
    )
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Units_Sold=("Units Sold", "sum"),
        Number_of_Orders=("Order ID", "count"),
        Average_Revenue_per_Order=("Revenue", "mean")
    )
)

product_performance["Revenue_Rank"] = (
    product_performance["Total_Revenue"]
    .rank(
        ascending=False,
        method="dense"
    )
)

product_performance = (
    product_performance
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
)

print("\n================ PRODUCT PERFORMANCE ================")
print(product_performance)


# ============================================================
# 3. Product Profitability
# ============================================================

product_profitability = (
    completed_orders[
        completed_orders["Total Cost"].notna()
    ]
    .groupby(
        ["Product Name", "Category"],
        as_index=False
    )
    .agg(
        Total_Cost=("Total Cost", "sum"),
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Orders=("Order ID", "count")
    )
)

product_profitability["Profit Margin %"] = (
    product_profitability["Total_Profit"]
    / product_profitability["Total_Revenue"]
    * 100
)

product_profitability = (
    product_profitability
    .sort_values(
        "Total_Profit",
        ascending=False
    )
)

print("\n================ PRODUCT PROFITABILITY ================")
print(product_profitability)


# ============================================================
# 4. Loss-Making Products
# ============================================================

loss_making_products = product_profitability[
    product_profitability["Total_Profit"] < 0
].copy()

loss_making_products = (
    loss_making_products
    .sort_values("Total_Profit")
)

print("\n================ LOSS-MAKING PRODUCTS ================")
print(loss_making_products)


# ============================================================
# 5. Customer Value Analysis
# ============================================================

customer_value = (
    completed_orders
    .groupby(
        [
            "Customer ID",
            "Customer Name",
            "Region",
            "Customer Segment"
        ],
        as_index=False
    )
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Orders=("Order ID", "count"),
        Average_Revenue_per_Order=("Revenue", "mean")
    )
)

customer_value["Profit Margin %"] = (
    customer_value["Total_Profit"]
    / customer_value["Total_Revenue"]
    * 100
)

customer_value = (
    customer_value
    .sort_values(
        "Total_Profit",
        ascending=False
    )
)

print("\n================ CUSTOMER VALUE ================")
print(customer_value)


# ============================================================
# 6. Regional Performance
# ============================================================

regional_performance = (
    completed_orders
    .groupby(
        "Region",
        as_index=False
    )
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Orders=("Order ID", "count")
    )
)

regional_performance["Average Revenue per Order"] = (
    regional_performance["Total_Revenue"]
    / regional_performance["Number_of_Orders"]
)

regional_performance["Profit Margin %"] = (
    regional_performance["Total_Profit"]
    / regional_performance["Total_Revenue"]
    * 100
)

regional_performance["Revenue Share %"] = (
    regional_performance["Total_Revenue"]
    / regional_performance["Total_Revenue"].sum()
    * 100
)

regional_performance = (
    regional_performance
    .sort_values(
        "Total_Profit",
        ascending=False
    )
)

print("\n================ REGIONAL PERFORMANCE ================")
print(regional_performance)


# ============================================================
# 7. Customer Segment Performance
# ============================================================

segment_performance = (
    completed_orders
    .groupby(
        "Customer Segment",
        as_index=False
    )
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Units_Sold=("Units Sold", "sum"),
        Number_of_Orders=("Order ID", "count"),
        Average_Revenue_per_Order=("Revenue", "mean")
    )
)

segment_performance["Revenue Share %"] = (
    segment_performance["Total_Revenue"]
    / segment_performance["Total_Revenue"].sum()
    * 100
)

segment_performance["Profit Margin %"] = (
    segment_performance["Total_Profit"]
    / segment_performance["Total_Revenue"]
    * 100
)

segment_performance = (
    segment_performance
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
)

print("\n================ CUSTOMER SEGMENTS ================")
print(segment_performance)


# ============================================================
# 8. Payment Method Performance
# ============================================================

payment_performance = (
    completed_orders
    .groupby(
        "Payment Method",
        as_index=False
    )
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Units_Sold=("Units Sold", "sum"),
        Number_of_Orders=("Order ID", "count")
    )
)

payment_performance["Profit Margin %"] = (
    payment_performance["Total_Profit"]
    / payment_performance["Total_Revenue"]
    * 100
)

payment_performance["Revenue Share %"] = (
    payment_performance["Total_Revenue"]
    / payment_performance["Total_Revenue"].sum()
    * 100
)

payment_performance = (
    payment_performance
    .sort_values(
        "Total_Profit",
        ascending=False
    )
)

print("\n================ PAYMENT PERFORMANCE ================")
print(payment_performance)


# ============================================================
# 9. Monthly Performance
# ============================================================

monthly_performance = (
    completed_orders
    .groupby(
        "Month",
        as_index=False
    )
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Cost=("Total Cost", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Orders=("Order ID", "count")
    )
    .sort_values("Month")
)

monthly_performance["Profit Margin %"] = (
    monthly_performance["Total_Profit"]
    / monthly_performance["Total_Revenue"]
    * 100
)

monthly_performance["Average Order Value"] = (
    monthly_performance["Total_Revenue"]
    / monthly_performance["Number_of_Orders"]
)

monthly_performance["Revenue Change %"] = (
    monthly_performance["Total_Revenue"]
    .pct_change()
    * 100
)

monthly_performance["Profit Change %"] = (
    monthly_performance["Total_Profit"]
    .pct_change()
    * 100
)

print("\n================ MONTHLY PERFORMANCE ================")
print(monthly_performance)


# ============================================================
# 10. Revenue Concentration
# ============================================================

revenue_concentration = (
    completed_orders
    .groupby(
        ["Product Name", "Category"],
        as_index=False
    )
    .agg(
        Total_Revenue=("Revenue", "sum")
    )
)

revenue_concentration["Revenue Share %"] = (
    revenue_concentration["Total_Revenue"]
    / revenue_concentration["Total_Revenue"].sum()
    * 100
)

revenue_concentration["Revenue Rank"] = (
    revenue_concentration["Total_Revenue"]
    .rank(
        ascending=False,
        method="dense"
    )
)

revenue_concentration = (
    revenue_concentration
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
)

print("\n================ REVENUE CONCENTRATION ================")
print(revenue_concentration)


# ============================================================
# 11. Product Revenue vs Profit Ranking
# ============================================================

product_rank_comparison = (
    product_profitability[
        [
            "Product Name",
            "Category",
            "Total_Revenue",
            "Total_Profit"
        ]
    ]
    .copy()
)

product_rank_comparison["Revenue Rank"] = (
    product_rank_comparison["Total_Revenue"]
    .rank(
        ascending=False,
        method="dense"
    )
)

product_rank_comparison["Profit Rank"] = (
    product_rank_comparison["Total_Profit"]
    .rank(
        ascending=False,
        method="dense"
    )
)

product_rank_comparison["Rank Gap"] = (
    product_rank_comparison["Revenue Rank"]
    - product_rank_comparison["Profit Rank"]
)

product_rank_comparison = (
    product_rank_comparison
    .sort_values(
        "Rank Gap",
        ascending=False
    )
)

print("\n================ REVENUE VS PROFIT RANKING ================")
print(product_rank_comparison)


# ============================================================
# 12. Regional + Customer Segment
# ============================================================

regional_segment = (
    completed_orders
    .groupby(
        ["Region", "Customer Segment"],
        as_index=False
    )
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Orders=("Order ID", "count")
    )
)

regional_segment["Region Total Revenue"] = (
    regional_segment
    .groupby("Region")["Total_Revenue"]
    .transform("sum")
)

regional_segment["Revenue Share Within Region %"] = (
    regional_segment["Total_Revenue"]
    / regional_segment["Region Total Revenue"]
    * 100
)

regional_segment = (
    regional_segment
    .sort_values(
        ["Region", "Total_Revenue"],
        ascending=[True, False]
    )
)

print("\n================ REGIONAL + SEGMENT ================")
print(regional_segment)


# ============================================================
# 13. Monthly Rolling / Expanding Analysis
# ============================================================

monthly_windows = monthly_performance[
    [
        "Month",
        "Total_Revenue",
        "Total_Profit",
        "Number_of_Orders"
    ]
].copy()

monthly_windows["Rolling 2 Month Revenue"] = (
    monthly_windows["Total_Revenue"]
    .rolling(
        window=2,
        min_periods=1
    )
    .sum()
)

monthly_windows["Rolling 2 Month Average Revenue"] = (
    monthly_windows["Total_Revenue"]
    .rolling(
        window=2,
        min_periods=1
    )
    .mean()
)

monthly_windows["Cumulative Revenue"] = (
    monthly_windows["Total_Revenue"]
    .expanding()
    .sum()
)

print("\n================ MONTHLY WINDOWS ================")
print(monthly_windows)


# ============================================================
# 14. Save Analysis Results
# ============================================================

reports = {
    "executive_kpis": executive_kpis,
    "product_performance": product_performance,
    "product_profitability": product_profitability,
    "loss_making_products": loss_making_products,
    "customer_value": customer_value,
    "regional_performance": regional_performance,
    "segment_performance": segment_performance,
    "payment_performance": payment_performance,
    "monthly_performance": monthly_performance,
    "revenue_concentration": revenue_concentration,
    "product_rank_comparison": product_rank_comparison,
    "regional_segment": regional_segment,
    "monthly_windows": monthly_windows
}


for name, report in reports.items():

    filename = f"{name}.csv"

    if isinstance(report, pd.Series):
        report.rename_axis("Metric").rename("Value").to_csv(
            REPORTS_DIR / filename
        )
    else:
        report.to_csv(
            REPORTS_DIR / filename,
            index=False
        )

print("\nMilestone 2 completed successfully.")