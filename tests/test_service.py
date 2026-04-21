import pytest

from calc_service import add, divide, healthcheck


def test_add() -> None:
    assert add(2, 3) == 5


def test_divide() -> None:
    assert divide(8, 2) == 4


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(10, 0)


def test_healthcheck() -> None:
    assert healthcheck()["status"] == "ok"
