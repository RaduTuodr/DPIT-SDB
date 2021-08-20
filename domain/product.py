class Product:
    def __init__(self, barcode, name, company, price, stock_quantity, promotion=0):
        """
        Constructor of class Product
        :param barcode: string (max 10 characters)
        :param name: string
        :param company: string
        :param price: positive integer
        :param stock_quantity: positive integer
        """
        self.__barcode = barcode
        self.__name = name
        self.__company = company
        self.__price = price
        self.__stock_quantity = stock_quantity
        self.__promotion = promotion

    def get_barcode(self):
        return self.__barcode
    def set_barcode(self, new_barcode):
        self.__barcode = new_barcode

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    def get_company(self):
        return self.__company
    def set_company(self, new_company):
        self.__company = new_company

    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price

    def get_stock_quantity(self):
        return self.__stock_quantity
    def set_stock_quantity(self, new_stock_quantity):
        self.__stock_quantity = new_stock_quantity

    def get_promotion(self):
        return self.__promotion
    def set_promotion(self, new_promotion):
        self.__promotion = new_promotion

    def __eq__(self, other):
        return self.get_name() == other.get_name() and self.get_company() == other.get_company()

    def __str__(self):
        return "Name: {0}, Company: {1}, Price: {2}, Available: {3}".format(self.get_name(), self.get_company(), self.get_price(), self.get_stock_quantity())
