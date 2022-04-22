import matplotlib.pyplot as plt


def plot_of_sales(all_data):

    result = all_data.groupby("Month").sum()["Sales"]
    months = range(1, 13)
    names_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                       'Nov', 'Dec']
    plt.xticks(months, names_of_months)
    plt.xlabel("Months")
    plt.ylabel("Sales in USD")
    plt.bar(months, result)
    plt.title("Total sales per month")
    plt.show()
