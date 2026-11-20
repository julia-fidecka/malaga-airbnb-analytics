import pandas as pd
import sqlite3

DB_PATH = "data/malaga_airbnb.db"
LISTINGS_PATH = "data/raw/listings.csv"
CALENDAR_PATH = "data/raw/calendar.csv"
conn = sqlite3.connect(DB_PATH)

LISTINGS_COLS = [
    "id",
    "name",
    "neighbourhood_cleansed",
    "property_type",
    "room_type",
    "review_scores_rating",
    "price",
    "accommodates",
    "bedrooms",
    "beds",
    "minimum_nights",
    "number_of_reviews",
    "host_id",
    "host_is_superhost",
]

CALENDAR_COLS = ["listing_id", "date", "available", "minimum_nights"]

df_listings = pd.read_csv(LISTINGS_PATH, usecols=LISTINGS_COLS)

df_listings["price"] = pd.to_numeric(
    df_listings["price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False),
    errors="coerce",
)

df_listings["host_is_superhost"] = df_listings["host_is_superhost"].map(
    {"t": True, "f": False}
)

df_listings.to_sql("listings", conn, if_exists="replace", index=False)
print(f"Listings table created with {len(df_listings)} records.")

df_calendar = pd.read_csv(CALENDAR_PATH, usecols=CALENDAR_COLS)

df_calendar["available"] = df_calendar["available"].map({"t": True, "f": False})
df_calendar.to_sql("calendar", conn, if_exists="replace", index=False)
print(f"Calendar table created with {len(df_calendar)} records.")

conn.close()
