from exception.exceptions import ValidationError


def validate_percentage(percentage):
    if int(percentage) < 0 or int(percentage) >= 100:
        raise ValidationError("Percentage is not between 0 and 100!")
    else:
        pass
