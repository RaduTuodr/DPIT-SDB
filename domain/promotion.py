class Promotion:
    def __init__(self, percentage, barcodes, expire_date):
        self.__percentage = percentage
        self.__barcodes = barcodes
        self.__expire_date = expire_date

    def get_percentage(self):
        return self.__percentage
    def set_percentage(self, new_percentage):
        self.__percentage = new_percentage

    def get_barcodes(self):
        return self.__barcodes
    def set_barcodes(self, new_barcodes):
        self.__barcodes = new_barcodes

    def get_expiry_date(self):
        return self.__expire_date
    def set_expiry_date(self, new_expire_date):
        self.__expire_date = new_expire_date

    def __str__(self):
        return self.get_percentage()