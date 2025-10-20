import pytest
from heroes import find_tallest_hero


def test_male_with_occupation():
    expected_name = "Galactus"
    assert find_tallest_hero("Male", True) == expected_name


def test_male_no_occupation():
    expected_name = "Fin Fang Foom"
    assert find_tallest_hero("Male", False) == expected_name


def test_female_with_occupation():
    expected_name = "Wolfsbane"
    assert find_tallest_hero("Female", True) == expected_name


def test_female_no_occupation():
    expected_name = "Ardina"
    assert find_tallest_hero("Female", False) == expected_name


def test_other_gender_with_occupation():
    expected_name = "Living Brain"
    assert find_tallest_hero("-", True) == expected_name


def test_no_results_invalid_gender():
    assert find_tallest_hero("Kryptonian", True) is None


def test_no_results_valid_filters():
    assert find_tallest_hero("Genderless", False) is None
