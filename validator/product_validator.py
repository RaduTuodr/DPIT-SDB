from exception.exceptions import ValidationError


class ProductValidator:
    @staticmethod
    def validate_barcode(barcode):
        if len(barcode) <= 10 or len(barcode) == 0:
            pass
        else:
            raise ValidationError("Barcode is longer than 10 characters!")

    @staticmethod
    def validate_price(price):
        try:
            float_price = float(price)
        except TypeError:
            raise ValidationError("Price of product is not a number!")

        if float(price) < 0:
            raise ValidationError("Price of product is not a positive number")

    @staticmethod
    def validate_stock_quantity(stock_quantity):
        if int(stock_quantity) < 0:
            raise ValidationError("Stock quantity is a negative number!")

        try:
            int_stock_quantity = int(stock_quantity)
        except Exception:
            raise ValidationError("Stock quantity is not a number!")
