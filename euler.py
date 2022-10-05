import math

pi = math.pi
e = math.e
repeat = 1

print("Euler\'s Formula Calculator\nby Laevateinn\n")

# Checks if input is numeric. For input with "pi", multiplies by pi. For input with "/", divides.
while repeat == 1:
    # Input without spaces.
    angle_in = input("Input angle in radians "
                     "(use \"pi\" for \u03C0 and \"/\" for fractions): ").replace(" ", "")
    if "pi" in angle_in and angle_in.replace("pi", "").replace(".", "").replace("/", "").isnumeric():
        angle_pi = angle_in.replace("pi", "")
        if "/" in angle_pi:
            if not(angle_pi.split("/", 1)[1] == "0"):
                if angle_pi.split("/", 1)[0] == "":
                    angle_final = 1 * pi / float(angle_pi.split("/", 1)[1])
                    repeat = 0
                else:
                    angle_final = float(angle_pi.split("/", 1)[0]) * pi / float(angle_pi.split("/", 1)[1])
                    repeat = 0
            else:
                print("What are you trying to do? (Cannot divide by zero.)\n")
        else:
            angle_final = float(angle_pi) * pi
            repeat = 0
    elif "pi" in angle_in and angle_in.replace("pi", "").replace(".", "") == "":
        angle_final = pi
        repeat = 0
    elif "/" in angle_in and angle_in.replace(".", "").replace("/", "").isnumeric():
        if not (angle_in.split("/", 1)[1] == "0"):
            if not(angle_in.split("/", 1)[0] == "" or angle_in.split("/", 1)[1] == ""):
                angle_final = float(angle_in.split("/", 1)[0]) / float(angle_in.split("/", 1)[1])
                repeat = 0
            else:
                print("Please provide a valid fraction.\n")
        else:
            print("What are you trying to do? (Cannot divide by zero.)\n")
    elif angle_in.replace(".", "").isnumeric():
        angle_final = float(angle_in)
        repeat = 0
    else:
        print("Please provide a valid angle value.\n")


def euler(angle):  # Euler's formula function.
    euler_value = e**(angle * 1j)
    return round(euler_value.real, 4) + round(euler_value.imag, 4) * 1j


print("Your result:", euler(angle_final))
