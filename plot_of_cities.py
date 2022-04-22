import matplotlib.pyplot as plt


def plot_of_cities(all_data):

    result = all_data.groupby("City").sum()["Sales"]
    cities = [city for city, df in all_data.groupby("City")]
    plt.bar(cities, result)
    plt.xlabel("City name")
    plt.xticks(cities, rotation="vertical", size=8)
    plt.ylabel("Sales in USD")
    plt.title("Total sales per city")
    plt.show()
