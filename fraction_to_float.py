def frac_to_float():
    repeat = 1
    while repeat == 1:
        fraction = input("Enter a fraction: ")
        if fraction.replace("/", "").isnumeric():
            if "/" in fraction:
                if not(fraction.split("/", 1)[1] == "0"):
                    if not (fraction.count("/") > 1):
                        repeat = 0
                        return float(fraction.split("/", 1)[0]) / float(fraction.split("/", 1)[1])
                    else:
                        print("Please use a single \"/\".\n")
                else:
                    print("What are you trying to do? (Cannot divide by zero.)\n")
            else:
                repeat = 0
                return float(fraction)
        else:
            print("Please provide a valid fraction.\n")


print(frac_to_float())
