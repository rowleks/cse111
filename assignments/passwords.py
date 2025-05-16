# I added Type hints for all functions to enable static analysis and prevent runtime type errors.
# I also properly documented each functions purpose, arguments and returns.

# fmt: off
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", '"', "'", ",", ".", "<", ">", "?", "/", "`", "~"]


# fmt: on
def main():
    """
    Main function to interact with the user for password strength testing.
    Continuously prompts the user for a password until 'q' is entered.
    Calls `password_strength` to evaluate the password's strength.

    Args:
        None

    Returns:
        None
    """
    while True:
        password = input("Type the password you want to test (or 'q' to quit): ")
        if password.lower() == "q":
            break
        strength = password_strength(password)
        print(f"Password strength score: {strength}")


def word_in_file(word: str, filename: str, case_sensitive: bool = False) -> bool:
    """
    Checks if a given word exists in a file.

    Args:
        word (str): The word to search for.
        filename (str): The name of the file to search in.
        case_sensitive (bool): Whether the search should be case-sensitive. Defaults to False.

    Returns:
        bool: True if the word is found in the file, False otherwise.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            stripped_line = line.strip()
            if case_sensitive:
                if word == stripped_line:
                    return True
            else:
                if word.lower() == stripped_line.lower():
                    return True
    return False


def word_has_character(word: str, character_list: list) -> bool:
    """
    Checks if a word contains at least one character from a given list.

    Args:
        word (str): The word to check.
        character_list (list): A list of characters to look for.

    Returns:
        bool: True if the word contains at least one character from the list, False otherwise.
    """
    for letter in word:
        if letter in character_list:
            return True
    return False


def word_complexity(word: str) -> int:
    """
    Calculates the complexity of a word based on the presence of different character types.

    Args:
        word (str): The word to evaluate.

    Returns:
        int: A complexity score (0 to 4) based on the presence of lowercase, uppercase, digits, and special characters.
    """
    complexity_value = 0

    if word_has_character(word, LOWER):
        complexity_value += 1
    if word_has_character(word, UPPER):
        complexity_value += 1
    if word_has_character(word, DIGITS):
        complexity_value += 1
    if word_has_character(word, SPECIAL):
        complexity_value += 1

    return complexity_value


def password_strength(
    password: str, min_length: int = 10, strong_length: int = 16
) -> int:
    """
    Evaluates the strength of a password based on length, complexity, and dictionary checks.

    Args:
        password (str): The password to evaluate.
        min_length (int): The minimum acceptable length for a password. Defaults to 10.
        strong_length (int): The length at which a password is considered strong. Defaults to 16.

    Returns:
        int: A strength score (0 to 5) indicating the password's security level.
    """
    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure")
        return 0
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity, this is a good password.")
        return 5
    strength_score = word_complexity(password) + 1
    return strength_score


if __name__ == "__main__":
    main()
