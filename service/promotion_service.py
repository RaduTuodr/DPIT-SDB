from datetime import datetime

from domain.promotion import Promotion
from repository.repository import Repository
from service.admin_service import AdminService
from ui.secondary_console import SecondaryConsoleUI


class PromotionService:
    def __init__(self, promotion_repository: Repository, admin_service: AdminService):
        self.__promotion_repository = promotion_repository
        self.__admin_service = admin_service

    def add(self, percentage, list_barcodes, date):
        final_list_barcodes = []

        for barcode in list_barcodes:
            check = False

            for product in self.__admin_service.get_all():
                if product.get_barcode() == barcode:
                    check = True

            if check is True:
                final_list_barcodes.append(barcode)

        self.__promotion_repository.addPromotion(Promotion(percentage, final_list_barcodes, date))

    def get_all(self):
        return self.__promotion_repository.get_all()

    @staticmethod
    def calc_price_after_promo(price: str, percentage: str):
        reduced_price = float(price) * (100 - float(percentage)) // 100
        return reduced_price

    @staticmethod
    def sortKey1(entity):
        return entity.get_percentage()

    @staticmethod
    def sortKey2(entity):
        return entity.get_price()

    def print_products_with_promotion(self, products):
        promotions = self.get_all()

        promotions.sort(key=self.sortKey1, reverse=True)

        for promotion in promotions:
            if len(promotion.get_barcodes()) > 0 and promotion.get_expiry_date() >= datetime.now():

                products_from_promotion = []

                for barcode in promotion.get_barcodes():

                    for product in products:
                        if product.get_barcode() == barcode and int(product.get_promotion()) == int(promotion.get_percentage()):
                            products_from_promotion.append(product)

                products_from_promotion.sort(key=self.sortKey2, reverse=True)

                if len(products_from_promotion) != 0:
                    SecondaryConsoleUI.print_promotion(promotion.get_percentage())

                for product in products_from_promotion:
                    SecondaryConsoleUI.print_promotion_product(string=product.__str__(), reduced_price=self.calc_price_after_promo(product.get_price(), promotion.get_percentage()))
