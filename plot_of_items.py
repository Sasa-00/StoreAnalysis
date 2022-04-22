import matplotlib.pyplot as plt


def plot_of_items(all_data):
    product_group = all_data.groupby("Product")
    quantity_ordered = product_group.sum()["Quantity Ordered"]

    items = [item for item, df in product_group]
    plt.bar(items, quantity_ordered)
    plt.xlabel("Product name")
    plt.xticks(items, rotation="vertical", size=8)
    plt.ylabel("Quantity ordered")
    plt.title("Bestseller products")
    plt.show()
