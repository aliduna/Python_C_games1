import random
import time
from datetime import datetime


CHANCE_MODE_PROBABILITY = 55

CHANCE_MODES = [
    "Hell", "Burnt Bridge", "Angel", "Legend", "Impossible",
    "Invisible", "Hot Cold", "Reverse World", "Minefield",
    "Double Victory", "Fleeing Target", "Shifted Hint", "Single Chance",
    "Close Shot", "Three Lives", "Forbidden Digit", "Two Targets",
    "Against Time", "Prime Hunt",
]

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def draw_line():
    print("\n" + "=" * 52)

def show_date():
    now = datetime.now()
    month_name = MONTHS[now.month - 1]
    print(f"Date: {now.day} {month_name} {now.year} | Time: {now:%H:%M}")


def get_number(prompt, lower_bound, upper_bound):
    """Gets a valid integer from the user within the specified range."""
    while True:
        try:
            number = int(input(prompt))
            if lower_bound <= number <= upper_bound:
                return number
            print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Please enter a valid integer.")


def get_guess(lower_bound, upper_bound, secret_number=None):
    """Gets a guess or game control: s = skip turn, q = quit."""
    while True:
        user_input = input("\nYour guess (s: skip turn, q: quit): ").strip().lower()

        if user_input in ("s", "q"):
            return user_input

        # ! Temporary test command: shows the secret number during gameplay.
        # TODO needs to be removed later
        if user_input == "abcd12" and secret_number is not None:
            print(f"[TEST] Secret number: {secret_number}")
            continue

        try:
            number = int(user_input)
            if lower_bound <= number <= upper_bound:
                return number
            print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Please enter a number, 's', or 'q'.")


def select_main_mode():
    draw_line()
    print("                SELECT MAIN MODE")
    print("1 - Easy      (1 - 100)")
    print("2 - Normal    (1 - 200)")
    print("3 - Hard      (1 - 500)")
    print("4 - Hardcore  (1 - 500, only 10 attempts)")
    print("5 - Select    (manually pick a custom mode)")

    choice = get_number("Your choice: ", 1, 5)
    modes = {
        1: ("Easy", 100, None, None),
        2: ("Normal", 200, None, None),
        3: ("Hard", 500, None, None),
        4: ("Hardcore", 500, 10, None),
    }
    if choice == 5:
        return "Custom Mode", 200, None, select_custom_mode()
    return modes[choice]


def select_chance_mode():
    """Selects a random mode if the chance mode is triggered."""
    return random.choice(CHANCE_MODES)


def select_custom_mode():
    """Allows the player to select a custom mode directly without randomness."""
    draw_line()
    print("                SELECT CUSTOM MODE")
    for number, mode_name in enumerate(CHANCE_MODES, start=1):
        print(f"{number:2} - {mode_name}")
    choice = get_number("Your choice: ", 1, len(CHANCE_MODES))
    return CHANCE_MODES[choice - 1]


def hot_cold_hint(difference):
    if difference == 0:
        return ""
    if difference <= 2:
        return "BURNING UP! You are incredibly close!"
    if difference <= 5:
        return "Very hot!"
    if difference <= 10:
        return "Hot!"
    if difference <= 25:
        return "Warm..."
    if difference <= 50:
        return "Cool."
    if difference <= 100:
        return "Cold!"
    return "Freezing cold! You are very far away."

def is_prime(number):
    """Returns True if the number is prime, otherwise False."""
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def burnt_bridge_start():
    draw_line()
    print("BURNT BRIDGE MODE ACTIVE!")
    print("To cross the bridge, you must guess the number I chose between 1 and 4.")
    bridge_number = random.randint(1, 4)
    guess = get_guess(1, 4)

    if guess == "q":
        return "quit"
    if guess == "s":
        print("You skipped the bridge. You will play in the main mode.")
        return "skip"

    if guess == bridge_number:
        print("You crossed the bridge safely! Continuing in your selected mode.")
        return True

    print(f"The bridge collapsed! The number was: {bridge_number}")
    print("As a penalty, you must find a number between 1 and 10,000!")
    return False


def play_game():
    main_mode, upper_bound, attempt_limit, selected_custom_mode = select_main_mode()
    chance_mode = None

    if selected_custom_mode:
        chance_mode = selected_custom_mode
        draw_line()
        print(f"SELECTED MODE: {chance_mode.upper()}!")
        input("Press Enter to start...")
    elif random.randint(1, 100) <= CHANCE_MODE_PROBABILITY:
        chance_mode = select_chance_mode()
        draw_line()
        print(f"CHANCE MODE TRIGGERED: {chance_mode.upper()}!")
        input("Press Enter to start...")

    if chance_mode == "Hell":
        mode_name, upper_bound, attempt_limit = "Hell", 1000, None
    elif chance_mode == "Angel":
        mode_name, upper_bound, attempt_limit = "Angel", 50, None
    elif chance_mode == "Legend":
        mode_name, upper_bound, attempt_limit = "Legend", 10, None
    elif chance_mode == "Impossible":
        mode_name, upper_bound, attempt_limit = "Impossible", 1_000_000, None
    elif chance_mode == "Invisible":
        mode_name = "Invisible"
    elif chance_mode == "Hot Cold":
        mode_name = "Hot Cold"
    elif chance_mode == "Reverse World":
        mode_name = "Reverse World"
    elif chance_mode == "Minefield":
        mode_name = "Minefield"
    elif chance_mode == "Double Victory":
        mode_name = "Double Victory"
    elif chance_mode == "Fleeing Target":
        mode_name = "Fleeing Target"
    elif chance_mode == "Shifted Hint":
        mode_name = "Shifted Hint"
    elif chance_mode == "Single Chance":
        mode_name, attempt_limit = "Single Chance", 1
    elif chance_mode == "Close Shot":
        mode_name = "Close Shot"
    elif chance_mode == "Three Lives":
        mode_name = "Three Lives"
    elif chance_mode == "Forbidden Digit":
        mode_name = "Forbidden Digit"
    elif chance_mode == "Two Targets":
        mode_name = "Two Targets"
    elif chance_mode == "Against Time":
        mode_name = "Against Time"
    elif chance_mode == "Prime Hunt":
        mode_name = "Prime Hunt"
    elif chance_mode == "Burnt Bridge":
        bridge_result = burnt_bridge_start()
        if bridge_result == "quit":
            print("Closing the game. Goodbye!")
            return False
        if bridge_result == "skip":
            mode_name = "Burnt Bridge (skipped)"
        elif bridge_result:
            mode_name = "Burnt Bridge (successful)"
        else:
            mode_name, upper_bound, attempt_limit = "Burnt Bridge (penalty)", 10_000, None
    else:
        mode_name = main_mode

    secret_number = random.randint(1, upper_bound)
    attempts = 0
    wrong_attempts = 0
    start_time = time.monotonic()
    mines = set()
    double_victory_pending = False
    targets_found = 0
    forbidden_digit = None

    if chance_mode == "Minefield":
        while len(mines) < min(3, upper_bound - 1):
            mine = random.randint(1, upper_bound)
            if mine != secret_number:
                mines.add(mine)
    elif chance_mode == "Forbidden Digit":
        forbidden_digit = str(random.randint(0, 9))
    elif chance_mode == "Prime Hunt":
        while not is_prime(secret_number):
            secret_number = random.randint(1, upper_bound)

    draw_line()
    print(f"MODE: {mode_name}")
    print(f"I picked a number between 1 and {upper_bound}.")
    if attempt_limit:
        print(f"Attention: You only have {attempt_limit} attempts!")
    if chance_mode == "Legend":
        parity = "even" if secret_number % 2 == 0 else "odd"
        print(f"Legendary hint: The secret number is {parity}.")
    if chance_mode == "Invisible":
        print("Invisible mode: Half of your hints will disappear!")
    if chance_mode == "Hot Cold":
        print("Hot Cold mode: Instead of higher/lower, you will get distance-based hints.")
    if chance_mode == "Reverse World":
        print("Reverse World mode: Hints have a 50% chance of being inverted!")
    if chance_mode == "Minefield":
        print("Minefield mode: There are 3 mined numbers; hitting one ends the game!")
    if chance_mode == "Double Victory":
        print("Double Victory mode: After your first correct guess, you must find a newly chosen second number.")
    if chance_mode == "Fleeing Target":
        print("Fleeing Target mode: The secret number changes after every wrong guess.")
    if chance_mode == "Shifted Hint":
        print("Shifted Hint mode: Hints are based on your guess randomly shifted by ±5, ±10, or ±20.")
    if chance_mode == "Single Chance":
        print("Single Chance mode: You only get one single guess.")
    if chance_mode == "Close Shot":
        print("Close Shot mode: You win if your guess is within a difference of 3 or less.")
    if chance_mode == "Three Lives":
        print("Three Lives mode: The game ends after three wrong guesses.")
    if chance_mode == "Forbidden Digit":
        print(f"Forbidden Digit mode: Guesses containing '{forbidden_digit}' are banned; violation ends the game!")
    if chance_mode == "Two Targets":
        print("Two Targets mode: You must find two different secret numbers in a row.")
    if chance_mode == "Against Time":
        print("Against Time mode: You must make the correct guess within 45 seconds.")
    if chance_mode == "Prime Hunt":
        print("Prime Hunt mode: The secret number is prime. You can only guess prime numbers.")

    while True:
        if attempt_limit and attempts >= attempt_limit:
            print(f"\nNo attempts left. The number was {secret_number}.")
            return True
        if chance_mode == "Against Time" and time.monotonic() - start_time >= 45:
            print(f"\nTime's up! The number was {secret_number}.")
            return True

        guess = get_guess(1, upper_bound, secret_number)

        if guess == "q":
            print("Closing the game. Goodbye!")
            return False
        if guess == "s":
            attempts += 1
            print("Turn skipped. The secret number remains the same.")
            continue

        if chance_mode == "Against Time" and time.monotonic() - start_time >= 45:
            print(f"\nTime's up! The number was {secret_number}.")
            return True

        if chance_mode == "Forbidden Digit" and forbidden_digit in str(guess):
            print(f"\nYOU USED THE FORBIDDEN DIGIT! Guessing '{forbidden_digit}' ended the game.")
            return True

        if chance_mode == "Prime Hunt" and not is_prime(guess):
            print("This number is not prime. In Prime Hunt, you can only guess prime numbers.")
            continue

        attempts += 1

        if chance_mode == "Minefield" and guess in mines:
            print(f"\nYOU STEPPED ON A MINE! The mined number was {guess}. Game over.")
            return True

        if guess == secret_number:
            if chance_mode == "Two Targets" and targets_found == 0:
                targets_found = 1
                old_number = secret_number
                while secret_number == old_number:
                    secret_number = random.randint(1, upper_bound)
                print("First target found! Now you must find the second, different target.")
                continue
            if chance_mode == "Double Victory" and not double_victory_pending:
                double_victory_pending = True
                old_number = secret_number
                while secret_number == old_number:
                    secret_number = random.randint(1, upper_bound)
                print("First hit! I picked a new number; find it to claim ultimate victory.")
                continue
            print(f"\nCONGRATULATIONS! You got it in {attempts} attempts!")
            return True

        if chance_mode == "Close Shot" and abs(secret_number - guess) <= 3:
            print(f"\nCLOSE SHOT! The number was {secret_number}; you won with a difference of only {abs(secret_number - guess)}!")
            return True

        wrong_attempts += 1
        if chance_mode == "Three Lives":
            remaining_lives = 3 - wrong_attempts
            if remaining_lives <= 0:
                print(f"\nYou lost all three lives. The number was {secret_number}.")
                return True
            print(f"Remaining lives: {remaining_lives}")

        if attempt_limit:
            remaining = attempt_limit - attempts
            print(f"Attempts left: {remaining}")

        if chance_mode == "Hot Cold":
            print(hot_cold_hint(abs(secret_number - guess)))
        elif chance_mode == "Reverse World":
            invert_hint = random.choice([True, False])
            if (guess < secret_number) != invert_hint:
                print("Try a larger number.")
            else:
                print("Try a smaller number.")
        elif chance_mode == "Shifted Hint":
            shift = random.choice([-20, -10, -5, 5, 10, 20])
            shifted_guess = guess + shift
            if shifted_guess < secret_number:
                print("Try a larger number.")
            else:
                print("Try a smaller number.")
        elif chance_mode == "Invisible" and random.choice([True, False]):
            print("The hint became invisible...")
        elif guess < secret_number:
            print("Try a larger number.")
        else:
            print("Try a smaller number.")

        if chance_mode == "Fleeing Target":
            old_number = secret_number
            while secret_number == old_number:
                secret_number = random.randint(1, upper_bound)
            print("The target fled! I am choosing a new secret number now!")


def how_to_play():
    draw_line()
    print("                     HOW TO PLAY")
    print("Choose a main mode and try to guess the computer's secret number.")
    print(f"There is a {CHANCE_MODE_PROBABILITY}% chance a random modifier (Chance Mode) activates each round.")
    print("\nChance Modes:")
    print("- Hell: Range 1-1000")
    print("- Burnt Bridge: Guess a 1-4 number first; fail and face a 1-10000 penalty range")
    print("- Angel: Range 1-50")
    print("- Legend: Range 1-10 and an odd/even hint")
    print("- Impossible: Range 1-1000000")
    print("- Invisible: 50% of your hints are hidden")
    print("- Hot Cold: Distance-based temperature hints instead of higher/lower")
    print("- Reverse World: Higher/lower hints have a 50% chance of being inverted")
    print("- Minefield: Avoid 3 randomly placed hidden mines or it is instant game over")
    print("- Double Victory: Find the first number, then immediately find a second, new one")
    print("- Fleeing Target: The secret number changes after every wrong guess")
    print("- Shifted Hint: Hints are calculated using your guess shifted by ±5, ±10, or ±20")
    print("- Single Chance: You only get one single guess")
    print("- Close Shot: Win by getting within a difference of 3 or less of the secret number")
    print("- Three Lives: Game over after three incorrect guesses")
    print("- Forbidden Digit: Guesses containing a randomly selected digit are banned")
    print("- Two Targets: Must find two different secret numbers in a row")
    print("- Against Time: You must find the number within 45 seconds")
    print("- Prime Hunt: The secret number is prime; you can only make prime guesses")
    input("\nPress Enter to return to the main menu...")


def main_menu():
    while True:
        draw_line()
        print("          N U M B E R   G U E S S I N G   G A M E")
        show_date()
        print("1 - Start game")
        print("2 - How to play")
        print("3 - Exit")

        choice = get_number("Your choice: ", 1, 3)

        if choice == 1:
            continue_playing = play_game()
            if continue_playing is False:
                break
            input("\nPress Enter to return to the main menu...")
        elif choice == 2:
            how_to_play()
        else:
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main_menu()