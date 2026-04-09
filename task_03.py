import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# DISPLAY SETTINGS (FIX ADDED ✅)
# ==============================
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# ==============================
# LOAD DATA FROM CSV
# ==============================
df = pd.read_csv("data.csv")

print("\n🔹 Original Dataset:\n")
print(df.to_string())   # 👈 FULL VIEW

# ==============================
# CALCULATIONS
# ==============================
df["Visitor_to_Lead (%)"] = (df["Leads"] / df["Visitors"]) * 100
df["Lead_to_Customer (%)"] = (df["Customers"] / df["Leads"]) * 100
df["Drop Visitor→Lead (%)"] = 100 - df["Visitor_to_Lead (%)"]
df["Drop Lead→Customer (%)"] = 100 - df["Lead_to_Customer (%)"]

print("\n🔹 Dataset with Calculations:\n")
print(df.to_string())   # 👈 FULL VIEW (NO ...)

# ==============================
# CHANNEL SUMMARY
# ==============================
channel_summary = df.groupby("Channel").sum(numeric_only=True)

channel_summary["Visitor_to_Lead (%)"] = (channel_summary["Leads"] / channel_summary["Visitors"]) * 100
channel_summary["Lead_to_Customer (%)"] = (channel_summary["Customers"] / channel_summary["Leads"]) * 100
channel_summary["Drop Visitor→Lead (%)"] = 100 - channel_summary["Visitor_to_Lead (%)"]
channel_summary["Drop Lead→Customer (%)"] = 100 - channel_summary["Lead_to_Customer (%)"]

print("\n🔹 Channel-wise Summary:\n")
print(channel_summary.to_string())   # 👈 FULL VIEW

# ==============================
# INSIGHTS
# ==============================
best_channel = channel_summary["Lead_to_Customer (%)"].idxmax()
worst_channel = channel_summary["Lead_to_Customer (%)"].idxmin()

print("\n🔹 Key Insights:\n")
print("Best Channel:", best_channel)
print("Worst Channel:", worst_channel)

# ==============================
# OVERALL CONVERSION
# ==============================
total_visitors = df["Visitors"].sum()
total_leads = df["Leads"].sum()
total_customers = df["Customers"].sum()

visitor_to_lead = (total_leads / total_visitors) * 100
lead_to_customer = (total_customers / total_leads) * 100

print("\n🔹 Overall Conversion:\n")
print("Visitor → Lead:", round(visitor_to_lead, 2), "%")
print("Lead → Customer:", round(lead_to_customer, 2), "%")

# ==============================
# VISUALIZATIONS (4 IMAGES)
# ==============================

# 1. Funnel Chart
stages = ["Visitors", "Leads", "Customers"]
values = [total_visitors, total_leads, total_customers]

plt.figure()
plt.plot(stages, values, marker='o')
plt.title("Overall Marketing Funnel")
plt.xlabel("Stages")
plt.ylabel("Users")
plt.grid()
plt.savefig("funnel.png")
plt.show()

# 2. Visitor → Lead Conversion
plt.figure()
plt.bar(channel_summary.index, channel_summary["Visitor_to_Lead (%)"])
plt.title("Visitor to Lead Conversion by Channel")
plt.xlabel("Channel")
plt.ylabel("Conversion (%)")
plt.xticks(rotation=45)
plt.savefig("visitor_to_lead.png")
plt.show()

# 3. Lead → Customer Conversion
plt.figure()
plt.bar(channel_summary.index, channel_summary["Lead_to_Customer (%)"])
plt.title("Lead to Customer Conversion by Channel")
plt.xlabel("Channel")
plt.ylabel("Conversion (%)")
plt.xticks(rotation=45)
plt.savefig("lead_to_customer.png")
plt.show()

# 4. Customer Distribution
plt.figure()
plt.pie(
    channel_summary["Customers"],
    labels=channel_summary.index,
    autopct='%1.1f%%'
)
plt.title("Customer Distribution by Channel")
plt.savefig("customer_distribution.png")
plt.show()