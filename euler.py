import math
import sys

pi = math.pi
e = math.e

print("Euler\'s Formula Calculator\nby Laevateinn\n")

# Input without spaces.
angle_in = input("Input angle in radians (Use \"pi\" for \u03C0 and \"/\" for fractions): ").replace(" ", "")

# Checks if input is numeric. For input with "pi", multiplies by pi. For input with "/", divides.
if "pi" in angle_in:
    angle_pi = angle_in.replace("pi", "")
    if "/" in angle_pi:
        if angle_pi.replace(".", "").replace("/", "").isnumeric():
            if angle_pi.split("/", 1)[0] == "":
                angle_final = 1 * pi / float(angle_pi.split("/", 1)[1])
            else:
                angle_final = float(angle_pi.split("/", 1)[0]) * pi / float(angle_pi.split("/", 1)[1])
        else:
            sys.exit("Please provide a valid angle value.")
    else:
        if angle_pi == "":
            angle_final = 1 * pi
        elif angle_pi.replace(".", "").isnumeric():
            angle_final = float(angle_pi) * pi
        else:
            sys.exit("Please provide a valid angle value.")

elif "/" in angle_in:
    if angle_in.replace(".", "").replace("/", "").isnumeric():
        angle_final = float(angle_in.split("/", 1)[0]) / float(angle_in.split("/", 1)[1])
    else:
        sys.exit("Please provide a valid angle value.")
elif angle_in.replace(".", "").isnumeric():
    angle_final = float(angle_in)
else:
    sys.exit("Please provide a valid angle value.")


def euler(angle):  # Euler's formula function.
    euler_value = e**(angle * 1j)
    return round(euler_value.real, 4) + round(euler_value.imag, 4) * 1j


print("Your result:", euler(angle_final))
