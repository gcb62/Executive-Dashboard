# exec-dash-test.py

from monthly_sales import to_usd
from monthly_sales import month_lookup

def test_usd():
    result1 = to_usd(3.5111111)
    result2 = to_usd(10)
    assert result1 == "$3.51"
    assert result2 == "$10.00"

def test_month_lookup():
    month1 = month_lookup('01')
    month2 = month_lookup('12')
    month3 = month_lookup('06')
    assert month1 == "January"
    assert month2 == "December"
    assert month3 == "June"
