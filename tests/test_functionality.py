import pytest

from functional_page import FunctionalPage

@pytest.mark.parametrize("n, expected",
                         [(1, 1),
                          (4, 3),
                          (6, 8),
                          (10, 55)])
def test_fibonacci(n, expected):
    assert FunctionalPage.fibonacci_func(n) == expected