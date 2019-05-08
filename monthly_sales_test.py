# shopping_cart_test.py

from shopping_cart import to_usd
from shopping_cart import now



def test_usd():
    result1 = to_usd(3.5111111)
    result2 = to_usd(10)
    assert result1 == "$3.51"
    assert result2 == "$10.00"

def human_friendly_time():
    time1 = now(18.52)
    time2 = now(6.43)
    assert time1 == "18:52"
    assert time2 == "6:43"
