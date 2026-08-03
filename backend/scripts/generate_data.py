import random
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker
from tqdm import tqdm

fake = Faker()

# ======================================================
# CONFIGURATION
# ======================================================

NUM_SUPPLIERS = 10
NUM_STORES = 20
NUM_PRODUCTS = 100
NUM_DAYS = 365

START_DATE = datetime(2025, 1, 1)

OUTPUT_DIR = Path(__file__).parent

random.seed(42)
np.random.seed(42)

# ======================================================
# MASTER DATA
# ======================================================

CATEGORIES = {
    "Dairy": [
        "Milk",
        "Cheese",
        "Butter",
        "Curd",
        "Yogurt"
    ],
    "Bakery": [
        "Bread",
        "Cake",
        "Bun",
        "Croissant",
        "Muffin"
    ],
    "Beverages": [
        "Coffee",
        "Tea",
        "Juice",
        "Soft Drink",
        "Energy Drink"
    ],
    "Vegetables": [
        "Tomato",
        "Potato",
        "Onion",
        "Carrot",
        "Cucumber"
    ],
    "Fruits": [
        "Apple",
        "Banana",
        "Orange",
        "Mango",
        "Grapes"
    ],
    "Meat": [
        "Chicken",
        "Fish",
        "Mutton",
        "Sausage",
        "Turkey"
    ],
    "Frozen": [
        "Frozen Pizza",
        "Frozen Peas",
        "Frozen Corn",
        "Ice Cream",
        "Frozen Fries"
    ],
    "Snacks": [
        "Chips",
        "Biscuits",
        "Chocolate",
        "Popcorn",
        "Cookies"
    ],
    "Household": [
        "Soap",
        "Shampoo",
        "Toothpaste",
        "Detergent",
        "Cleaner"
    ],
    "Grocery": [
        "Rice",
        "Sugar",
        "Salt",
        "Flour",
        "Oil"
    ]
}

SUPPLIER_NAMES = [
    "FreshFoods",
    "DailyFarm",
    "GreenHarvest",
    "RetailSource",
    "PrimeFoods",
    "NatureBest",
    "MetroSupply",
    "FoodHub",
    "FarmDirect",
    "SmartWholesale"
]

STORE_TYPES = [
    "Hypermarket",
    "Supermarket",
    "Express"
]

CITIES = [
    "Bangalore",
    "Mysore",
    "Mangalore",
    "Hubli",
    "Belgaum",
    "Kochi",
    "Chennai",
    "Hyderabad",
    "Mumbai",
    "Pune"
]


# ======================================================
# HOLIDAYS
# ======================================================

HOLIDAYS = [
    ("2025-01-01", "New Year"),
    ("2025-01-14", "Pongal"),
    ("2025-03-14", "Holi"),
    ("2025-04-18", "Good Friday"),
    ("2025-08-15", "Independence Day"),
    ("2025-08-27", "Ganesh Chaturthi"),
    ("2025-10-02", "Gandhi Jayanti"),
    ("2025-10-20", "Diwali"),
    ("2025-12-25", "Christmas")
]

# 1) Generate Holidays DataFrame

holiday_df = pd.DataFrame(
    HOLIDAYS,
    columns=[
        "date",
        "holiday_name"
    ]
)


# 2) Generate Suppliers
suppliers = []

for i in range(NUM_SUPPLIERS):

    suppliers.append({

        "supplier_id": i + 1,

        "supplier_name": SUPPLIER_NAMES[i],

        "city": random.choice(CITIES),

        "country": "India",

        "lead_time_days": random.randint(2,10)

    })

supplier_df = pd.DataFrame(suppliers)

# 3) Generate Stores
stores = []

for i in range(NUM_STORES):

    stores.append({

        "store_id": i + 1,

        "store_name": f"Store_{i+1}",

        "city": random.choice(CITIES),

        "state": "Karnataka",

        "store_type": random.choice(STORE_TYPES),

        "opening_date": fake.date_between(
            "-10y",
            "-1y"
        ),

        "is_active": True

    })

store_df = pd.DataFrame(stores)

# 4) Generate Products

products = []

product_id = 1

for category, names in CATEGORIES.items():

    while len(
        [p for p in products if p["category"] == category]
    ) < 10:

        name = random.choice(names)

        products.append({

            "product_id": product_id,

            "product_name": f"{name} {product_id}",

            "category": category,

            "price": round(
                random.uniform(20,500),
                2
            ),

            "shelf_life_days": random.randint(
                3,
                365
            ),

            "supplier_id": random.randint(
                1,
                NUM_SUPPLIERS
            ),

            "is_active": True

        })

        product_id += 1

product_df = pd.DataFrame(products)



# 5) Save Master Datasets to CSV    
supplier_df.to_csv(
    OUTPUT_DIR / "suppliers.csv",
    index=False
)

store_df.to_csv(
    OUTPUT_DIR / "stores.csv",
    index=False
)

product_df.to_csv(
    OUTPUT_DIR / "products.csv",
    index=False
)

holiday_df.to_csv(
    OUTPUT_DIR / "holidays.csv",
    index=False
)

print("Master datasets generated successfully.")




# ======================================================
# SALES GENERATOR
# ======================================================

print("\nGenerating Sales Data...\n")

sales = []

for day in tqdm(range(NUM_DAYS)):

    current_date = START_DATE + timedelta(days=day)

    weekday = current_date.weekday()

    holiday = holiday_df[
        holiday_df["date"] == current_date.strftime("%Y-%m-%d")
    ]

    is_holiday = len(holiday) > 0

    for _, store in store_df.iterrows():

        for _, product in product_df.iterrows():

            base_demand = random.randint(8, 40)

            category = product["category"]

            multiplier = 1.0

            # Weekend boost

            if weekday >= 5:
                if category in [
                    "Dairy",
                    "Bakery",
                    "Snacks",
                    "Beverages"
                ]:
                    multiplier *= 1.25

            # Holiday boost

            if is_holiday:
                if category in [
                    "Snacks",
                    "Beverages",
                    "Frozen"
                ]:
                    multiplier *= 1.35

            # Summer effect

            if current_date.month in [4, 5]:

                if category == "Beverages":
                    multiplier *= 1.40

                if category == "Frozen":
                    multiplier *= 1.50

            # Winter effect

            if current_date.month in [11, 12]:

                if category == "Dairy":
                    multiplier *= 1.15

            quantity = max(
                1,
                int(base_demand * multiplier + np.random.normal(0, 3))
            )

            discount = random.choice(
                [
                    0,
                    0,
                    0,
                    5,
                    10,
                    15,
                    20
                ]
            )

            revenue = (
                quantity *
                product["price"] *
                (1 - discount / 100)
            )

            sales.append({

                "sale_date": current_date,

                "store_id": store["store_id"],

                "product_id": product["product_id"],

                "quantity_sold": quantity,

                "discount_percentage": discount,

                "revenue": round(revenue, 2)

            })

sales_df = pd.DataFrame(sales)

print("\nSales Generation Complete.")

sales_df.to_csv(
    OUTPUT_DIR / "sales.csv",
    index=False
)

print("sales.csv saved.")
print("\n==============================")
print("Dataset Generation Completed")
print("==============================")

print(f"Suppliers : {len(supplier_df)}")
print(f"Stores    : {len(store_df)}")
print(f"Products  : {len(product_df)}")
print(f"Sales     : {len(sales_df)}")


# ======================================================
# INVENTORY GENERATOR
# ======================================================

print("\nGenerating Inventory...\n")

inventory = []

inventory_id = 1

latest_sales = (
    sales_df
    .sort_values("sale_date")
    .groupby(["store_id", "product_id"])
    .tail(30)
)

avg_sales = (
    latest_sales
    .groupby(["store_id", "product_id"])["quantity_sold"]
    .mean()
    .reset_index()
)

for _, row in tqdm(avg_sales.iterrows(), total=len(avg_sales)):

    avg_daily = row["quantity_sold"]

    minimum_stock = max(
        10,
        int(avg_daily * 3)
    )

    maximum_stock = max(
        minimum_stock + 20,
        int(avg_daily * 10)
    )

    current_stock = random.randint(
        minimum_stock,
        maximum_stock
    )

    inventory.append({

        "inventory_id": inventory_id,

        "store_id": row["store_id"],

        "product_id": row["product_id"],

        "current_stock": current_stock,

        "minimum_stock": minimum_stock,

        "maximum_stock": maximum_stock,

        "last_updated": START_DATE + timedelta(days=NUM_DAYS)

    })

    inventory_id += 1

inventory_df = pd.DataFrame(inventory)

inventory_df.to_csv(
    OUTPUT_DIR / "inventory.csv",
    index=False
)

print("inventory.csv saved.")