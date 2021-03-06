import datetime
import unittest


DISCOUNT_FOR_SENIORS = 5
DISCOUNT_FOR_NEW_CLIENTS = 15
DISCOUNT_FOR_VETERANS = 10
DEFAULT_DISCOUNT = 0
YEAR = datetime.timedelta(days=365)
SENIOR_AGE = 65 * YEAR



class Customer:
    def __init__(self, first_purchase_date, birth_date, is_veteran):
        assert isinstance(first_purchase_date, (type(None), datetime.datetime))
        assert isinstance(birth_date, datetime.datetime)
        assert isinstance(is_veteran, bool)

        self.first_purchase_date = first_purchase_date
        self.birth_date = birth_date
        self.is_veteran = is_veteran


class Discount:
    def compute_discount(self, customer):
        raise NotImplementedError


class BinaryDiscount(Discount):
    discount = NotImplementedError

    def is_eligible(self, customer):
        raise NotImplementedError

    def compute_discount(self, customer):
        if self.is_eligible(customer):
            return self.discount
        else:
            return DEFAULT_DISCOUNT


class SeniorDiscount(BinaryDiscount):
    discount = DISCOUNT_FOR_SENIORS

    def is_eligible(self, customer):
        now = datetime.datetime.now()    
        return customer.birth_date <= now - SENIOR_AGE


class FirstPurchaseDiscount(BinaryDiscount):
    discount = DISCOUNT_FOR_NEW_CLIENTS

    def is_eligible(self, customer):
        return customer.first_purchase_date is None


class LoyalCustomerDiscount(BinaryDiscount):
    def __init__(self, years, discount):
        self.years = years
        self.discount = discount

    def is_eligible(self, customer):
        now = datetime.datetime.now()
        return (customer.first_purchase_date is not None and
                customer.first_purchase_date <= now - self.years * YEAR)


class VeteranDiscount(BinaryDiscount):
    discount = DISCOUNT_FOR_VETERANS

    def is_eligible(self, customer):
        return customer.is_veteran


class MaxDiscount(Discount):
    def __init__(self, rules):
        self.rules = rules

    def compute_discount(self, customer):
        discounts = (rule.compute_discount(customer) 
                     for rule in self.rules)
        return max(discounts, default=DEFAULT_DISCOUNT)


DEFAULT_DISCOUNT_RULES = [
    SeniorDiscount(),
    FirstPurchaseDiscount(),
    LoyalCustomerDiscount(years=1, discount=10),
    LoyalCustomerDiscount(years=5, discount=12),
    LoyalCustomerDiscount(years=10, discount=20),
    VeteranDiscount(),
]


calculator = MaxDiscount(DEFAULT_DISCOUNT_RULES)
calculate_discount_percentage = calculator.compute_discount


class CalculateDiscountPercentageTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime.datetime.now()
        self.year = datetime.timedelta(days=365)

    def test_should_return_zero_for_casual_customer(self):
        customer = Customer(first_purchase_date=self.now,
                            birth_date=self.now-20*self.year,
                            is_veteran=False)
        got = calculate_discount_percentage(customer)
        expected = 0
        self.assertEqual(got, expected)

    def test_should_return_15_for_new_client(self):
        customer = Customer(first_purchase_date=None,
                            birth_date=self.now-20*self.year,
                            is_veteran=False)
        got = calculate_discount_percentage(customer)
        expected = 15
        self.assertEqual(got, expected)

    def test_should_return_10_for_veteran(self):
        customer = Customer(first_purchase_date=self.now,
                            birth_date=self.now-20*self.year,
                            is_veteran=True)
        got = calculate_discount_percentage(customer)
        expected = 10
        self.assertEqual(got, expected)

    def test_should_return_5_for_a_senior(self):
        customer = Customer(first_purchase_date=self.now,
                            birth_date=self.now-65*self.year,
                            is_veteran=False)
        got = calculate_discount_percentage(customer)
        expected = 5
        self.assertEqual(got, expected)

    def test_should_return_10_for_a_loyal_customer(self):
        customer = Customer(first_purchase_date=self.now-1*self.year,
                            birth_date=self.now-20*self.year,
                            is_veteran=False)
        got = calculate_discount_percentage(customer)
        expected = 10
        self.assertEqual(got, expected)

    def test_should_return_12_for_a_more_loyal_customer(self):
        customer = Customer(first_purchase_date=self.now-5*self.year,
                            birth_date=self.now-20*self.year,
                            is_veteran=False)
        got = calculate_discount_percentage(customer)
        expected = 12
        self.assertEqual(got, expected)

    def test_should_return_20_for_a_most_loyal_customer(self):
        customer = Customer(first_purchase_date=self.now-10*self.year,
                            birth_date=self.now-20*self.year,
                            is_veteran=False)
        got = calculate_discount_percentage(customer)
        expected = 20
        self.assertEqual(got, expected)

    def test_should_return_maximum_discount(self):
        customer = Customer(first_purchase_date=None,
                            birth_date=self.now-20*self.year,
                            is_veteran=True)
        # eligible for 15% discount as a new client and 10% as a veteran
        got = calculate_discount_percentage(customer)
        expected = 15
        self.assertEqual(got, expected)

if __name__ == "__main__":
    unittest.main()
