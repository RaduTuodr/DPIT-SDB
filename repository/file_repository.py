from domain.product import Product
from exception.exceptions import ValidationError
from repository.repository import Repository
from validator.product_validator import ProductValidator


class FileRepository:
    def __init__(self, product_validator: ProductValidator, product_repository: Repository):
        self.__products_list = []
        self.__product_validator = product_validator
        self.__product_repository = product_repository

    def get_products_list(self):
        return self.__products_list

    def set_products_in_repository(self):
        self.__product_repository.get_all().clear()

        for product in self.__products_list:
            self.__product_repository.add(product)

    def read_products(self):
        self.__product_repository.get_all().clear()

        with open('repository\\products.txt', 'r') as file:
            lines = file.read().splitlines()

            for line in lines:
                product_info = line.split(', ')

                if len(product_info) < 5 or len(product_info) > 6:  # 5 sau 6 parametrii( depinde de promotie)
                    print(len(product_info))
                    raise ValidationError()
                else:
                    self.__product_validator.validate_barcode(product_info[0])
                    self.__product_validator.validate_price(product_info[3])
                    self.__product_validator.validate_stock_quantity(product_info[4])

                try:
                    self.__product_repository.get_all().append(Product(barcode=product_info[0], name=product_info[1], company=product_info[2],price=product_info[3], stock_quantity=product_info[4], promotion=product_info[5]))
                except:
                    self.__product_repository.get_all().append(Product(barcode=product_info[0], name=product_info[1], company=product_info[2], price=product_info[3], stock_quantity=product_info[4]))

    @staticmethod
    def write_products(products):
        with open('repository\\products.txt', 'w') as file:

            for product in products:
                file.write('{0}, {1}, {2}, {3}, {4}, {5}\n'.format(product.get_barcode(), product.get_name(), product.get_company(), product.get_price(), product.get_stock_quantity(), product.get_promotion()))
