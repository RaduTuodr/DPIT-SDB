from repository.repository import Repository
from validator.product_validator import ProductValidator

from exception.exceptions import NotEnoughItemsInStock


class ClientService:
    def __init__(self, client_repository: Repository):
        self.__client_repository = client_repository

    @staticmethod
    def buy(products, name, company, quantity):

        try:
            ProductValidator.validate_price(quantity)
        except ValueError:
            return None

        for product in products:
            if product.get_name() == name and product.get_company() == company:
                if int(product.get_stock_quantity()) >= int(quantity):
                    product.set_stock_quantity(int(product.get_stock_quantity()) - int(quantity))
                    return True
                else:
                    raise NotEnoughItemsInStock()

        return False

    @staticmethod
    def get_products_under_price(products, price):
        products_affordable = []

        for product in products:
            if float(product.get_price()) < float(price):
                products_affordable.append(product)

        for i in range(len(products_affordable)):
            for j in range(i + 1, len(products_affordable)):
                if float(products_affordable[i].get_price()) < float(products_affordable[j].get_price()):
                    aux_product = products_affordable[i]
                    products_affordable[i] = products_affordable[j]
                    products_affordable[j] = aux_product

        return products_affordable
