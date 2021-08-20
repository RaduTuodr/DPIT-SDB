from domain.product import Product
from exception.exceptions import NotFoundException
from repository.repository import Repository


class AdminService:
    def __init__(self, admin_repository: Repository):
        self.__admin_repository = admin_repository

    def add(self, barcode, name, company, price, stock_quantity):
        self.__admin_repository.add(Product(barcode, name, company, price, stock_quantity))

    def delete(self, barcode):
        products = self.__admin_repository.get_all()

        entity = None

        for i in range(len(products)):
            if products[i].get_barcode() == barcode:
                entity = products[i]

        if entity is None:
            raise NotFoundException()

        self.__admin_repository.delete(entity)

    def update(self, barcode, new_attribute, new_attribute_value):
        print("Updating in Admin Service...")
        products = self.__admin_repository.get_all()

        for i in range(len(products)):
            if products[i].get_barcode() == barcode:
                entity = products[i]

        if new_attribute == "promotion":
            print("updating promotion in Admin service")
        self.__admin_repository.update(entity, new_attribute, new_attribute_value)

    def get_all(self):
        return self.__admin_repository.get_all()

    def get_all_company(self, company):
        products = self.__admin_repository.get_all()

        products_company = []

        for product in products:
            if product.get_company() == company:
                products_company.append(product)

        return products_company
