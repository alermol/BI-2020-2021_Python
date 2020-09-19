print("Stranger, welcome in units converter!")
print("----------------------------------------------------------------------")
print("This converter can convert rounds per some time interval into all "
      "other available rounds per time interval")
print("----------------------------------------------------------------------")
print("Available units:")
print("RPW - Round per week")
print("RPD - Round per day")
print("RPH - Round per hour")
print("RPM - Round per minute")
print("----------------------------------------------------------------------")

converts_coef = {
    "RPW": {"RPD": (1 / 7), "RPH": (1 / 168), "RPM": (1 / 10080)},
    "RPD": {"RPW": 7, "RPH": (1 / 24), "RPM": (1 / 1440)},
    "RPH": {"RPW": 168, "RPD": 24, "RPM": (1 / 60)},
    "RPM": {"RPW": 10080, "RPD": 1440, "RPH": 60}
}

while True:
    unit_to_convert = input("Input one of the available units "
                            "or Exit to exit from script: ")
    if unit_to_convert.lower() == "exit":
        print("You choose to exit from script")
        break
    elif unit_to_convert.upper() in converts_coef.keys():
        print(f"You input is {unit_to_convert.upper()}")
        break
    else:
        print("You input something else. Try again.")

while True:
    unit_value = input("Input value to convert (decimal separator - point) "
                       "or Exit to exit from script: ")
    if unit_to_convert.lower() == "exit":
        print("You choose to exit from script")
        break
    try:
        unit_value = int(unit_value)
        break
    except ValueError:
        try:
            unit_value = float(unit_value)
            break
        except ValueError:
            print("Not a number")

print("----------------------------------------------------------------------")
print("Result")
print(f"Your input - {unit_value} {unit_to_convert.upper()}")
for unit in converts_coef[unit_to_convert.upper()].items():
    print(f"{unit_value} {unit_to_convert.upper()} = "
          f"{unit[1] * unit_value} {unit[0]}")
print("----------------------------------------------------------------------")
print("DONE")
