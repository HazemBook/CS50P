def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    cost = float(d.removeprefix('$'))
    return cost


def percent_to_float(p):
    # TODO
    tipPercentage = float(p.removesuffix('%')) / 100
    return tipPercentage


main()
