import pandas as pd
from scipy import stats


# --------------------------------
# 1. Load Dataset
# --------------------------------

df = pd.read_csv("books_scraped.csv")


# --------------------------------
# 2. Basic Dataset Information
# --------------------------------

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# --------------------------------
# 3. Data Quality Checks
# --------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# --------------------------------
# 4. Statistical Summary
# --------------------------------

print("\nStatistical Summary:")
print(df.describe())


# --------------------------------
# 5. Price Analysis
# --------------------------------

print("\nPrice Analysis")

print(
    "Average Price:",
    round(df["price_gbp"].mean(), 2)
)

print(
    "Median Price:",
    round(df["price_gbp"].median(), 2)
)

print(
    "Minimum Price:",
    round(df["price_gbp"].min(), 2)
)

print(
    "Maximum Price:",
    round(df["price_gbp"].max(), 2)
)


# --------------------------------
# 6. Cheapest Book
# --------------------------------

cheapest = df.loc[
    df["price_gbp"].idxmin()
]

print("\nCheapest Book:")
print(cheapest["title"])
print("Price:", cheapest["price_gbp"])


# --------------------------------
# 7. Most Expensive Book
# --------------------------------

expensive = df.loc[
    df["price_gbp"].idxmax()
]

print("\nMost Expensive Book:")
print(expensive["title"])
print("Price:", expensive["price_gbp"])


# --------------------------------
# 8. Rating Analysis
# --------------------------------

print("\nRating Distribution:")

print(
    df["rating"]
    .value_counts()
    .sort_index()
)


# --------------------------------
# 9. Five-Star Books
# --------------------------------

five_star_books = df[
    df["rating"] == 5
]

print("\nNumber of 5-Star Books:")
print(len(five_star_books))

print("\nSome 5-Star Books:")

print(
    five_star_books[
        ["title", "price_gbp"]
    ].head(10)
)


# --------------------------------
# 10. Outlier Detection
# --------------------------------

Q1 = df["price_gbp"].quantile(0.25)

Q3 = df["price_gbp"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["price_gbp"] < lower_limit) |
    (df["price_gbp"] > upper_limit)
]

print("\nOutlier Analysis")

print(
    "Q1:",
    round(Q1, 2)
)

print(
    "Q3:",
    round(Q3, 2)
)

print(
    "IQR:",
    round(IQR, 2)
)

print(
    "Lower Limit:",
    round(lower_limit, 2)
)

print(
    "Upper Limit:",
    round(upper_limit, 2)
)

print(
    "Number of Potential Outliers:",
    len(outliers)
)


# --------------------------------
# 11. Hypothesis Testing
# --------------------------------

t_statistic, p_value = stats.ttest_1samp(
    df["price_gbp"],
    30
)

print("\nHypothesis Test")

print(
    "T-statistic:",
    round(t_statistic, 4)
)

print(
    "P-value:",
    round(p_value, 4)
)

if p_value < 0.05:

    print(
        "Result: There is statistical evidence "
        "that the average price differs from £30."
    )

else:

    print(
        "Result: There is not enough statistical "
        "evidence to say that the average price differs from £30."
    )


# --------------------------------
# END
# --------------------------------

print("\nEDA COMPLETED SUCCESSFULLY!")