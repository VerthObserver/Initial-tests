fraction_in = input("Enter a fraction: ")


def frac_to_float(fraction):
    if "/" in fraction:
        return float(fraction.split("/", 1)[0]) / float(fraction.split("/", 1)[1])
    else:
        return float(fraction)


print(frac_to_float(fraction_in))
