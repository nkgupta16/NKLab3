def hex_to_dec(hex_number):
    decimal_number = int(hex_number, 16)
    return decimal_number


# Input a hexadecimal number
hex_number = input("Enter a number in hexadecimal format: ")

# Converting the hexadecimal number to decimal
decimal_number = hex_to_dec(hex_number)

print(f"The decimal equivalent of {hex_number} is {decimal_number}")
