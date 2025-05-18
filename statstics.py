# statistics.py
import matplotlib.pyplot as plt

def show_horsepower_chart(models):
    years = [model.year for model in models]
    horsepower = [model.horsepower for model in models]

    plt.plot(years, horsepower, marker='o')
    plt.title('Audi RS4 Zirgspēku attīstība')
    plt.xlabel('Gads')
    plt.ylabel('Zirgspēki')
    plt.grid(True)
    plt.show()


def average_price(models):
    prices = [model.price for model in models]
    return sum(prices) / len(prices)

