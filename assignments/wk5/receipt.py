# Added days until New Year Sale begins
# Included docstrings for main function and read_dictionary function

import csv
from datetime import datetime


def read_dictionary(filename: str, key_column_index: int) -> dict:
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    try:
        with open(filename, "rt", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            result = {}
            for row in reader:
                key = row[key_column_index]
                result[key] = row
        return result
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def main():
    """
    Generates and prints a receipt for a thrift shop purchase.

    Reads product data from 'products.csv' and purchase requests from 'request.csv'.
    Calculates the subtotal, sales tax, and total for the requested items.
    Prints a formatted receipt showing each item, quantity, price, subtotal, sales tax, total,
    current date and time, and days remaining until the next New Year.

    Handles missing files and unknown product IDs with user-friendly error messages.
    """
    PRODUCTS_FILE = "products.csv"
    REQUEST_FILE = "request.csv"
    KEY_COLUMN_INDEX = 0

    products = read_dictionary(PRODUCTS_FILE, KEY_COLUMN_INDEX)

    if products:
        print("\nAll Products")
        print(products)

    else:
        print("Failed to load products.")

    try:
        with open(REQUEST_FILE, "rt") as file:
            reader = csv.reader(file)
            next(reader)
            number_of_items = 0
            subtotal = 0.0

            print("\nThrift Shop")

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                product_info = products[product_id]
                product_name = product_info[1]
                price = float(product_info[2])
                subtotal += quantity * price
                number_of_items += quantity
                print(f"{product_name}: {quantity}, @ {price:.2f}")

            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax

            next_year = datetime.now().year + 1
            days_before_new_year = (
                datetime(next_year, 1, 1).date() - datetime.now().date()
            ).days

            print(f"\nNumber of items: {number_of_items}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales tax: {sales_tax:.2f}")
            print(f"Total: {total:.2f}")

            print("\nThank you for shopping with us!")
            print(datetime.now().strftime("%a %b %-d %H:%M:%S %Y"))

            print(f"\nDays until New Year Sale begins (Jan 1): {days_before_new_year}")
    except FileNotFoundError:
        print(f"Error: The file '{REQUEST_FILE}' was not found.")
    except KeyError as e:
        print(f"Error: unknown product ID in the {REQUEST_FILE} file {e}.")
    except Exception as e:
        print(f"An error occurred while processing the receipt: {e}")


if __name__ == "__main__":
    main()
