import pytest
from pytest import approx
from mortgage_calculator import calculate_monthly_repayment, calculate_total_payment

def test_calculate_monthly_repayment():
    assert calculate_monthly_repayment(100_000, 5, 30) == approx(536.82, abs=0.1)
    assert calculate_monthly_repayment(200_000, 3.5, 15) == approx(1429.77, abs=0.1)
    assert calculate_monthly_repayment(50_000, 6, 10) == approx(555.10, abs=0.1)

def test_calculate_total_payment():
    assert calculate_total_payment(536.82, 30) == approx(193255.20, abs=0.5)
    assert calculate_total_payment(1429.77, 15) == approx(257358.60, abs=0.5)
    assert calculate_total_payment(555.10, 10) == approx(66612.00, abs=0.5)

pytest.main([__file__, "-v", "--tb=line"])