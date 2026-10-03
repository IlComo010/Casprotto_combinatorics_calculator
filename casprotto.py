import os
import sys
import textwrap


# =========================================
# APPLICATION INFO
# =========================================

APP_NAME = "CASPROTTO — COMBINATORICS CALCULATOR"
VERSION = "1.0.0"
AUTHOR = "Casprotto"

BOX_WIDTH = 60
INNER_WIDTH = BOX_WIDTH - 2


# =========================================
# COLORS / INTERFACE
# =========================================

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"


# Python 3.11+ has a safety limit for converting very large integers
# to strings. The calculator works with exact integers, so allow
# large exact results to be displayed when the Python version supports it.
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


# =========================================
# INTERFACE HELPERS
# =========================================

def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.environ.get("TERM"):
        os.system("clear")
    else:
        print("\033[2J\033[H", end="")


def wrap_text(text, width=INNER_WIDTH):
    lines = []

    for raw_line in str(text).split("\n"):
        wrapped = textwrap.wrap(
            raw_line,
            width=width,
            break_long_words=True,
            break_on_hyphens=False
        )

        if wrapped:
            lines.extend(wrapped)
        else:
            lines.append("")

    return lines


def print_box_row(
    text="",
    border_color=CYAN,
    text_color=WHITE,
    bold=False,
    align="left"
):
    text = str(text)

    if align == "center":
        content = text.center(INNER_WIDTH)
    elif align == "right":
        content = text.rjust(INNER_WIDTH)
    else:
        content = text.ljust(INNER_WIDTH)

    style = BOLD if bold else ""

    print(
        border_color + "║" +
        style + text_color + content + RESET +
        border_color + "║" +
        RESET
    )


def print_title(title, border_color=CYAN):
    clear()

    title_lines = wrap_text(title, INNER_WIDTH)

    print(
        border_color +
        "╔" + "═" * INNER_WIDTH + "╗" +
        RESET
    )

    for line in title_lines:
        print_box_row(
            line,
            border_color=border_color,
            text_color=WHITE,
            bold=True,
            align="center"
        )

    print(
        border_color +
        "╚" + "═" * INNER_WIDTH + "╝" +
        RESET
    )

    print()


def print_panel(title, lines, border_color=MAGENTA):
    print(
        border_color +
        "╔" + "═" * INNER_WIDTH + "╗" +
        RESET
    )

    print_box_row(
        title,
        border_color=border_color,
        text_color=WHITE,
        bold=True,
        align="center"
    )

    print(
        border_color +
        "╠" + "═" * INNER_WIDTH + "╣" +
        RESET
    )

    for line in lines:
        for wrapped_line in wrap_text(line, INNER_WIDTH):
            print_box_row(
                wrapped_line,
                border_color=border_color,
                text_color=WHITE
            )

    print(
        border_color +
        "╚" + "═" * INNER_WIDTH + "╝" +
        RESET
    )


def pause():
    input(GRAY + "\nPress ENTER to continue..." + RESET)


def print_result(result, operation, calculation):
    info = OPERATION_INFO[operation]

    result_text = str(result)
    result_lines = wrap_text(result_text, 56)

    print()
    print(
        GREEN +
        "╔" + "═" * INNER_WIDTH + "╗" +
        RESET
    )

    print_box_row(
        "RESULT",
        border_color=GREEN,
        text_color=WHITE,
        bold=True,
        align="center"
    )

    print(
        GREEN +
        "╠" + "═" * INNER_WIDTH + "╣" +
        RESET
    )

    print_box_row(
        f"Operation: {info['NAME']}",
        border_color=GREEN,
        text_color=WHITE
    )

    print_box_row(
        f"Formula: {info['FORMULA']}",
        border_color=GREEN,
        text_color=WHITE
    )

    for line in wrap_text(
        f"Calculation: {calculation}",
        INNER_WIDTH
    ):
        print_box_row(
            line,
            border_color=GREEN,
            text_color=WHITE
        )

    print(
        GREEN +
        "╠" + "═" * INNER_WIDTH + "╣" +
        RESET
    )

    label = (
        "Result:"
        if operation == fattoriale
        else "Number of possible outcomes:"
    )

    print_box_row(
        label,
        border_color=GREEN,
        text_color=WHITE,
        bold=True,
        align="center"
    )

    for line in result_lines:
        print_box_row(
            line,
            border_color=GREEN,
            text_color=YELLOW,
            bold=True,
            align="center"
        )

    print(
        GREEN +
        "╚" + "═" * INNER_WIDTH + "╝" +
        RESET
    )


def print_error(title, message):
    print()
    print(
        RED +
        "╔" + "═" * INNER_WIDTH + "╗" +
        RESET
    )

    for line in wrap_text(title, INNER_WIDTH):
        print_box_row(
            line,
            border_color=RED,
            text_color=WHITE,
            bold=True,
            align="center"
        )

    print(
        RED +
        "╠" + "═" * INNER_WIDTH + "╣" +
        RESET
    )

    for line in wrap_text(message, INNER_WIDTH):
        print_box_row(
            line,
            border_color=RED,
            text_color=WHITE,
            align="center"
        )

    print(
        RED +
        "╚" + "═" * INNER_WIDTH + "╝" +
        RESET
    )


# =========================================
# MATHEMATICAL FUNCTIONS
# =========================================

def fattoriale(x):
    r = 1

    for i in range(1, x + 1):
        r *= i

    return r


# Simple formulas

def permutazione_semplice(n):
    return fattoriale(n)


def disposizione_semplice(n, k):
    return fattoriale(n) // fattoriale(n - k)


def combinazione_semplice(n, k):
    return fattoriale(n) // (
        fattoriale(k) * fattoriale(n - k)
    )


# Formulas with repetition

def permutazione_con_ripetizione(n, lista):
    nominatore = fattoriale(n)
    denominatore = 1

    for v in lista:
        denominatore *= fattoriale(v)

    return nominatore // denominatore


def disposizione_con_ripetizioni(n, k):
    return n ** k


def combinazione_con_ripetizione(n, k):
    numeratore = fattoriale(n + k - 1)
    denominatore = fattoriale(k) * fattoriale(n - 1)

    return numeratore // denominatore


# =========================================
# OPERATION INFORMATION
# =========================================

OPERATION_INFO = {

    fattoriale: {
        "NAME": "Factorial",
        "FORMULA": "N!",
        "INPUTS": "N"
    },

    permutazione_semplice: {
        "NAME": "Permutation",
        "FORMULA": "N!",
        "INPUTS": "N"
    },

    disposizione_semplice: {
        "NAME": "Arrangement",
        "FORMULA": "N! / (N-K)!",
        "INPUTS": "N, K"
    },

    combinazione_semplice: {
        "NAME": "Combination",
        "FORMULA": "N! / (K! * (N-K)!)",
        "INPUTS": "N, K"
    },

    permutazione_con_ripetizione: {
        "NAME": "Permutation with repetition",
        "FORMULA": "N! / (n1! * n2! * ...)",
        "INPUTS": "N, repetition counts"
    },

    disposizione_con_ripetizioni: {
        "NAME": "Arrangement with repetition",
        "FORMULA": "N^K",
        "INPUTS": "N, K"
    },

    combinazione_con_ripetizione: {
        "NAME": "Combination with repetition",
        "FORMULA": "(N+K-1)! / (K! * (N-1)!)",
        "INPUTS": "N, K"
    }
}


# =========================================
# CALCULATION DISPLAY
# =========================================

def build_calculation(operation, n, k=None, lista=None):

    if operation in (fattoriale, permutazione_semplice):
        return f"{n}!"

    if operation == disposizione_semplice:
        return f"{n}! / ({n}-{k})!"

    if operation == combinazione_semplice:
        return f"{n}! / ({k}! * ({n}-{k})!)"

    if operation == permutazione_con_ripetizione:
        denominator = " * ".join(
            f"{value}!"
            for value in lista
        )
        return f"{n}! / ({denominator})"

    if operation == disposizione_con_ripetizioni:
        return f"{n}^{k}"

    if operation == combinazione_con_ripetizione:
        return f"({n}+{k}-1)! / ({k}! * ({n}-1)!)"

    return ""


# =========================================
# WHAT SYSTEM
# =========================================

def what(operation):

    while True:

        print_title(
            "WHAT? — HELP",
            border_color=MAGENTA
        )

        data = what_answ.get(operation)

        if data is None:
            print_error(
                "HELP ERROR",
                "No help information is available for this operation."
            )
            pause()
            return

        options = data["ARGUMENTS"]

        print_panel(
            f"{data['TITLE']} — WHAT?",
            [f"[ {option} ]" for option in options],
            border_color=MAGENTA
        )

        print()
        print(GRAY + "Type ESC to return." + RESET)

        user_input = input(
            CYAN + "\nChoose an option ---> " + RESET
        ).strip().upper()

        if user_input == "ESC":
            return

        enter_answ(operation, user_input)


def enter_answ(operation, user_input):

    data = what_answ.get(operation)

    if data is None:
        print_error(
            "HELP ERROR",
            "No help information is available for this operation."
        )
        pause()
        return

    answer = data["ANSWERS"].get(user_input)

    if answer is not None:
        print_title(
            user_input,
            border_color=MAGENTA
        )

        print_panel(
            data["TITLE"],
            answer.split("\n"),
            border_color=MAGENTA
        )

        pause()
        return

    clear()

    print_error(
        "INVALID OPTION",
        "The selected WHAT option does not exist."
    )

    pause()
    clear()


# =========================================
# WHAT DATABASE
# =========================================

what_answ = {

    fattoriale: {
        "TITLE": "FACTORIAL",
        "ARGUMENTS": [
            "N",
            "FACTORIAL",
            "EXAMPLE"
        ],
        "ANSWERS": {
            "N":
                "N is the non-negative integer whose factorial you want to calculate.",

            "FACTORIAL":
                "The factorial of a non-negative integer N is the product of all positive integers from 1 to N.\n"
                "The formula is: N!",

            "EXAMPLE":
                "Example: if N = 5:\n"
                "5! = 5 * 4 * 3 * 2 * 1 = 120."
        }
    },

    permutazione_semplice: {
        "TITLE": "PERMUTATION",
        "ARGUMENTS": [
            "N",
            "PERMUTATION",
            "EXAMPLE"
        ],
        "ANSWERS": {
            "N":
                "N is the total number of available elements.",

            "PERMUTATION":
                "A permutation is used when you arrange ALL N distinct elements in a specific order.\n"
                "The formula is: N!",

            "EXAMPLE":
                "Example: if you have 3 elements (A, B, C), the possible permutations are:\n"
                "ABC, ACB, BAC, BCA, CAB, CBA\n"
                "Therefore, 3! = 6."
        }
    },

    disposizione_semplice: {
        "TITLE": "ARRANGEMENT",
        "ARGUMENTS": [
            "N",
            "K",
            "ARRANGEMENT",
            "EXAMPLE"
        ],
        "ANSWERS": {
            "N":
                "N is the total number of available elements.",

            "K":
                "K is the number of elements you want to choose and arrange.",

            "ARRANGEMENT":
                "An arrangement is used when you choose K distinct elements from N available elements and the order matters.\n"
                "The formula is: N! / (N-K)!",

            "EXAMPLE":
                "Example: with N = 5 and K = 2, you create ordered groups of 2 elements.\n"
                "5! / (5-2)! = 20."
        }
    },

    combinazione_semplice: {
        "TITLE": "COMBINATION",
        "ARGUMENTS": [
            "N",
            "K",
            "COMBINATION",
            "EXAMPLE"
        ],
        "ANSWERS": {
            "N":
                "N is the total number of available elements.",

            "K":
                "K is the number of elements you want to choose.",

            "COMBINATION":
                "A combination is used when you choose K distinct elements from N available elements and the order does NOT matter.\n"
                "The formula is: N! / (K! * (N-K)!).",

            "EXAMPLE":
                "Example: you have 5 people and want to choose 2 of them for a team.\n"
                "The order does not matter, so this is a combination.\n"
                "5! / (2! * 3!) = 10."
        }
    },

    permutazione_con_ripetizione: {
        "TITLE": "PERMUTATION WITH REPETITION",
        "ARGUMENTS": [
            "N",
            "REPETITION COUNTS",
            "PERMUTATION WITH REPETITION",
            "EXAMPLE"
        ],
        "ANSWERS": {
            "N":
                "N is the total number of elements, including repetitions.",

            "REPETITION COUNTS":
                "Enter how many times each repeated element appears.\n"
                "For example, 3,2 means one element appears 3 times and another appears 2 times.",

            "PERMUTATION WITH REPETITION":
                "A permutation with repetition is used when you arrange ALL the elements, but some elements are identical.\n"
                "The formula is: N! / (n1! * n2! * ...).",

            "EXAMPLE":
                "Example: the word MAMMA has 5 letters.\n"
                "M appears 3 times and A appears 2 times.\n"
                "5! / (3! * 2!) = 10."
        }
    },

    disposizione_con_ripetizioni: {
        "TITLE": "ARRANGEMENT WITH REPETITION",
        "ARGUMENTS": [
            "N",
            "K",
            "ARRANGEMENT WITH REPETITION",
            "EXAMPLE"
        ],
        "ANSWERS": {
            "N":
                "N is the number of available elements.",

            "K":
                "K is the number of positions you want to fill.",

            "ARRANGEMENT WITH REPETITION":
                "An arrangement with repetition is used when you choose K elements from N available elements, the order matters, and the same element can be chosen multiple times.\n"
                "The formula is: N^K.",

            "EXAMPLE":
                "Example: you have 3 symbols (A, B, C) and want sequences of length 2.\n"
                "Repetition is allowed, so AA, AB, AC, BA, BB, BC, CA, CB, and CC are possible.\n"
                "Therefore: 3^2 = 9."
        }
    },

    combinazione_con_ripetizione: {
        "TITLE": "COMBINATION WITH REPETITION",
        "ARGUMENTS": [
            "N",
            "K",
            "COMBINATION WITH REPETITION",
            "EXAMPLE"
        ],
        "ANSWERS": {
            "N":
                "N is the number of different available elements.",

            "K":
                "K is the number of elements you want to choose.",

            "COMBINATION WITH REPETITION":
                "A combination with repetition is used when you choose K elements from N available elements, the order does NOT matter, and repetition is allowed.\n"
                "The formula is: (N+K-1)! / (K! * (N-1)!).",

            "EXAMPLE":
                "Example: you have 3 ice cream flavors and want 2 scoops.\n"
                "You can choose the same flavor twice, and the order does not matter.\n"
                "(3+2-1)! / (2! * (3-1)!) = 6."
        }
    }
}


# =========================================
# INPUT VALIDATION
# =========================================

def is_integer(value):
    try:
        int(value)
        return True
    except (TypeError, ValueError):
        return False


def is_valid_integer_list(list_str):
    try:
        parts = [
            part.strip()
            for part in list_str.split(",")
        ]

        if not parts or any(part == "" for part in parts):
            return False

        for part in parts:
            int(part)

        return True

    except (AttributeError, TypeError, ValueError):
        return False


def transform_in_list(list_str):
    return [
        int(part.strip())
        for part in list_str.split(",")
    ]


# =========================================
# MATHEMATICAL VALIDATION
# =========================================

def valid_n(n):
    if n < 0:
        return "N cannot be negative."

    return True


def valid_n_k(n, k):
    if n < 0:
        return "N cannot be negative."

    if k < 0:
        return "K cannot be negative."

    if k > n:
        return "K cannot be greater than N."

    return True


def valid_n_k_r(n, k):
    if n < 1:
        return "N must be greater than 0."

    if k < 0:
        return "K cannot be negative."

    return True


def valid_n_list(n, lista):
    if n < 1:
        return "N must be greater than 0."

    if len(lista) == 0:
        return "The repetition list cannot be empty."

    for value in lista:
        if value <= 0:
            return "Every repetition value must be greater than 0."

    total = sum(lista)

    if total != n:
        return (
            "The sum of the repetition values must be equal to N.\n"
            f"Current sum: {total}\n"
            f"N: {n}"
        )

    return True


# =========================================
# INPUT SCREENS
# =========================================

def operation_title(operation, action):
    return f"{OPERATION_INFO[operation]['NAME'].upper()} — {action}"


def read_integer(prompt):
    value = input(
        CYAN + prompt + RESET
    ).strip()

    if value.upper() in ("WHAT", "ESC"):
        return value.upper()

    if not is_integer(value):
        clear()

        print_error(
            "FORMAT ERROR",
            'Enter an integer, or type "WHAT" or "ESC".'
        )

        pause()
        return None

    return int(value)


def insert_n(function, validator):
    operation = function

    while True:
        print_title(
            operation_title(operation, "ENTER N")
        )

        print(WHITE + "Enter the value of N.")
        print('Type "WHAT" for more information.')
        print("Type ESC to return to the main menu.")
        print()

        n = read_integer("Enter N ---> ")

        if n is None:
            continue

        if n == "WHAT":
            what(operation)
            continue

        if n == "ESC":
            return

        clear()

        validation = validator(n)

        if validation is not True:
            print_error(
                "MATHEMATICAL ERROR",
                validation
            )
            pause()
            continue

        result = function(n)
        calculation = build_calculation(
            operation,
            n
        )

        print_result(
            result,
            operation,
            calculation
        )

        pause()
        return


def insert_n_k(function, validator):
    operation = function

    while True:
        print_title(
            operation_title(operation, "ENTER N")
        )

        print(WHITE + "Enter the value of N.")
        print('Type "WHAT" for more information.')
        print("Type ESC to return to the main menu.")
        print()

        n = read_integer("Enter N ---> ")

        if n is None:
            continue

        if n == "WHAT":
            what(operation)
            continue

        if n == "ESC":
            return

        # Validate N before asking for K.
        if operation in (
            disposizione_semplice,
            combinazione_semplice
        ):
            validation = valid_n(n)

        else:
            validation = (
                "N must be greater than 0."
                if n < 1
                else True
            )

        if validation is not True:
            clear()

            print_error(
                "MATHEMATICAL ERROR",
                validation
            )

            pause()
            continue

        while True:
            print_title(
                operation_title(operation, "ENTER K")
            )

            print(WHITE + f"N = {n}")
            print()
            print("Enter the value of K.")
            print('Type "WHAT" for more information.')
            print("Type ESC to return to the main menu.")
            print()

            k = read_integer("Enter K ---> ")

            if k is None:
                continue

            if k == "WHAT":
                what(operation)
                continue

            if k == "ESC":
                return

            clear()

            validation = validator(n, k)

            if validation is not True:
                print_error(
                    "MATHEMATICAL ERROR",
                    validation
                )
                pause()
                continue

            result = function(n, k)
            calculation = build_calculation(
                operation,
                n,
                k=k
            )

            print_result(
                result,
                operation,
                calculation
            )

            pause()
            return


def insert_n_list(function, validator):
    operation = function

    while True:
        print_title(
            operation_title(operation, "ENTER N")
        )

        print(WHITE + "Enter the value of N.")
        print('Type "WHAT" for more information.')
        print("Type ESC to return to the main menu.")
        print()

        n = read_integer("Enter N ---> ")

        if n is None:
            continue

        if n == "WHAT":
            what(operation)
            continue

        if n == "ESC":
            return

        # Validate N before asking for repetition counts.
        validation = valid_n_k_r(n, 0)

        if validation is not True:
            clear()

            print_error(
                "MATHEMATICAL ERROR",
                validation
            )

            pause()
            continue

        while True:
            print_title(
                operation_title(
                    operation,
                    "ENTER REPETITION COUNTS"
                )
            )

            print(WHITE + f"N = {n}")
            print()
            print(
                "Enter how many times each repeated element appears."
            )
            print("Separate multiple values with commas.")
            print("Example: 3,2")
            print('Type "WHAT" for more information.')
            print("Type ESC to return to the main menu.")
            print()

            repetition_list = input(
                CYAN +
                "Enter repetition counts ---> " +
                RESET
            ).strip()

            if repetition_list.upper() == "WHAT":
                what(operation)
                continue

            if repetition_list.upper() == "ESC":
                return

            if not is_valid_integer_list(repetition_list):
                clear()

                print_error(
                    "FORMAT ERROR",
                    'Enter a comma-separated list of integers, or type "WHAT" or "ESC".'
                )

                pause()
                continue

            values = transform_in_list(
                repetition_list
            )

            clear()

            validation = validator(n, values)

            if validation is not True:
                print_error(
                    "MATHEMATICAL ERROR",
                    validation
                )
                pause()
                continue

            result = function(n, values)
            calculation = build_calculation(
                operation,
                n,
                lista=values
            )

            print_result(
                result,
                operation,
                calculation
            )

            pause()
            return


# =========================================
# ABOUT
# =========================================

def about():
    print_title("ABOUT")

    print_panel(
        APP_NAME,
        [
            f"Version {VERSION}",
            "",
            "An exact-integer calculator for basic combinatorics.",
            "",
            f"Created by {AUTHOR}.",
            "",
            "Calculations are performed using Python integers,",
            "so the mathematical results are exact."
        ],
        border_color=BLUE
    )

    print()
    print(
        GRAY +
        "Press ENTER to return to the main menu." +
        RESET
    )

    pause()


# =========================================
# MAIN MENU
# =========================================

def print_main_menu():
    print_title(APP_NAME)

    print_panel(
        "CHOOSE A CALCULATION",
        [
            "[F]   Factorial",
            "[P]   Permutation",
            "[A]   Arrangement",
            "[C]   Combination",
            "",
            "[PR]  Permutation with repetition",
            "[AR]  Arrangement with repetition",
            "[CR]  Combination with repetition",
            "",
            "[H]   About",
            "[Q]   Quit"
        ],
        border_color=CYAN
    )

    print()
    print(
        GRAY +
        "Inside a calculation, type WHAT for help." +
        RESET
    )

    print()


def main():
    while True:
        print_main_menu()

        user_input = input(
            CYAN +
            "Enter your choice ---> " +
            RESET
        ).strip().upper()

        if user_input == "P":
            insert_n(
                permutazione_semplice,
                valid_n
            )

        elif user_input == "A":
            insert_n_k(
                disposizione_semplice,
                valid_n_k
            )

        elif user_input == "C":
            insert_n_k(
                combinazione_semplice,
                valid_n_k
            )

        elif user_input == "PR":
            insert_n_list(
                permutazione_con_ripetizione,
                valid_n_list
            )

        elif user_input == "AR":
            insert_n_k(
                disposizione_con_ripetizioni,
                valid_n_k_r
            )

        elif user_input == "CR":
            insert_n_k(
                combinazione_con_ripetizione,
                valid_n_k_r
            )

        elif user_input == "F":
            insert_n(
                fattoriale,
                valid_n
            )

        elif user_input == "H":
            about()

        elif user_input in ("Q", "ESC"):
            break

        else:
            clear()

            print_error(
                "INVALID MENU OPTION",
                "That option does not exist.\n"
                "Choose one of the options shown in the menu."
            )

            pause()


# =========================================
# PROGRAM START
# =========================================

if __name__ == "__main__":
    try:
        main()

    except (KeyboardInterrupt, EOFError):
        clear()

        print()
        print(
            CYAN +
            "╔" + "═" * INNER_WIDTH + "╗" +
            RESET
        )

        print_box_row(
            "CASPROTTO CLOSED",
            border_color=CYAN,
            text_color=WHITE,
            bold=True,
            align="center"
        )

        print(
            CYAN +
            "╚" + "═" * INNER_WIDTH + "╝" +
            RESET
        )

        print()
        print(
            GRAY +
            "See you next time! =)" +
            RESET
        )

        print()