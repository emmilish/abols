# main.py
from data_handler import get_sample_data
from statistics import show_horsepower_chart, average_price

def main():
    models = get_sample_data()

    for model in models:
        print(f"Gads: {model.year}, Power-to-Weight: {model.power_to_weight():.2f}")

    print(f"Vidējā cena: €{average_price(models):,.2f}")

    show_horsepower_chart(models)


if __name__ == "__main__":
    main()

