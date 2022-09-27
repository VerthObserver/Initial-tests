fraction_in = input("Enter a fraction: ")


def frac_to_float(fraction):
    if "/" in fraction:
        float_out = float(fraction.split("/", 1)[0]) / float(fraction.split("/", 1)[1])
        print(float_out)
    else:
        float_out = float(fraction)
        print(float_out)


frac_to_float(fraction_in)
