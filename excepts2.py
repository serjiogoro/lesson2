def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
    except ValueError:
        print('ValueError')
        raise SystemExit(1)
    try:
        price = abs(price)
        discount = abs(discount)
    except TypeError:
        print('TypeError')
        raise SystemExit(1)
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
print(discounted('two handred',12,20))