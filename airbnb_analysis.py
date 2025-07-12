# 📦 Import Libraries
import pandas as pd
import numpy as np

# 📥 Load the dataset
df = pd.read_csv("airbnb_listings.csv")

# 👀 Preview the data
print("🔹 First 5 Rows of Data:")
print(df.head())

# 🧹 Step 1: Basic Cleaning
# Drop missing values if any (our mock data doesn't have any)
df.dropna(inplace=True)

# 🧮 Step 2: Summary Statistics
print("\n📊 Summary Statistics:")
print(df.describe())

# 🧠 Step 3: Key Insights

# Average price per night
avg_price = np.mean(df["Price_per_Night"])
print(f"\n💰 Average Price per Night: ${avg_price:.2f}")

# Average review score
avg_score = np.mean(df["Review_Score"])
print(f"🌟 Average Review Score: {avg_score:.2f}")

# Host(s) with highest review score
max_score = df["Review_Score"].max()
top_hosts = df[df["Review_Score"] == max_score][["Host_Name", "Location", "Review_Score"]]
print("\n🏆 Host(s) with Highest Review Score:")
print(top_hosts)

# Listings with price > $100 and availability > 200 days
premium_listings = df[(df["Price_per_Night"] > 100) & (df["Availability_365"] > 200)]
print("\n💼 Premium Listings with High Availability:")
print(premium_listings[["Host_Name", "Location", "Price_per_Night", "Availability_365"]])

# Listings by city (counts)
city_counts = df["Location"].value_counts()
print("\n📍 Listings Count by Location:")
print(city_counts)

# Step 4: Export processed summary (optional)
df.to_csv("processed_airbnb_listings.csv", index=False)
