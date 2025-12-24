import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

tips = sns.load_dataset("tips")

print("First 5 rows:")
print(tips.head())






print("\n--- BASIC INSPECTION ---")

# Shape
print("Shape:", tips.shape)

# Info
print("\nInfo:")
tips.info()

# Describe numeric columns
print("\nDescribe (numeric):")
print(tips.describe())

# Check missing values
print("\nMissing values per column:")
print(tips.isna().sum())




print("\n--- GROUPBY ANALYSIS ---")

# Average total_bill and tip by sex
print("\nAverage total_bill and tip by sex:")
print(tips.groupby("sex")[["total_bill", "tip"]].mean())

# Average total_bill and tip by smoker
print("\nAverage total_bill and tip by smoker:")
print(tips.groupby("smoker")[["total_bill", "tip"]].mean())

# Average total_bill and tip by day
print("\nAverage total_bill and tip by day:")
print(tips.groupby("day")[["total_bill", "tip"]].mean())


print("\n--- PLOTS ---")

# Histogram of total_bill
plt.figure(figsize=(6, 4))
sns.histplot(data=tips, x="total_bill", bins=20, kde=True)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# Boxplot of tip by day
plt.figure(figsize=(6, 4))
sns.boxplot(data=tips, x="day", y="tip")
plt.title("Tip Amount by Day")
plt.xlabel("Day of Week")
plt.ylabel("Tip")
plt.tight_layout()
plt.show()

# Scatter + regression: total_bill vs tip
plt.figure(figsize=(6, 4))
sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.regplot(data=tips, x="total_bill", y="tip", scatter=False, color="red")
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.tight_layout()
plt.show()

print("\n--- TIP PERCENT ---")

tips["tip_percent"] = tips["tip"] / tips["total_bill"] * 100

print(tips[["total_bill", "tip", "tip_percent"]].head())

print("\n--- AVERAGE TIP PERCENT BY SMOKER ---")

avg_tip_percent = tips.groupby("smoker")["tip_percent"].mean().reset_index()
print(avg_tip_percent)

plt.figure(figsize=(6, 4))
sns.barplot(data=avg_tip_percent, x="smoker", y="tip_percent")
plt.title("Average Tip %: Smokers vs Non-Smokers")
plt.xlabel("Smoker")
plt.ylabel("Average Tip Percent")
plt.tight_layout()
plt.show()

print("\n--- AVERAGE TIP % BY TIME (LUNCH VS DINNER) ---")
avg_tip_time = tips.groupby("time")["tip_percent"].mean().reset_index()
print(avg_tip_time)

plt.figure(figsize=(6, 4))
sns.barplot(data=avg_tip_time, x="time", y="tip_percent")
plt.title("Average Tip %: Lunch vs Dinner")
plt.xlabel("Time")
plt.ylabel("Average Tip Percent")
plt.tight_layout()
plt.show()
