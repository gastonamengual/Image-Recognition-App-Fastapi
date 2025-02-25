import pytest

from app.validations import validate_filename


def test_incorrect_extension():
    filename = "filename.asd"
    with pytest.raises(ValueError) as ex:
        validate_filename(filename)
        assert ex == "Wrong filename format"


def test_no_filename():
    filename = ""
    with pytest.raises(ValueError) as ex:
        validate_filename(filename)
        assert ex == "Wrong filename format"
