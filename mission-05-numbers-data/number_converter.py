# Mission 5 — Decimal to Binary and Hexadecimal Number Converter

user_input = input("Enter a positive decimal integer: ")
decimal_number = int(user_input.strip())

binary_value = bin(decimal_number)
hex_value = hex(decimal_number)

print(f"Decimal input      : {decimal_number}")
print(f"Binary output      : {binary_value} (bits: {binary_value[2:]})")
print(f"Hexadecimal output : {hex_value} (hex digits: {hex_value[2:].upper()})")
