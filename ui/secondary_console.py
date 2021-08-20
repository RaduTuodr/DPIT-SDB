class SecondaryConsoleUI:
    def __init__(self):
        pass

    @classmethod
    def print_promotion(cls, percentage):
        print("Products with {0}% promotion: ".format(percentage))

    @classmethod
    def print_promotion_product(cls, string, reduced_price):
        print('{0}, Price reduced to: {1}'.format(string, reduced_price))
