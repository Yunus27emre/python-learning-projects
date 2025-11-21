import sys


def found_current_value(volt,resis):
    try:
        return volt/resis
    except ZeroDivisionError:
        print("Resistance value is not equal to 0")
        sys.exit()


voltage_value=float(input("Enter the voltage value: "))
resistance_value=float(input("Enter the resistance value: "))

print(found_current_value(voltage_value, resistance_value))