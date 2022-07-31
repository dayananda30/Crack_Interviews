class NameTooShortError(ValueError):
    pass


def validate_name(name):
    if len(name) < 10:
        # raise ValueError
        # raise ValueError("Name is too Short")
        # we can also create our custom Exception
        raise NameTooShortError(name)


if __name__ == "__main__":
    validate_name("Daya")
