from exception.exceptions import ValidationError, NotFoundException, NotEnoughItemsInStock, DuplicateException
from repository.file_repository import FileRepository
from repository.repository import Repository
from service.admin_service import AdminService
from service.client_service import ClientService
from service.promotion_service import PromotionService
from validator.product_validator import ProductValidator
from validator.promotion_validator import validate_percentage

from datetime import datetime


class ConsoleUI:
    def __init__(self, admin_service: AdminService, client_service: ClientService, promotion_service: PromotionService,
                 repository: Repository, file_repository: FileRepository):
        self.__admin_service = admin_service
        self.__client_service = client_service
        self.__promotion_service = promotion_service
        self.__repository = repository
        self.__file_repository = file_repository

    @staticmethod
    def print_role_menu():
        print("1. Admin menu")
        print("2. Client menu")
        print("0. Exit")

    @staticmethod
    def print_admin_menu():
        print("1. Add a product to the list")
        print("2. Delete a product from the list")
        print("3. Modify a product's data")
        print("4. Show all products")
        print("5. Show all of a company's products")
        print("6. Add a promotion to a list of products")
        print("0. Back")

    @staticmethod
    def print_client_menu():
        print("1. Buy a product")
        print("2. Show all products")
        print("3. Show all products that cost less than a specific price")
        print("4. Show all products that have a promotion")
        print("0. Back")

    def __add_product(self):
        barcode = input("Input the barcode of the product\n").strip()

        try:
            ProductValidator.validate_barcode(barcode)
        except ValidationError:
            print("Invalid barcode")
            return

        name = input("Input the name of the product\n").strip()
        company = input("Input the company of the product\n").strip()

        price = input("Input the price of the product\n").strip()

        try:
            ProductValidator.validate_price(price)
        except ValidationError:
            print("Invalid price")
            return

        stock_quantity = input("Input the stock quantity of the product\n").strip()

        try:
            ProductValidator.validate_stock_quantity(stock_quantity)
        except ValidationError:
            print("Invalid stock quantity")
            return

        try:
            self.__admin_service.add(barcode, name, company, price, stock_quantity)
        except DuplicateException:
            print("The product has an already existing barcode!")

    def __delete_product(self):
        barcode = input("Input the barcode of the product\n").strip()

        try:
            ProductValidator.validate_barcode(barcode)
        except ValidationError:
            print("Invalid barcode")

        try:
            self.__admin_service.delete(barcode)
        except NotFoundException:
            print("Product not found")

    def __update_product(self):
        barcode = input("Input the barcode of the product\n").strip()

        try:
            ProductValidator.validate_barcode(barcode)
        except ValidationError:
            print("Invalid Input")
            return

        new_attribute = input("Input the attribute of the product that you want to update\n").strip()
        new_attribute_value = input("Input the new value of the attribute\n").strip()

        try:
            if new_attribute == "barcode":
                ProductValidator.validate_barcode(new_attribute_value)
            elif new_attribute == "price":
                ProductValidator.validate_price(new_attribute_value)
            elif new_attribute == "stock quantity":
                ProductValidator.validate_stock_quantity(new_attribute_value)
        except ValidationError:
            print("Invalid Input")

    def __print_all_products(self):
        products = self.__admin_service.get_all()

        if len(products) == 0:
            print("No items to show!")
        for product in products:
            print('{0}, Barcode: {1}'.format(product.__str__(), product.get_barcode()))

    def __print_all_products_client(self):
        products = self.__admin_service.get_all()

        for product in products:
            print(product.__str__())

    def __print_all_products_company(self):
        company = input("Input the name of the company:\n").strip()
        product_from_company = self.__admin_service.get_all_company(company)

        if len(product_from_company) == 0:
            print("There are no products from this company!")

        for product in product_from_company:
            print(product.__str__())

    def __buy_product(self):
        name = input("Input the name of the product:\n").strip()
        company = input("Input the company that creates that product:\n").strip()
        quantity = input("Input how many you want:\n").strip()

        try:
            ProductValidator.validate_stock_quantity(quantity)
        except ValidationError:
            print("Invalid quantity!")
            return

        try:
            if self.__client_service.buy(self.__admin_service.get_all(), name, company, quantity):
                print("Purchase was successful!")
            else:
                print("Product not found!")
        except NotFoundException:
            print("The product is not from the list!")
        except NotEnoughItemsInStock:
            print("There are not enough items in stock for your purchase!")

    def __print_products_under_price(self):
        products = self.__admin_service.get_all()
        price = input("Input the price\n").strip()
        products_under_price = self.__client_service.get_products_under_price(products, price)

        if len(products_under_price) == 0:
            print("There are no items under that price!")

        for product in products_under_price:
            print(product.__str__())

    def __add_promotion(self):
        percentage = input("Input the percentage:\n").strip()

        try:
            percentage = int(percentage)
            validate_percentage(percentage)
        except ValidationError:
            print("Percentage is not between 0 and 100!")
            return

        list_barcodes = []
        print("Input the barcodes of the products. Press '0' when done:")

        while True:
            barcode = input().strip()

            if barcode == '0':
                break

            try:
                ProductValidator.validate_barcode(barcode)
            except ValidationError:
                print("Invalid barcode")

            try:
                self.__admin_service.update(barcode, "promotion", percentage)
                list_barcodes.append(barcode)
            except TypeError and UnboundLocalError:
                print("Barcode does not exist!")
        try:
            print("Input the date until which the promotion should be active: ")

            year = int(input("Year: ").strip())
            month = int(input("Month: ").strip())
            day = int(input("Day: ").strip())

            date = datetime(year, month, day)
        except TypeError:
            print("Invalid date!")

        self.__promotion_service.add(percentage, list_barcodes, date)

    def __print_products_with_promotion(self):
        self.__promotion_service.print_products_with_promotion(self.__admin_service.get_all())

    def run(self):
        while True:
            self.print_role_menu()

            try:
                role = int(input().strip())

                if role == 0:
                    break
                elif role == 1:
                    while True:
                        self.print_admin_menu()

                        try:
                            self.__file_repository.read_products()
                        except ValidationError:
                            print("Invalid products in file!")

                        try:
                            task = int(input().strip())

                            if task == 1:
                                self.__add_product()
                            elif task == 2:
                                self.__delete_product()
                            elif task == 3:
                                self.__update_product()
                            elif task == 4:
                                self.__print_all_products()
                            elif task == 5:
                                self.__print_all_products_company()
                            elif task == 6:
                                self.__add_promotion()
                            elif task == 0:
                                break
                            else:
                                print("Input not from the listed responses")
                        except ValueError:
                            print("Invalid input!")

                        self.__file_repository.write_products(self.__admin_service.get_all())

                elif role == 2:
                    while True:
                        self.print_client_menu()

                        try:
                            self.__file_repository.read_products()
                        except ValidationError:
                            print("Invalid products in file!")

                        try:
                            task = int(input().strip())

                            if task == 1:
                                self.__buy_product()
                            elif task == 2:
                                self.__print_all_products_client()
                            elif task == 3:
                                self.__print_products_under_price()
                            elif task == 4:
                                self.__print_products_with_promotion()

                            elif task == 0:
                                break
                            else:
                                print("Input not from the listed responses")
                        except ValueError:
                            print("Invalid input!")

                        self.__file_repository.write_products(self.__admin_service.get_all())
                else:
                    print("Input not from the listed responses")
            except ValueError:
                print("Invalid input!")
