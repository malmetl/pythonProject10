import pytest
from scr.Rectangle import Rectangle


@pytest.fixture
def test_rectangle_integer():
    r = Rectangle(side_a=5, side_b=10)
    assert r.side_a == 5
