import csv


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
            print("\nRequested Items")

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])
                if product_id in products:
                    product_info = products[product_id]
                    product_name = product_info[1]
                    price = float(product_info[2])
                    print(f"{product_name}: {quantity}, @ {price:.2f}")
                else:
                    print(f"Product ID {product_id} not found in the product list.")
    except FileNotFoundError:
        print(f"Error: The file '{REQUEST_FILE}' was not found.")
    except Exception as e:
        print(f"An error occurred while processing the receipt: {e}")


if __name__ == "__main__":
    main()
