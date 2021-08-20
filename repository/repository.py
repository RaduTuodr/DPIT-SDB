from exception.exceptions import DuplicateException
from exception.exceptions import NotFoundException


class Repository:
    def __init__(self):
        self.__entities_list = []

    def __find_position(self, entity):
        for i in range(len(self.__entities_list)):
            if entity.get_barcode() == self.__entities_list[i].get_barcode():
                return i
        return None

    def check_product_in_stock(self, entity):
        for i in range(len(self.__entities_list)):
            if __eq__(entity, self.__entities_list[i]):
                return True

        return False

    def find_by_barcode(self, barcode):
        for i in range(len(self.__entities_list)):
            if self.__entities_list[i].get_barcode() == barcode:
                return i

        return None

    @staticmethod
    def find_product_by_barcode(products, barcode):
        for i in range(len(products)):
            if products[i].get_barcode() == barcode:
                return i

        return None

    def add(self, new_entity):
        if self.__find_position(new_entity) is not None:
            raise DuplicateException(new_entity)
        self.__entities_list.append(new_entity)

    def addPromotion(self, new_entity):
        self.__entities_list.append(new_entity)

    def delete(self, entity):
        position = self.__find_position(entity)

        if position is None:
            raise NotFoundException(entity)
        del self.__entities_list[position]

    @staticmethod
    def update(entity, new_attribute, new_attribute_value):
        if new_attribute == "barcode":
            entity.set_barcode(new_attribute_value)

        elif new_attribute == "name":
            entity.set_name(new_attribute_value)

        elif new_attribute == "company":
            entity.set_company(new_attribute_value)

        elif new_attribute == "price":
            entity.set_price(new_attribute_value)

        elif new_attribute == "stock quantity":
            entity.set_stock_quantity(new_attribute_value)

        elif new_attribute == "promotion":
            print("Setting in Repository class new value")
            entity.set_promotion(new_attribute_value)

    def get_all(self):
        return self.__entities_list
