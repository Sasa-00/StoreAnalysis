import pandas as pd
import merging_files
import plot_of_sales
import plot_of_cities
import plot_of_items

# Calling function to merge separate CSV files in one
# merging_files.merge_csv()

all_data = pd.read_csv("./SalesAnalysis/Output/Sales_2019.csv")

# Clearing all NaN values in list
all_data = all_data.dropna(how="all")

# There was some "Or" in table and i cleared it up
all_data = all_data[all_data["Order Date"].str[:2] != "Or"]

# Making "Month" column and converting it to int
all_data["Month"] = all_data["Order Date"].str[:2]
all_data["Month"] = all_data["Month"].astype("int32")

# Converting "Price Each" and "Quantity Ordered" to numeric type
all_data["Price Each"] = pd.to_numeric(all_data["Price Each"])
all_data["Quantity Ordered"] = pd.to_numeric(all_data["Quantity Ordered"])

# Making "Sales" column to have an insight into a total earnings per item
all_data["Sales"] = all_data["Price Each"] * all_data["Quantity Ordered"]


# Making a plot of total sales per month
plot_of_sales.plot_of_sales(all_data)

# Making "City" column
all_data["City"] = all_data["Purchase Address"].apply(lambda x: x.split(",")[1] + " " + "(" + x.split(",")[2][1:3] + ")")

# Making a plot of total sales per city
plot_of_cities.plot_of_cities(all_data)

# Making a plot of bestseller products
plot_of_items.plot_of_items(all_data)
