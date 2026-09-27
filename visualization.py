import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_scraped.csv")

# Price distribution
plt.figure(figsize=(10, 6))

plt.hist(
    df["price_gbp"],
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "charts/price_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()