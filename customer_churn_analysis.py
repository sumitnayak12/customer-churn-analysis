# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:42:49 2026

@author: user
"""

import pandas as pd

df = pd.read_csv("C:/Users/user/Documents/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate Customer IDs:")
print(df["customerID"].duplicated().sum())

print("\nTotalCharges data type:")
print(df["TotalCharges"].dtype)

print("\nBlank TotalCharges:")
print((df["TotalCharges"].str.strip() == "").sum())

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df["TotalCharges"].dtype)
print(df["TotalCharges"].isnull().sum())

print(df[df["TotalCharges"].isnull()][
    ["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]
])

df.loc[df["TotalCharges"].isnull(), "TotalCharges"] = 0
print(df["TotalCharges"].isnull().sum())

print(df[df["tenure"] == 0][
    ["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]
])

print("\nGender:")
print(df["gender"].value_counts())

print("\nContract:")
print(df["Contract"].value_counts())

print("\nInternet Service:")
print(df["InternetService"].value_counts())

print("\nPayment Method:")
print(df["PaymentMethod"].value_counts())

print("\nChurn:")
print(df["Churn"].value_counts())

total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
churn_rate = (churned_customers / total_customers) * 100

print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print(contract_churn.round(2))

import matplotlib.pyplot as plt

contract_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("Minimum tenure:", df["tenure"].min())
print("Maximum tenure:", df["tenure"].max())
print("Average tenure:", round(df["tenure"].mean(), 2))

bins = [0, 12, 24, 48, 72]
labels = ["0-12 months", "13-24 months", "25-48 months", "49-72 months"]

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=bins,
    labels=labels,
    include_lowest=True
)
tenure_churn = pd.crosstab(
    df["TenureGroup"],
    df["Churn"],
    normalize="index"
) * 100

print(tenure_churn.round(2))

tenure_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Customer Tenure")
plt.xlabel("Customer Tenure")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

monthly_charges_churn = df.groupby("Churn")["MonthlyCharges"].mean()

print(monthly_charges_churn.round(2))

monthly_charges_churn.plot(kind="bar")

plt.title("Average Monthly Charges by Churn Status")
plt.xlabel("Churn Status")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100

print(internet_churn.round(2))

internet_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100

print(payment_churn.round(2))

payment_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

segment_churn = pd.crosstab(
    [df["Contract"], df["InternetService"]],
    df["Churn"],
    normalize="index"
) * 100

print(segment_churn.round(2))

df.to_csv(
    "C:/Users/user/Documents/telco_churn_clean.csv",
    index=False
)

print("Cleaned dataset saved successfully.")

import matplotlib.pyplot as plt

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

contract_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()