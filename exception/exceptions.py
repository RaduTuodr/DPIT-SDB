class ProgramError(Exception):
    pass


class ValidationError(ProgramError):
    pass


class DuplicateException(ProgramError):
    pass


class NotFoundException(ProgramError):
    pass


class NoProductsList(ProgramError):
    pass


class NoPromotionsList(ProgramError):
    pass


class NotEnoughItemsInStock(ProgramError):
    pass


class ValueErrorMessage(ProgramError):
    pass
