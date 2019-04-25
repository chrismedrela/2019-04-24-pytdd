import unittest


TAX_RATE = 0.15
MINIMUM_SUBTOTAL_FOR_DISCOUNT = 100
DISCOUNT_RATE = 0.1


def calculate_subtotal():
    print('Calculate subtotal')
    return 400.0


def calculate_taxable_subtotal():
    print('Calculate taxable subtotal')
    return 300.0


def calculate_total():
    print('Calculate total')
    subtotal = calculate_subtotal()
    tax = calculate_taxable_subtotal() * TAX_RATE
    total = subtotal + tax
    qualifies_for_discount = subtotal > MINIMUM_SUBTOTAL_FOR_DISCOUNT
    if qualifies_for_discount:
        discount = subtotal * DISCOUNT_RATE
    else:
        discount = 0
    result = total - discount
    return result


if __name__ == "__main__":
    total = calculate_total()
    print('Total: {}'.format(total))
    